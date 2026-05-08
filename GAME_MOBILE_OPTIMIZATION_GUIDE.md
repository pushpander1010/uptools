# UpTools Games: Mobile Optimization & Canvas Sizing Guide

## Overview

This guide explains the issues with game canvas sizing on mobile devices and provides solutions to fix them across all 24 games.

## Current Issues Identified

### 1. **Canvas Sizing Problems**
- **2048**: ✅ Already fixed with ResizeObserver pattern
- **Snake**: ❌ D-pad overlaps game area on small screens
- **Tetris**: ❌ Canvas doesn't scale properly on mobile
- **Flappy Bird**: ❌ Canvas sizing issues in fullscreen
- **Tic-Tac-Toe**: ❌ Needs mobile optimization
- **Other games**: ❌ Similar issues across all 19 remaining games

### 2. **Touch Control Issues**
- **Flappy Bird**: ❌ No touch controls (tap to flap)
- **Tic-Tac-Toe**: ❌ Touch targets too small
- **Snake**: ⚠️ D-pad works but overlaps game
- **Other games**: ❌ Inconsistent touch support

### 3. **Fullscreen Mode Issues**
- **Snake**: ❌ D-pad not visible in fullscreen
- **2048**: ⚠️ Partially fixed but needs safe area support
- **All games**: ❌ No safe area support for notches/home bar

### 4. **Mobile-Specific Problems**
- **Layout Shift (CLS)**: Ads and score displays cause layout shifts
- **Viewport Issues**: URL bar jumps on iOS
- **Safe Areas**: Notches and home bars not accounted for
- **Orientation**: Landscape mode not optimized

## Solution: ResizeObserver Pattern

The 2048 game already implements the correct pattern. Here's how it works:

### Step 1: Create a Responsive Container

```html
<div class="board-outer" id="boardWrap">
  <div class="board-inner">
    <canvas id="game"></canvas>
  </div>
</div>
```

### Step 2: CSS for Responsive Sizing

```css
.board-outer {
  position: relative;
  display: flex;
  justify-content: center;
  align-items: center;
  padding: 0.5rem;
  border-radius: var(--radius);
  border: 1px solid var(--cardBorder);
  background: linear-gradient(180deg, rgba(255,255,255,.03), transparent);
}

.board-inner {
  position: relative;
  width: 100%;
  max-width: min(90vmin, 640px);
  aspect-ratio: 1;  /* Square board */
}

canvas {
  width: 100%;
  height: 100%;
  display: block;
  border-radius: var(--radius);
  background: #121a24;
  box-shadow: inset 0 0 0 2px var(--cardBorder);
  touch-action: none;  /* Important for gestures */
  image-rendering: pixelated;
  cursor: pointer;
}
```

### Step 3: JavaScript ResizeObserver

```javascript
// Responsive: fit square board to visible wrapper
function fitBoardSize() {
  const wrap = document.querySelector(".board-inner");
  if (!wrap) return;
  
  const cs = getComputedStyle(wrap);
  const padX = parseFloat(cs.paddingLeft) + parseFloat(cs.paddingRight);
  const padY = parseFloat(cs.paddingTop) + parseFloat(cs.paddingBottom);
  const availW = Math.max(160, wrap.clientWidth - padX);
  const availH = Math.max(180, wrap.clientHeight - padY);
  
  // Square that always fits - never clips
  const size = Math.floor(Math.min(availW, availH));
  canvas.width = size;
  canvas.height = size;
  
  // Re-position tiles/elements after size change
  redraw();
}

// Observe size changes (handles rotations, browser bars, split view)
const ro = new ResizeObserver(() => fitBoardSize());
ro.observe(document.querySelector(".board-inner"));
addEventListener('orientationchange', fitBoardSize, { passive: true });
```

## Safe Area Support for Notched Devices

### CSS Safe Area Padding

