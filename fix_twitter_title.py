#!/usr/bin/env python3
"""
Fix twitter:title tags that contain slug names instead of actual titles.
Also fix any remaining issues with OG/Twitter tags.
"""

import os
import re
import glob

BASE_DIR = "C:/ai/uptools"
DEFAULT_IMAGE = "https://www.uptools.in/assets/home.png"

def extract_meta_tag(content, attr_name, attr_value):
    """Extract a meta tag's content by attribute name and value."""
    # Match both formats: <meta name="xxx" content="yyy"> and <meta content="yyy" name="xxx">
    pattern = rf'<meta\s+(?:[^>]*?\s+){re.escape(attr_name)}="{re.escape(attr_value)}"[^>]*?content="([^"]*?)"'
    match = re.search(pattern, content, re.IGNORECASE)
    if match:
        return match.group(1)
    
    # Try reversed order
    pattern = rf'<meta\s+content="([^"]*?)"[^>]*?\s+{re.escape(attr_name)}="{re.escape(attr_value)}"[^>]*?>'
    match = re.search(pattern, content, re.IGNORECASE)
    if match:
        return match.group(1)
    
    return None

def extract_title(content):
    """Extract the page title."""
    match = re.search(r'<title>(.*?)</title>', content, re.IGNORECASE)
    if match:
        title = match.group(1).strip()
        # Decode HTML entities
        title = title.replace('&amp;', '&').replace('&#39;', "'").replace('&quot;', '"')
        return title
    return None

def is_slug_name(name):
    """Check if a name looks like a slug (contains hyphens, lowercase only)."""
    if not name:
        return False
    # If it's all lowercase with hyphens, it's likely a slug
    return re.match(r'^[a-z0-9]+(-[a-z0-9]+)+$', name) is not None

def fix_twitter_title(content, tool_name):
    """Fix twitter:title if it contains a slug name."""
    twitter_title = extract_meta_tag(content, 'name', 'twitter:title')
    
    if twitter_title and is_slug_name(twitter_title):
        # Get proper title from page title or og:title
        page_title = extract_title(content)
        og_title = extract_meta_tag(content, 'property', 'og:title')
        
        # Use og_title if available and not a slug, otherwise use page_title
        if og_title and not is_slug_name(og_title):
            proper_title = og_title
        elif page_title:
            # Remove " | UpTools" suffix for twitter title
            proper_title = re.sub(r'\s*\|\s*UpTools.*$', '', page_title, flags=re.IGNORECASE)
        else:
            # Convert slug to title case
            proper_title = tool_name.replace('-', ' ').title()
        
        # Replace the twitter:title tag
        if proper_title:
            # Try both attribute orders
            pattern = r'<meta\s+(?:content="[^"]*"\s+)?name="twitter:title"(?:\s+content="[^"]*")?\s*/?>'
            replacement = f'<meta name="twitter:title" content="{proper_title}" />'
            new_content = re.sub(pattern, replacement, content, flags=re.IGNORECASE)
            
            if new_content != content:
                return new_content, True, proper_title
    
    return content, False, None

def process_file(file_path):
    """Process a single index.html file."""
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    original_content = content
    
    # Extract tool name from file path
    tool_name = os.path.basename(os.path.dirname(file_path))
    
    # Fix twitter:title if needed
    content, changed, new_title = fix_twitter_title(content, tool_name)
    
    if content != original_content:
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
        return True, new_title
    
    return False, None

def main():
    # Find all index.html files (up to 2 levels deep)
    index_files = []
    for root, dirs, files in os.walk(BASE_DIR):
        # Skip certain directories
        dirs[:] = [d for d in dirs if d not in ['node_modules', '.git', 'dist', 'build']]
        
        if 'index.html' in files:
            index_files.append(os.path.join(root, 'index.html'))
        
        # Only go 2 levels deep
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
