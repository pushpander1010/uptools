#!/usr/bin/env python3
"""
Fix twitter:title tags that contain slug names instead of actual titles.
Uses a more robust approach to extract and replace meta tags.
"""

import os
import re

BASE_DIR = "C:/ai/uptools"

def get_meta_content(content, attr_name, attr_value):
    """Extract content from a meta tag by attribute name/value. Handles any attribute order."""
    # Find the tag that has the specified attribute
    pattern = rf'<meta[^>]*{re.escape(attr_name)}=["\']({re.escape(attr_value)})["\'][^>]*>'
    match = re.search(pattern, content, re.IGNORECASE)
    if match:
        tag = match.group(0)
        # Extract content attribute
        content_match = re.search(r'content=["\']([^"\']+)["\']', tag)
        if content_match:
            return content_match.group(1)
    return None

def get_title(content):
    """Extract the page title."""
    match = re.search(r'<title>(.*?)</title>', content, re.IGNORECASE)
    if match:
        title = match.group(1).strip()
        # Decode common HTML entities
        title = title.replace('&amp;', '&').replace('&#39;', "'").replace('&quot;', '"')
        return title
    return None

def is_slug_name(name):
    """Check if a name looks like a slug (lowercase letters, numbers, hyphens)."""
    if not name:
        return False
    return bool(re.match(r'^[a-z0-9]+(-[a-z0-9]+)+$', name))

def process_file(file_path):
    """Process a single index.html file and fix twitter:title if needed."""
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    original_content = content
    
    # Get current twitter:title
    twitter_title = get_meta_content(content, 'name', 'twitter:title')
    
    if not twitter_title or not is_slug_name(twitter_title):
        return False, None
    
    # Get proper title from og:title or page title
    og_title = get_meta_content(content, 'property', 'og:title')
    page_title = get_title(content)
    
    # Choose best title
    if og_title and not is_slug_name(og_title):
        proper_title = og_title
    elif page_title:
        # Remove " | UpTools" or "- UpTools" suffix
        proper_title = re.sub(r'\s*[-|]\s*UpTools.*$', '', page_title, flags=re.IGNORECASE)
    else:
        # Convert slug to title case
        tool_name = os.path.basename(os.path.dirname(file_path))
        proper_title = tool_name.replace('-', ' ').title()
    
    if not proper_title or proper_title == twitter_title:
        return False, None
    
    # Build new tag - use the same format as original
    # Check original format
    tag_pattern = rf'<meta[^>]*name=["\']twitter:title["\'][^>]*>'
    tag_match = re.search(tag_pattern, content, re.IGNORECASE)
    
    if tag_match:
        original_tag = tag_match.group(0)
        # Check if original used single or double quotes for content
        if "content='" in original_tag or 'content="' not in original_tag:
            new_tag = f"<meta name='twitter:title' content='{proper_title}' />"
        else:
            new_tag = f'<meta name="twitter:title" content="{proper_title}" />'
        
        new_content = content[:tag_match.start()] + new_tag + content[tag_match.end():]
        
        if new_content != original_content:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(new_content)
            return True, proper_title
    
    return False, None

def main():
    index_files = []
    for root, dirs, files in os.walk(BASE_DIR):
        dirs[:] = [d for d in dirs if d not in ['node_modules', '.git', 'dist', 'build']]
        
        if 'index.html' in files:
            index_files.append(os.path.join(root, 'index.html'))
        
        if root.count(os.sep) - BASE_DIR.count(os.sep) >= 2:
            dirs.clear()
    
    print(f"Found {len(index_files)} index.html files to process")
    print("-" * 60)
    
    modified_files = []
    
    for file_path in sorted(index_files):
        try:
            modified, new_title = process_file(file_path)
            if modified:
                modified_files.append((file_path, new_title))
                print(f"✓ Fixed: {file_path}")
                print(f"  New twitter:title: {new_title}")
        except Exception as e:
            print(f"✗ Error processing {file_path}: {e}")
    
    print("-" * 60)
    print(f"Summary:")
    print(f"  Total files processed: {len(index_files)}")
    print(f"  Files modified: {len(modified_files)}")

if __name__ == '__main__':
    main()
