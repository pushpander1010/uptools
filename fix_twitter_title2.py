#!/usr/bin/env python3
"""
Fix twitter:title tags that contain slug names instead of actual titles.
"""

import os
import re

BASE_DIR = "C:/ai/uptools"

def extract_meta_tag(content, attr_name, attr_value):
    """Extract a meta tag's content by attribute name and value."""
    pattern = rf'<meta\s+(?:[^>]*?\s+){re.escape(attr_name)}="{re.escape(attr_value)}"[^>]*?content="([^"]*?)"'
    match = re.search(pattern, content, re.IGNORECASE)
    if match:
        return match.group(1)
    
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
        title = title.replace('&amp;', '&').replace('&#39;', "'").replace('&quot;', '"')
        return title
    return None

def is_slug_name(name):
    """Check if a name looks like a slug (contains hyphens, lowercase only)."""
    if not name:
        return False
    return re.match(r'^[a-z0-9]+(-[a-z0-9]+)+$', name) is not None

def process_file(file_path):
    """Process a single index.html file."""
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    original_content = content
    
    # Extract twitter:title
    twitter_title = extract_meta_tag(content, 'name', 'twitter:title')
    
    if twitter_title and is_slug_name(twitter_title):
        # Get proper title from page title
        page_title = extract_title(content)
        og_title = extract_meta_tag(content, 'property', 'og:title')
        
        # Choose the best title
        if og_title and not is_slug_name(og_title):
            proper_title = og_title
        elif page_title:
            # Remove " | UpTools" suffix
            proper_title = re.sub(r'\s*\|\s*UpTools.*$', '', page_title, flags=re.IGNORECASE)
        else:
            tool_name = os.path.basename(os.path.dirname(file_path))
            proper_title = tool_name.replace('-', ' ').title()
        
        if proper_title and proper_title != twitter_title:
            # Replace the entire twitter:title tag using a simpler approach
            # Find and replace the tag
            pattern = r'<meta\s+(?:content="[^"]*"\s+)?name="twitter:title"\s+content="[^"]*"\s*/?>'
            if re.search(pattern, content, re.IGNORECASE):
                replacement = f'<meta name="twitter:title" content="{proper_title}" />'
                new_content = re.sub(pattern, replacement, content, count=1, flags=re.IGNORECASE)
                
                if new_content != content:
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
