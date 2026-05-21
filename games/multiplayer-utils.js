/**
 * Multiplayer Game Utilities
 * Provides robust multiplayer support using Server API + polling + localStorage fallback
 */

class MultiplayerGameManager {
  constructor(options = {}) {
    this.gameId = null;
    this.playerId = null;
    this.playerName = '';
    this.opponentName = '';
    this.storageKey = null;
    this.pollInterval = options.pollInterval || 500; // ms
    this.pollTimer = null;
    this.isPollingActive = false;
    this.lastProcessedRound = 0;
    this.gameState = {};
    this.onStateChange = options.onStateChange || null;
    this.onGameReady = options.onGameReady || null;
    this.onRoundComplete = options.onRoundComplete || null;
  }

  /**
   * Create a new multiplayer game
   */
  async createGame(playerName) {
    if (!playerName || playerName.trim().length === 0) {
      throw new Error('Player name is required');
    }

    // Generate unique game code
    this.gameId = this.generateGameCode();
    this.playerId = 1;
    this.playerName = playerName.trim();
    this.storageKey = `mp-game-${this.gameId}`;

    // Initialize game state
    this.gameState = {
      gameId: this.gameId,
      createdAt: Date.now(),
      player1: {
        id: 1,
        name: this.playerName,
        score: 0,
        choice: null,
        ready: false
      },
      player2: {
        id: 2,
        name: '',
        score: 0,
        choice: null,
        ready: false
      },
      round: 1,
      maxRounds: 5,
      status: 'waiting', // waiting, playing, completed
      lastUpdate: Date.now(),
      lastRoundResult: null
    };

    await this.saveState();
    this.startPolling();

    return {
      gameId: this.gameId,
      gameUrl: this.getGameUrl()
    };
  }

  /**
   * Join an existing multiplayer game
   */
  async joinGame(gameId, playerName) {
    if (!gameId || gameId.trim().length === 0) {
      throw new Error('Game code is required');
    }
    if (!playerName || playerName.trim().length === 0) {
      throw new Error('Player name is required');
    }

    this.gameId = gameId.trim().toUpperCase();
    this.playerId = 2;
    this.playerName = playerName.trim();
    this.storageKey = `mp-game-${this.gameId}`;

    // Load existing game state
    const state = await this.loadState();
    if (!state) {
      throw new Error('Game not found. Check the game code.');
    }

    // Update player 2 info
    state.player2.name = this.playerName;
    state.status = 'playing';
    state.lastUpdate = Date.now();

    this.gameState = state;
    await this.saveState();
    this.startPolling();

    if (this.onGameReady) {
      this.onGameReady(this.gameState);
    }

    return this.gameState;
  }

  /**
   * Make a move in the game
   */
  async makeMove(choice) {
    if (!this.gameState || !this.storageKey) {
      throw new Error('Game not initialized');
    }

    const state = await this.loadState();
    if (!state) {
      throw new Error('Game state lost');
    }

    // Update player choice
    if (this.playerId === 1) {
      state.player1.choice = choice;
      state.player1.ready = true;
    } else {
      state.player2.choice = choice;
      state.player2.ready = true;
    }

    state.lastUpdate = Date.now();
    this.gameState = state;
    await this.saveState();

    // Check if both players have made their move
    if (state.player1.ready && state.player2.ready) {
      await this.resolveRound(state);
    }

    return state;
  }

  /**
   * Resolve a round (determine winner)
   */
  async resolveRound(state) {
    const p1Choice = state.player1.choice;
    const p2Choice = state.player2.choice;

    if (!p1Choice || !p2Choice) return;

    // Determine winner (override this in subclass for game-specific logic)
    const result = this.determineWinner(p1Choice, p2Choice);

    // Update scores
    if (result === 'player1') {
      state.player1.score += 1;
    } else if (result === 'player2') {
      state.player2.score += 1;
    }

    // Set lastRoundResult
    state.lastRoundResult = {
      result,
      p1Choice,
      p2Choice,
      scores: {
        player1: state.player1.score,
        player2: state.player2.score
      },
      round: state.round
    };

    // Reset for next round
    state.player1.choice = null;
    state.player1.ready = false;
    state.player2.choice = null;
    state.player2.ready = false;
    state.round += 1;

    // Check if game is complete
    if (state.round > state.maxRounds) {
      state.status = 'completed';
    }

    state.lastUpdate = Date.now();
    this.gameState = state;
    await this.saveState();

    if (this.onRoundComplete) {
      this.onRoundComplete(state.lastRoundResult);
    }
  }

  /**
   * Determine winner (override in subclass)
   */
  determineWinner(choice1, choice2) {
    // Default: tie
    return 'tie';
  }

  /**
   * Get current game state
   */
  async getState() {
    return (await this.loadState()) || this.gameState;
  }

