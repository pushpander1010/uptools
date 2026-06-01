#!/usr/bin/env python3
"""
Add complete OG and Twitter Card tags to files that are missing them entirely.
"""

import os
import re

BASE_DIR = "C:/ai/uptools"
DEFAULT_IMAGE = "https://www.uptools.in/assets/home.png"
SITE_NAME = "UpTools"

def get_meta_content(content, attr_name, attr_value):
    """Extract content from a meta tag by attribute name/value."""
    pattern = rf'<meta[^>]*{re.escape(attr_name)}=["\']({re.escape(attr_value)})["\'][^>]*>'
    match = re.search(pattern, content, re.IGNORECASE)
    if match:
        tag = match.group(0)
        content_match = re.search(r'content=["\']([^"\']+)["\']', tag)
        if content_match:
            return content_match.group(1)
    return None

def get_title(content):
    """Extract the page title."""
    match = re.search(r'<title>(.*?)</title>', content, re.IGNORECASE)
    if match:
        title = match.group(1).strip()
        title = title.replace('&amp;', '&').replace('&#39;', "'").replace('&quot;', '"')
        return title
    return None

def process_file(file_path):
    """Process a single index.html file and add missing tags."""
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    original_content = content
    changes = []
    
    # Extract tool name from URL or file path
    og_url = get_meta_content(content, 'property', 'og:url')
    if og_url:
        match = re.search(r'uptools\.in/([^/]+)/?', og_url)
        tool_name = match.group(1) if match else os.path.basename(os.path.dirname(file_path))
    else:
        tool_name = os.path.basename(os.path.dirname(file_path))
        # Check for localized paths like de/, es/, fr/
        parent = os.path.basename(os.path.dirname(os.path.dirname(file_path)))
        if parent in ['de', 'es', 'fr', 'pt', 'ja', 'ko', 'zh']:
            tool_name = os.path.basename(os.path.dirname(file_path))
    
    # Get title
    page_title = get_title(content)
    og_title = get_meta_content(content, 'property', 'og:title')
    og_description = get_meta_content(content, 'property', 'og:description')
    og_image = get_meta_content(content, 'property', 'og:image')
    meta_description = get_meta_content(content, 'name', 'description')
    
    # Build og block and twitter block
    title = og_title or page_title or tool_name.replace('-', ' ').title()
    description = og_description or meta_description or f"Free online {tool_name.replace('-', ' ').title()} tool by UpTools."
    image = og_image or DEFAULT_IMAGE
    url = og_url or f"https://www.uptools.in/{tool_name}/"
    
    # Check what's missing
    has_og_title = bool(re.search(r'property=["\']og:title["\']', content, re.IGNORECASE))
    has_og_description = bool(re.search(r'property=["\']og:description["\']', content, re.IGNORECASE))
    has_og_type = bool(re.search(r'property=["\']og:type["\']', content, re.IGNORECASE))
    has_og_url = bool(re.search(r'property=["\']og:url["\']', content, re.IGNORECASE))
    has_og_site_name = bool(re.search(r'property=["\']og:site_name["\']', content, re.IGNORECASE))
    has_og_image = bool(re.search(r'property=["\']og:image["\']', content, re.IGNORECASE))
    has_twitter_card = bool(re.search(r'name=["\']twitter:card["\']', content, re.IGNORECASE))
    has_twitter_title = bool(re.search(r'name=["\']twitter:title["\']', content, re.IGNORECASE))
    has_twitter_description = bool(re.search(r'name=["\']twitter:description["\']', content, re.IGNORECASE))
    has_twitter_image = bool(re.search(r'name=["\']twitter:image["\']', content, re.IGNORECASE))
    
    # If all twitter tags are missing, add them all
    if not has_twitter_card:
        # Find insertion point - after meta description or before style/link
        insert_patterns = [
            r'<meta\s+name="description"[^>]*>',
            r'<meta\s+name="robots"[^>]*>',
            r'<link[^>]*rel="canonical"[^>]*>',
        ]
        
        insert_point = None
        for pattern in insert_patterns:
            match = re.search(pattern, content, re.IGNORECASE)
            if match:
                insert_point = match.end()
                break
        
        if insert_point is None:
            # Insert after </head> or before <style>
            match = re.search(r'</head>|<style', content, re.IGNORECASE)
            if match:
                insert_point = match.start()
        
        if insert_point is not None:
            # Build og block if missing
            og_block = ""
            if not has_og_title or not has_og_description or not has_og_type or not has_og_url or not has_og_site_name or not has_og_image:
                og_block = "\n  <!-- Open Graph -->\n"
                if not has_og_title:
                    og_block += f'  <meta property="og:title" content="{title}" />\n'
                if not has_og_description:
                    og_block += f'  <meta property="og:description" content="{description}" />\n'
                if not has_og_type:
                    og_block += f'  <meta property="og:type" content="website" />\n'
                if not has_og_url:
                    og_block += f'  <meta property="og:url" content="{url}" />\n'
                if not has_og_site_name:
                    og_block += f'  <meta property="og:site_name" content="{SITE_NAME}" />\n'
                if not has_og_image:
                    og_block += f'  <meta property="og:image" content="{image}" />\n'
            
            # Build twitter block
            twitter_block = "\n  <!-- Twitter Card -->\n"
            twitter_block += f'  <meta name="twitter:card" content="summary_large_image" />\n'
            if not has_twitter_title:
                twitter_block += f'  <meta name="twitter:title" content="{title}" />\n'
            if not has_twitter_description:
                twitter_block += f'  <meta name="twitter:description" content="{description}" />\n'
            if not has_twitter_image:
                twitter_block += f'  <meta name="twitter:image" content="{image}" />\n'
            
            content = content[:insert_point] + og_block + twitter_block + content[insert_point:]
            changes.append("Added complete OG and Twitter Card tags")
    
    elif not has_twitter_title or not has_twitter_description or not has_twitter_image:
        # Add missing twitter tags after twitter:card
        twitter_card_match = re.search(r'<meta[^>]*name=["\']twitter:card["\'][^>]*>', content, re.IGNORECASE)
        if twitter_card_match:
            tags_to_add = ""
            if not has_twitter_title:
                tags_to_add += f'\n  <meta name="twitter:title" content="{title}" />'
            if not has_twitter_description:
                tags_to_add += f'\n  <meta name="twitter:description" content="{description}" />'
            if not has_twitter_image:
                tags_to_add += f'\n  <meta name="twitter:image" content="{image}" />'
            
            insert_point = twitter_card_match.end()
            content = content[:insert_point] + tags_to_add + content[insert_point:]
            changes.append(f"Added missing twitter tags")
    
    return content, changes

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
            new_content, changes = process_file(file_path)
            if changes:
                with open(file_path, 'w', encoding='utf-8') as f:
                    f.write(new_content)
                modified_files.append((file_path, changes))
                print(f"✓ Fixed: {file_path}")
                for change in changes:
                    print(f"  - {change}")
        except Exception as e:
            print(f"✗ Error processing {file_path}: {e}")
    
    print("-" * 60)
    print(f"Summary:")
    print(f"  Total files processed: {len(index_files)}")
    print(f"  Files modified: {len(modified_files)}")

if __name__ == '__main__':
    main()
