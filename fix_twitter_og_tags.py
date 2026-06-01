#!/usr/bin/env python3
"""
Add Twitter Card tags and fix OG descriptions across ALL index.html files in C:/ai/uptools.
1) Add Twitter Card meta tags where missing
2) Fix empty og:description tags
3) Ensure og:type is set to 'website'
4) Ensure og:site_name is 'UpTools'
"""

import os
import re
import glob

BASE_DIR = "C:/ai/uptools"
DEFAULT_IMAGE = "https://www.uptools.in/assets/home.png"
SITE_NAME = "UpTools"

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

def extract_description(content):
    """Extract meta description."""
    return extract_meta_tag(content, 'name', 'description')

def extract_og_description(content):
    """Extract og:description content."""
    return extract_meta_tag(content, 'property', 'og:description')

def extract_og_title(content):
    """Extract og:title content."""
    return extract_meta_tag(content, 'property', 'og:title')

def extract_og_url(content):
    """Extract og:url content."""
    return extract_meta_tag(content, 'property', 'og:url')

def extract_og_image(content):
    """Extract og:image content."""
    return extract_meta_tag(content, 'property', 'og:image')

def extract_tool_name_from_url(og_url, file_path):
    """Extract tool name from og:url or file path."""
    if og_url:
        # Extract from URL like https://www.uptools.in/whatsapp-font-generator/
        match = re.search(r'uptools\.in/([^/]+)/?', og_url)
        if match:
            return match.group(1)
    
    # Fall back to directory name
    return os.path.basename(os.path.dirname(file_path))

def generate_og_description(tool_name, title=None):
    """Generate an og:description based on the tool name."""
    # Convert hyphens to spaces and title case
    tool_words = tool_name.replace('-', ' ').title()
    if title:
        # Try to get a short version from title
        # Remove " | UpTools" and similar suffixes
        short_title = re.sub(r'\s*\|\s*UpTools.*$', '', title, flags=re.IGNORECASE)
        short_title = re.sub(r'\s*-\s*UpTools.*$', '', short_title, flags=re.IGNORECASE)
        if len(short_title) > 20:
            return f"{short_title}. Free online tool by UpTools."
    
    return f"Free online {tool_words} tool. Fast, easy to use, and privacy-first by UpTools."

def fix_og_description(content, tool_name, title, og_description, meta_description):
    """Fix empty or missing og:description."""
    if og_description and og_description.strip():
        return content, False
    
    # Use meta description if available, otherwise generate one
    if meta_description and meta_description.strip():
        new_desc = meta_description
    else:
        new_desc = generate_og_description(tool_name, title)
    
    # Find the og:description tag and replace it
    # Try different formats
    if 'property="og:description"' in content:
        # Replace empty or missing og:description
        pattern = r'<meta\s+property="og:description"\s+content="[^"]*"\s*/?>'
        replacement = f'<meta property="og:description" content="{new_desc}" />'
        new_content = re.sub(pattern, replacement, content, flags=re.IGNORECASE)
        
        # Also try reversed order
        if new_content == content:
            pattern = r'<meta\s+content="[^"]*"\s+property="og:description"\s*/?>'
            replacement = f'<meta property="og:description" content="{new_desc}" />'
            new_content = re.sub(pattern, replacement, content, flags=re.IGNORECASE)
        
        return new_content, True
    
    return content, False

def ensure_og_type(content):
    """Ensure og:type is set to 'website'."""
    if 'property="og:type"' in content.lower():
        # Check if it's already correct
        og_type = extract_meta_tag(content, 'property', 'og:type')
        if og_type and og_type.lower() == 'website':
            return content, False
    
    # Add og:type after og:title if it doesn't exist
    if 'property="og:type"' not in content:
        # Find og:title and add after it
        match = re.search(r'(<meta\s+property="og:title"[^>]*?/?>)', content, re.IGNORECASE)
        if match:
            insert_point = match.end()
            og_type_tag = '\n  <meta property="og:type" content="website">'
            new_content = content[:insert_point] + og_type_tag + content[insert_point:]
            return new_content, True
    
    return content, False

def ensure_og_site_name(content):
    """Ensure og:site_name is 'UpTools'."""
    if 'property="og:site_name"' in content.lower():
        # Check if it's already correct
        site_name = extract_meta_tag(content, 'property', 'og:site_name')
        if site_name and site_name == SITE_NAME:
            return content, False
        elif site_name:
            # Update existing og:site_name
            pattern = r'<meta\s+property="og:site_name"\s+content="[^"]*"\s*/?>'
            replacement = f'<meta property="og:site_name" content="{SITE_NAME}" />'
            new_content = re.sub(pattern, replacement, content, flags=re.IGNORECASE)
            
            if new_content == content:
                pattern = r'<meta\s+content="[^"]*"\s+property="og:site_name"\s*/?>'
                replacement = f'<meta property="og:site_name" content="{SITE_NAME}" />'
                new_content = re.sub(pattern, replacement, content, flags=re.IGNORECASE)
            
            return new_content, True
    
    # Add og:site_name after og:type
    match = re.search(r'(<meta\s+property="og:type"[^>]*?/?>)', content, re.IGNORECASE)
    if match:
        insert_point = match.end()
        site_name_tag = f'\n  <meta property="og:site_name" content="{SITE_NAME}">'
        new_content = content[:insert_point] + site_name_tag + content[insert_point:]
        return new_content, True
    
    return content, False