  /**
   * Get game URL for sharing
   */
  getGameUrl() {
    const baseUrl = window.location.origin + window.location.pathname;
    return `${baseUrl}?game=${this.gameId}`;
  }

  /**
   * Save state to localStorage and Server
   */
  async saveState() {
    if (!this.storageKey) return;
    try {
      localStorage.setItem(this.storageKey, JSON.stringify(this.gameState));
    } catch (err) {
      console.error('Failed to save game state to localStorage:', err);
    }

    try {
      const response = await fetch('/api/multiplayer', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json'
        },
        body: JSON.stringify({
          gameId: this.gameId,
          state: this.gameState
        })
      });
      if (!response.ok) {
        throw new Error(`HTTP error! status: ${response.status}`);
      }
    } catch (err) {
      console.error('Failed to save game state to server:', err);
    }
  }

  /**
   * Load state from Server and fallback to localStorage
   */
  async loadState() {
    if (!this.storageKey) return null;
    let state = null;
    try {
      const response = await fetch(`/api/multiplayer?code=${encodeURIComponent(this.gameId)}`);
      if (response.ok) {
        state = await response.json();
      } else if (response.status === 404) {
        return null;
      }
    } catch (err) {
      console.error('Failed to load game state from server:', err);
    }

    if (!state) {
      try {
        const data = localStorage.getItem(this.storageKey);
        state = data ? JSON.parse(data) : null;
      } catch (err) {
        console.error('Failed to load game state from localStorage:', err);
      }
    }
    return state;
  }

  /**
   * Start polling for state changes
   */
  startPolling() {
    if (this.pollTimer) return;
    this.isPollingActive = true;
    this.lastProcessedRound = this.gameState && this.gameState.round ? this.gameState.round - 1 : 0;

    const poll = async () => {
      if (!this.isPollingActive) return;
      try {
        const newState = await this.loadState();
        if (newState && this.isPollingActive) {
          const stateChanged = JSON.stringify(newState) !== JSON.stringify(this.gameState);

          // Check if there is a new round result we haven't processed yet
          if (newState.lastRoundResult && newState.lastRoundResult.round > this.lastProcessedRound) {
            this.lastProcessedRound = newState.lastRoundResult.round;
            if (this.onRoundComplete) {
              this.onRoundComplete(newState.lastRoundResult);
            }
          }

          // Check if transition from waiting to playing occurred
          if (this.gameState && this.gameState.status === 'waiting' && newState.status === 'playing') {
            if (this.onGameReady) {
              this.onGameReady(newState);
            }
          }

          if (stateChanged) {
            this.gameState = newState;
            if (this.onStateChange) {
              this.onStateChange(newState);
            }
          }
        }
      } catch (err) {
        console.error('Error during polling:', err);
      }

      if (this.isPollingActive) {
        this.pollTimer = setTimeout(poll, this.pollInterval);
      }
    };

    this.pollTimer = setTimeout(poll, this.pollInterval);
  }

  /**
   * Stop polling
   */
  stopPolling() {
    this.isPollingActive = false;
    if (this.pollTimer) {
      clearTimeout(this.pollTimer);
      this.pollTimer = null;
    }
  }

  /**
   * Reset game
   */
  resetGame() {
    this.stopPolling();
    if (this.storageKey) {
      localStorage.removeItem(this.storageKey);
    }
    this.gameId = null;
    this.playerId = null;
    this.playerName = '';
    this.opponentName = '';
    this.storageKey = null;
    this.gameState = {};
  }

  /**
   * Generate unique game code
   */
  generateGameCode() {
    return Math.random().toString(36).substring(2, 8).toUpperCase();
  }

  /**
   * Check if game is ready (both players joined)
   */
  isGameReady() {
    return this.gameState &&
           this.gameState.player1 &&
           this.gameState.player1.name &&
           this.gameState.player2 &&
           this.gameState.player2.name;
  }

  /**
   * Check if game is complete
   */
  isGameComplete() {
    return this.gameState && this.gameState.status === 'completed';
  }

  /**
   * Get winner
   */
  getWinner() {
    if (!this.isGameComplete()) return null;

    const p1Score = this.gameState.player1.score;
    const p2Score = this.gameState.player2.score;

    if (p1Score > p2Score) {
      return {
        playerId: 1,
        playerName: this.gameState.player1.name,
        score: p1Score
      };
    } else if (p2Score > p1Score) {
      return {
        playerId: 2,
        playerName: this.gameState.player2.name,
        score: p2Score
      };
    } else {
      return {
        playerId: 0,
        playerName: 'Tie',
        score: p1Score
      };
    }
  }
}

// Export for use in games
window.MultiplayerGameManager = MultiplayerGameManager;
