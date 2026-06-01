#!/usr/bin/env python3
"""
Fix broken meta robots tags and duplicate meta/canonical tags across ALL tool index.html files.
"""

import os
import re
from pathlib import Path

def extract_keywords_from_broken_tag(line):
    """Extract keywords content from a broken meta tag like:
    <meta name="robots" content="ai blog generator, ..." name="keywords"/>
    """
    match = re.search(r'content="([^"]*)"', line)
    if match:
        return match.group(1)
    return None

def fix_broken_meta_robots(content, tool_name):
    """Fix the broken meta robots tag that has duplicate name attributes and keyword content."""
    # Pattern: <meta name="robots" content="keywords" name="keywords"/>
    broken_pattern = r'<meta\s+name="robots"\s+content="([^"]*)"\s+name="keywords"\s*/>'
    
    # Also handle variations
    broken_pattern2 = r'<meta\s+name="robots"\s+content="([^"]*)"\s+name="keywords"\s*>'
    
    # Match both patterns
    match = re.search(broken_pattern, content, re.IGNORECASE)
    if not match:
        match = re.search(broken_pattern2, content, re.IGNORECASE)
    
    if match:
        keywords_content = match.group(1)
        old_tag = match.group(0)
        
        # Create new tags
        new_robots_tag = '<meta name="robots" content="index,follow,max-snippet:-1,max-image-preview:large,max-video-preview:large" />'
        new_keywords_tag = f'<meta name="keywords" content="{keywords_content}" />'
        
        # Replace the broken tag with both new tags
        replacement = f'{new_robots_tag}\n{new_keywords_tag}'
        content = content.replace(old_tag, replacement)
        
        print(f"  ✓ Fixed broken meta robots tag for {tool_name}")
        print(f"    Extracted keywords: {keywords_content[:50]}...")
        return True, content
    
    return False, content

def fix_duplicate_canonical(content, tool_name):
    """Remove duplicate canonical tags, keeping only the first one."""
    # Find all canonical tags
    canonical_pattern = r'<link\s+[^>]*rel="canonical"[^>]*/>'
    canonical_pattern2 = r'<link\s+[^>]*rel="canonical"[^>]*>'
    
    matches1 = list(re.finditer(canonical_pattern, content, re.IGNORECASE))
    matches2 = list(re.finditer(canonical_pattern2, content, re.IGNORECASE))
    
    all_matches = matches1 + matches2
    
    if len(all_matches) > 1:
        # Keep only the first one
        first_match = all_matches[0]
        
        # Remove all others (from last to first to avoid index shifting)
        for match in reversed(all_matches[1:]):
            content = content[:match.start()] + content[match.end():]
        
        print(f"  ✓ Removed {len(all_matches) - 1} duplicate canonical tags for {tool_name}")
        print(f"    Kept: {first_match.group(0)[:80]}...")
        return True, content
    
    return False, content

def fix_duplicate_robots(content, tool_name):
    """Remove duplicate meta robots tags, keeping only one with proper content."""
    # Find all meta robots tags (including the broken pattern)
    robots_pattern1 = r'<meta\s+name="robots"\s+content="[^"]*"\s*/>'
    robots_pattern2 = r'<meta\s+name="robots"\s+content="[^"]*"\s*>'
    robots_pattern3 = r'<meta\s+name="robots"\s+content="[^"]*"\s+name="keywords"\s*/>'
    robots_pattern4 = r'<meta\s+name="robots"\s+content="[^"]*"\s+name="keywords"\s*>'
    # Also match: <meta content="..." name="robots"/>
    robots_pattern5 = r'<meta\s+content="[^"]*"\s+name="robots"\s*/>'
    robots_pattern6 = r'<meta\s+content="[^"]*"\s+name="robots"\s*>'
    # Also match: <meta content="index,follow..." /> (without name attribute)
    robots_pattern7 = r'<meta\s+content="index,follow[^"]*"\s*/>'
    
    all_patterns = [robots_pattern1, robots_pattern2, robots_pattern3, robots_pattern4,
                    robots_pattern5, robots_pattern6, robots_pattern7]
    
    all_matches = []
    seen_positions = set()
    
    for pattern in all_patterns:
        for match in re.finditer(pattern, content, re.IGNORECASE):
            if match.start() not in seen_positions:
                all_matches.append(match)
                seen_positions.add(match.start())
    
    # Sort by position
    all_matches.sort(key=lambda x: x.start())
    
    if len(all_matches) > 1:
        # Find the proper robots tag or create one
        proper_robots = '<meta name="robots" content="index,follow,max-snippet:-1,max-image-preview:large,max-video-preview:large" />'
        
        # Replace the first match with the proper robots tag
        first_match = all_matches[0]
        content = content[:first_match.start()] + proper_robots + content[first_match.end():]
        
        # Re-calculate positions after replacement
        length_diff = len(proper_robots) - len(first_match.group())
        
        # Remove remaining duplicates (from last to first)
        for match in reversed(all_matches[1:]):
            new_start = match.start() + length_diff
            new_end = match.end() + length_diff
            if new_start < len(content):
                content = content[:new_start] + content[new_end:]
        
        print(f"  ✓ Fixed {len(all_matches)} meta robots tags for {tool_name} (kept 1 proper)")
        return True, content
    
    elif len(all_matches) == 1:
        # Check if the single robots tag is proper
        match = all_matches[0]
        if 'name="robots"' not in match.group() and 'content="index,follow' not in match.group():
            # This is the orphaned meta content without name attribute
            proper_robots = '<meta name="robots" content="index,follow,max-snippet:-1,max-image-preview:large,max-video-preview:large" />'
            content = content[:match.start()] + proper_robots + content[match.end():]
            print(f"  ✓ Fixed orphaned meta robots tag for {tool_name}")
            return True, content
    
    return False, content