```css
@supports (padding: max(0px)) {
  .fullscreen-mode {
    padding-top: max(1rem, env(safe-area-inset-top));
    padding-bottom: max(1rem, env(safe-area-inset-bottom));
    padding-left: max(1rem, env(safe-area-inset-left));
    padding-right: max(1rem, env(safe-area-inset-right));
  }
  
  .board-outer {
    padding: max(0.5rem, env(safe-area-inset-top))
             max(0.5rem, env(safe-area-inset-right))
             max(0.5rem, env(safe-area-inset-bottom))
             max(0.5rem, env(safe-area-inset-left));
  }
}
```

### Viewport Meta Tag

```html
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover"/>
```

## D-Pad Positioning Fix (Snake Game)

### Current Problem
```css
.dpad {
  display: grid;
  grid-template-columns: repeat(3, 64px);
  gap: 0.5rem;
  place-content: center;
  margin-top: 0.75rem;  /* ❌ Overlaps game on small screens */
}
```

### Solution
```css
.dpad {
  display: grid;
  grid-template-columns: repeat(3, 64px);
  gap: 0.5rem;
  place-content: center;
  margin-top: 1rem;
  margin-bottom: 1rem;
  /* Ensure it doesn't overlap */
  position: relative;
  z-index: 10;
}

@media (max-width: 480px) {
  .dpad {
    grid-template-columns: repeat(3, 48px);  /* Smaller on mobile */
    gap: 0.25rem;
    margin-top: 0.5rem;
    margin-bottom: 0.5rem;
  }
  
  .dpad .cbtn {
    width: 48px;
    height: 48px;
    font-size: 1rem;
  }
}
```

## Touch Control Implementation

### Swipe Gestures

```javascript
let touchStart = null;

canvas.addEventListener('touchstart', (e) => {
  if (e.touches.length) {
    touchStart = {
      x: e.touches[0].clientX,
      y: e.touches[0].clientY,
      t: performance.now()
    };
  }
}, { passive: true });

canvas.addEventListener('touchend', (e) => {
  if (!touchStart) return;
  
  const dx = e.changedTouches[0].clientX - touchStart.x;
  const dy = e.changedTouches[0].clientY - touchStart.y;
  const ax = Math.abs(dx);
  const ay = Math.abs(dy);
  
  if (Math.max(ax, ay) > 18) {  // Threshold
    if (ax > ay) {
      // Horizontal swipe
      handleMove(Math.sign(dx) > 0 ? 'right' : 'left');
    } else {
      // Vertical swipe
      handleMove(Math.sign(dy) > 0 ? 'down' : 'up');
    }
  }
  
  touchStart = null;
}, { passive: true });
```

### Tap to Action (Flappy Bird)

```javascript
canvas.addEventListener('click', () => {
  if (!gameRunning) startGame();
  else flap();
});

canvas.addEventListener('touchstart', (e) => {
  e.preventDefault();
  if (!gameRunning) startGame();
  else flap();
}, { passive: false });
```

## Fullscreen Mode Optimization

### CSS for Fullscreen

```css
.fullscreen-mode {
  position: fixed !important;
  top: 0 !important;
  left: 0 !important;
  width: 100vw !important;
  height: 100dvh !important;  /* Use dynamic viewport height */
  background: var(--bg) !important;
  z-index: 9999 !important;
  margin: 0 !important;
  padding: max(1rem, env(safe-area-inset-top))
           max(1rem, env(safe-area-inset-right))
           max(1rem, env(safe-area-inset-bottom))
           max(1rem, env(safe-area-inset-left)) !important;
  display: flex !important;
  flex-direction: column !important;
  justify-content: center !important;
  align-items: center !important;
}

.fullscreen-mode .board-outer {
  max-width: min(85vmin, 700px) !important;
  width: 100% !important;
}

.fullscreen-mode .board-inner {
  max-width: min(85vmin, 700px) !important;
}
```

### JavaScript for Fullscreen

```javascript
function enterFullscreen() {
  document.body.classList.add('fullscreen-mode');
  
  // Create exit button
  const exitBtn = document.createElement('button');
  exitBtn.className = 'exit-fullscreen-btn';
  exitBtn.innerHTML = '✕ Exit Fullscreen';
  exitBtn.onclick = exitFullscreen;
  document.body.appendChild(exitBtn);
  
  // Recalculate board size
  fitBoardSize();
}

function exitFullscreen() {
  document.body.classList.remove('fullscreen-mode');
  document.querySelector('.exit-fullscreen-btn')?.remove();
  fitBoardSize();
}
```

