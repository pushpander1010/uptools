#!/usr/bin/env python3
"""
Add missing Twitter Card tags (twitter:description and twitter:image) to files that are missing them.
"""

import os
import re

BASE_DIR = "C:/ai/uptools"
DEFAULT_IMAGE = "https://www.uptools.in/assets/home.png"

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

def process_file(file_path):
    """Process a single index.html file and add missing twitter tags."""
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    original_content = content
    changes = []
    
    # Check for twitter:card
    has_twitter_card = bool(re.search(r'name=["\']twitter:card["\']', content, re.IGNORECASE))
    
    if not has_twitter_card:
        # Add all twitter tags after og:image
        og_image = get_meta_content(content, 'property', 'og:image')
        og_title = get_meta_content(content, 'property', 'og:title')
        og_description = get_meta_content(content, 'property', 'og:description')
        
        # Find og:image tag
        og_image_pattern = r'<meta[^>]*property=["\']og:image["\'][^>]*>'
        og_image_match = re.search(og_image_pattern, content, re.IGNORECASE)
        
        if og_image_match:
            twitter_tags = f'''  <meta name="twitter:card" content="summary_large_image" />
  <meta name="twitter:title" content="{og_title or ''}" />
  <meta name="twitter:description" content="{og_description or ''}" />
  <meta name="twitter:image" content="{og_image or DEFAULT_IMAGE}" />'''
            
            insert_point = og_image_match.end()
            content = content[:insert_point] + '\n' + twitter_tags + content[insert_point:]
            changes.append("Added all twitter tags")
            return content, changes
    
    # twitter:card exists, check for missing tags
    missing_tags = []
    
    if not re.search(r'name=["\']twitter:description["\']', content, re.IGNORECASE):
        missing_tags.append('twitter:description')
    
    if not re.search(r'name=["\']twitter:image["\']', content, re.IGNORECASE):
        missing_tags.append('twitter:image')
    
    if missing_tags:
        # Find twitter:card tag to insert after
        twitter_card_pattern = r'<meta[^>]*name=["\']twitter:card["\'][^>]*>'
        twitter_card_match = re.search(twitter_card_pattern, content, re.IGNORECASE)
        
        if twitter_card_match:
            og_description = get_meta_content(content, 'property', 'og:description')
            og_image = get_meta_content(content, 'property', 'og:image')
            
            tags_to_add = ""
            for tag in missing_tags:
                if tag == 'twitter:description':
                    tags_to_add += f'\n  <meta name="twitter:description" content="{og_description or ""}" />'
                elif tag == 'twitter:image':
                    tags_to_add += f'\n  <meta name="twitter:image" content="{og_image or DEFAULT_IMAGE}" />'
            
            insert_point = twitter_card_match.end()
            content = content[:insert_point] + tags_to_add + content[insert_point:]
            changes.append(f"Added: {', '.join(missing_tags)}")
    
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