def fix_duplicate_keywords(content, tool_name):
    """Remove duplicate meta keywords tags, keeping only the first one."""
    # Find all keywords tags
    keywords_pattern1 = r'<meta\s+name="keywords"\s+content="[^"]*"\s*/>'
    keywords_pattern2 = r'<meta\s+name="keywords"\s+content="[^"]*"\s*>'
    
    all_matches = []
    seen_positions = set()
    
    for pattern in [keywords_pattern1, keywords_pattern2]:
        for match in re.finditer(pattern, content, re.IGNORECASE):
            if match.start() not in seen_positions:
                all_matches.append(match)
                seen_positions.add(match.start())
    
    # Sort by position
    all_matches.sort(key=lambda x: x.start())
    
    if len(all_matches) > 1:
        # Keep only the first one
        first_match = all_matches[0]
        
        # Remove all others (from last to first)
        for match in reversed(all_matches[1:]):
            content = content[:match.start()] + content[match.end():]
        
        print(f"  ✓ Removed {len(all_matches) - 1} duplicate keywords tags for {tool_name}")
        print(f"    Kept: {first_match.group(0)[:80]}...")
        return True, content
    
    return False, content

def process_file(file_path):
    """Process a single index.html file."""
    tool_name = file_path.parent.name
    
    with open(file_path, 'r', encoding='utf-8') as f:
        original_content = f.read()
    
    content = original_content
    changes_made = []
    
    # Fix broken meta robots tag
    fixed, content = fix_broken_meta_robots(content, tool_name)
    if fixed:
        changes_made.append("broken_meta_robots")
    
    # Fix duplicate canonical tags
    fixed, content = fix_duplicate_canonical(content, tool_name)
    if fixed:
        changes_made.append("duplicate_canonical")
    
    # Fix duplicate robots tags
    fixed, content = fix_duplicate_robots(content, tool_name)
    if fixed:
        changes_made.append("duplicate_robots")
    
    # Fix duplicate keywords tags
    fixed, content = fix_duplicate_keywords(content, tool_name)
    if fixed:
        changes_made.append("duplicate_keywords")
    
    # Save if changes were made
    if content != original_content:
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
        return True, changes_made
    
    return False, []

def main():
    base_dir = Path("C:/ai/uptools")
    
    # Find all index.html files
    html_files = list(base_dir.glob("*/index.html"))
    
    print(f"Found {len(html_files)} index.html files to process\n")
    
    fixed_count = 0
    skipped_count = 0
    total_changes = []
    
    for file_path in sorted(html_files):
        tool_name = file_path.parent.name
        
        try:
            changed, changes = process_file(file_path)
            if changed:
                fixed_count += 1
                total_changes.extend(changes)
                print(f"\n{tool_name}: Changes applied")
            else:
                skipped_count += 1
                print(f"\n{tool_name}: No changes needed")
        except Exception as e:
            print(f"\n{tool_name}: ERROR - {e}")
            import traceback
            traceback.print_exc()
    
    # Summary
    print("\n" + "="*60)
    print("SUMMARY")
    print("="*60)
    print(f"Files processed: {len(html_files)}")
    print(f"Files modified: {fixed_count}")
    print(f"Files skipped (no changes): {skipped_count}")
    print("\nChange types applied:")
    
    from collections import Counter
    change_counts = Counter(total_changes)
    for change_type, count in change_counts.items():
        print(f"  - {change_type}: {count} files")
    
    print("\n✅ All fixes applied successfully!")

if __name__ == "__main__":
    main()