## Preventing Layout Shift (CLS)

### Problem
Ads and score displays cause layout shifts when they load.

### Solution

```css
/* Reserve space for ads */
.ad-slot {
  min-height: 50px;  /* Standard ad height */
  background: rgba(255, 255, 255, 0.02);
  border: 1px dashed var(--border);
  border-radius: var(--radius);
  margin-bottom: 1rem;
}

/* Fixed HUD to prevent shift */
.hud {
  display: grid;
  grid-template-columns: repeat(4, 1fr);
  gap: 0.75rem;
  align-items: center;
  margin-bottom: 0.75rem;
  /* Prevent layout shift */
  min-height: 60px;
}

.kpi {
  text-align: center;
  padding: 0.5rem 0.75rem;
  border: 1px solid var(--cardBorder);
  border-radius: 0.75rem;
  background: rgba(255, 255, 255, 0.02);
  /* Prevent text shift */
  min-height: 50px;
  display: flex;
  flex-direction: column;
  justify-content: center;
}
```

## Testing Checklist

### Desktop Testing
- [ ] Game loads correctly
- [ ] Canvas is square and centered
- [ ] Keyboard controls work
- [ ] Mouse/click controls work
- [ ] Fullscreen button works
- [ ] Fullscreen mode displays correctly
- [ ] Exit fullscreen works

### Mobile Testing (Portrait)
- [ ] Game loads correctly
- [ ] Canvas fits screen without scrolling
- [ ] Touch controls work
- [ ] D-pad doesn't overlap game
- [ ] Score display is visible
- [ ] No layout shift when ads load
- [ ] Fullscreen mode works

### Mobile Testing (Landscape)
- [ ] Game loads correctly
- [ ] Canvas fits screen without scrolling
- [ ] Touch controls work
- [ ] D-pad is positioned correctly
- [ ] Score display is visible
- [ ] Fullscreen mode works

### Device Testing
- [ ] iPhone SE (small screen)
- [ ] iPhone 12/13 (notch)
- [ ] iPhone 14 Pro (Dynamic Island)
- [ ] iPad (tablet)
- [ ] Android phone (various sizes)
- [ ] Android tablet

### Orientation Testing
- [ ] Portrait to landscape transition
- [ ] Landscape to portrait transition
- [ ] Game state preserved during rotation
- [ ] Canvas resizes correctly

## Games to Update (Priority Order)

### High Priority (Most Issues)
1. **Snake** - D-pad overlap, mobile optimization
2. **Tetris** - Canvas sizing, touch controls
3. **Flappy Bird** - Touch controls, canvas sizing
4. **Tic-Tac-Toe** - Mobile optimization, touch targets

### Medium Priority
5. **Breakout** - Canvas sizing
6. **Pong** - Touch controls
7. **Memory Game** - Touch targets
8. **Simon Says** - Touch controls

### Lower Priority (Fewer Issues)
9-24. Other games - General mobile optimization

## Performance Considerations

- **ResizeObserver**: Minimal performance impact (~0.1ms per resize)
- **Touch events**: Use `passive: true` for better scrolling performance
- **Canvas rendering**: Use `image-rendering: pixelated` for retro games
- **Animations**: Respect `prefers-reduced-motion`

## Browser Support

✅ All modern browsers
✅ iOS Safari 13+
✅ Chrome Mobile 80+
✅ Samsung Internet 12+
✅ Firefox Mobile 68+

## Estimated Effort

- **Per game**: 30-45 minutes
- **All 24 games**: 12-18 hours
- **Testing**: 4-6 hours
- **Total**: 16-24 hours

## Questions?

Refer to:
- `2048/index.html` - Reference implementation
- `snake/index.html` - Example with D-pad
- `uptools-standards.md` - Design system
- `/style.css` - Global styles