def add_twitter_card_tags(content, og_title, og_description, og_image, tool_name):
    """Add Twitter Card meta tags if missing."""
    changes = []
    
    # Check for twitter:card
    if 'name="twitter:card"' not in content and "name='twitter:card'" not in content:
        # Add all twitter tags after og:image
        twitter_tags = f'''  <meta name="twitter:card" content="summary_large_image" />
  <meta name="twitter:title" content="{og_title or tool_name}" />
  <meta name="twitter:description" content="{og_description}" />
  <meta name="twitter:image" content="{og_image or DEFAULT_IMAGE}" />'''
        
        # Find og:image tag and insert after it
        match = re.search(r'(<meta\s+property="og:image"[^>]*?/?>)', content, re.IGNORECASE)
        if match:
            insert_point = match.end()
            new_content = content[:insert_point] + '\n' + twitter_tags + content[insert_point:]
            return new_content, True, ["all_tags"]
    
    # Twitter card exists but might be missing other tags
    missing_tags = []
    
    if 'name="twitter:title"' not in content and "name='twitter:title'" not in content:
        missing_tags.append('twitter:title')
    
    if 'name="twitter:description"' not in content and "name='twitter:description'" not in content:
        missing_tags.append('twitter:description')
    
    if 'name="twitter:image"' not in content and "name='twitter:image'" not in content:
        missing_tags.append('twitter:image')
    
    if missing_tags:
        # Add missing tags after twitter:card
        twitter_block = ""
        for tag in missing_tags:
            if tag == 'twitter:title':
                twitter_block += f'\n  <meta name="twitter:title" content="{og_title or tool_name}" />'
            elif tag == 'twitter:description':
                twitter_block += f'\n  <meta name="twitter:description" content="{og_description}" />'
            elif tag == 'twitter:image':
                twitter_block += f'\n  <meta name="twitter:image" content="{og_image or DEFAULT_IMAGE}" />'
        
        match = re.search(r'(<meta\s+name="twitter:card"[^>]*?/?>)', content, re.IGNORECASE)
        if match:
            insert_point = match.end()
            new_content = content[:insert_point] + twitter_block + content[insert_point:]
            return new_content, True, missing_tags
    
    return content, False, []

def process_file(file_path):
    """Process a single index.html file."""
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    original_content = content
    changes = []
    
    # Extract existing information
    title = extract_title(content)
    og_title = extract_og_title(content)
    og_description = extract_og_description(content)
    meta_description = extract_description(content)
    og_image = extract_og_image(content)
    og_url = extract_og_url(content)
    
    # Determine tool name
    tool_name = extract_tool_name_from_url(og_url, file_path)
    
    # If og:description is empty or missing, fix it
    if not og_description or not og_description.strip():
        content, changed = fix_og_description(content, tool_name, title, og_description, meta_description)
        if changed:
            changes.append("Fixed empty og:description")
            og_description = extract_og_description(content) or meta_description or generate_og_description(tool_name, title)
    else:
        og_description = og_description.strip()
    
    # Ensure og:type is 'website'
    content, changed = ensure_og_type(content)
    if changed:
        changes.append("Added og:type")
    
    # Ensure og:site_name is 'UpTools'
    content, changed = ensure_og_site_name(content)
    if changed:
        changes.append("Added/fixed og:site_name")
    
    # Add Twitter Card tags if missing
    content, changed, added_tags = add_twitter_card_tags(content, og_title, og_description, og_image, tool_name)
    if changed:
        changes.append(f"Added Twitter Card tags: {', '.join(added_tags)}")
    
    # Write back if changed
    if content != original_content:
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
        return True, changes
    
    return False, []

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
    error_files = []
    
    for file_path in sorted(index_files):
        try:
            modified, changes = process_file(file_path)
            if modified:
                modified_files.append((file_path, changes))
                print(f"✓ Modified: {file_path}")
                for change in changes:
                    print(f"  - {change}")
        except Exception as e:
            error_files.append((file_path, str(e)))
            print(f"✗ Error processing {file_path}: {e}")
    
    print("-" * 60)
    print(f"Summary:")
    print(f"  Total files processed: {len(index_files)}")
    print(f"  Files modified: {len(modified_files)}")
    print(f"  Errors: {len(error_files)}")
    
    if error_files:
        print("\nErrors:")
        for file_path, error in error_files:
            print(f"  {file_path}: {error}")

if __name__ == '__main__':
    main()
