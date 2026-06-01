#!/usr/bin/env python3
"""
Accessibility improvements for ALL index.html files in C:/ai/uptools.

Tasks:
1) Add skip-to-content links where missing
2) Add CSS for .skip-link where missing
3) Ensure all <input> elements have proper aria-label or associated <label>
4) Ensure all <button> elements have aria-label or descriptive text
5) Add role="main" to <main> tags where missing
"""

import os
import re
import sys
from pathlib import Path

# Directories to skip
SKIP_DIRS = {'node_modules', 'dist', '.git', '__pycache__', '.wrangler'}

# Skip link HTML
SKIP_LINK_HTML = '<a href="#main" class="sr-only skip-link">Skip to content</a>'

# Skip link CSS
SKIP_LINK_CSS = """
    .skip-link {
      position: absolute;
      top: -40px;
      left: 0;
      background: #000;
      color: #fff;
      padding: 8px;
      z-index: 10000;
      transition: top 0.3s;
    }
    .skip-link:focus {
      top: 0;
    }
"""

def should_skip(path: Path) -> bool:
    """Check if path should be skipped."""
    for part in path.parts:
        if part in SKIP_DIRS:
            return True
    return False

def add_skip_link(html: str) -> tuple[str, bool]:
    """Add skip-to-content link after <body> if missing."""
    # Check if skip link already exists (with or without skip-link class)
    if 'href="#main"' in html and 'Skip to content' in html:
        # Check if it has skip-link class
        skip_match = re.search(r'<a[^>]*href="#main"[^>]*>Skip to content</a>', html)
        if skip_match:
            # Has skip link but might not have skip-link class
            if 'skip-link' not in skip_match.group():
                # Add skip-link class to existing skip link
                old_tag = skip_match.group()
                new_tag = old_tag.replace('class="sr-only"', 'class="sr-only skip-link"')
                if new_tag == old_tag:
                    # Try to add class attribute
                    new_tag = re.sub(r'<a\s+href="#main"', '<a href="#main" class="sr-only skip-link"', old_tag)
                html = html.replace(old_tag, new_tag)
            return html, False  # Already exists
        return html, False
    
    # Find <body> tag
    body_match = re.search(r'<body[^>]*>', html)
    if not body_match:
        print(f"  WARNING: No <body> tag found")
        return html, False
    
    body_end = body_match.end()
    
    # Insert skip link after <body>
    html = html[:body_end] + '\n  ' + SKIP_LINK_HTML + '\n' + html[body_end:]
    return html, True

def add_skip_link_css(html: str) -> tuple[str, bool]:
    """Add skip-link CSS if missing."""
    if '.skip-link' in html:
        return html, False
    
    # Find last </style> before </head>
    head_end_match = re.search(r'</head>', html, re.IGNORECASE)
    if not head_end_match:
        # No head tag, add before </style> at the end
        style_matches = list(re.finditer(r'</style>', html, re.IGNORECASE))
        if style_matches:
            last_style = style_matches[-1]
            html = html[:last_style.start()] + SKIP_LINK_CSS + '\n' + html[last_style.start():]
            return html, True
        return html, False
    
    head_end = head_end_match.start()
    
    # Find last </style> before </head>
    style_matches = list(re.finditer(r'</style>', html[:head_end], re.IGNORECASE))
    if style_matches:
        last_style = style_matches[-1]
        html = html[:last_style.start()] + SKIP_LINK_CSS + '\n' + html[last_style.start():]
        return html, True
    
    # No style tag found, add before </head>
    html = html[:head_end] + '<style>' + SKIP_LINK_CSS + '</style>\n' + html[head_end:]
    return html, True

def ensure_role_main(html: str) -> tuple[str, bool]:
    """Add role='main' to <main> tags where missing."""
    if not re.search(r'<main\b', html):
        return html, False
    
    # Check if role="main" already exists on any <main> tag
    main_matches = list(re.finditer(r'<main\b([^>]*)>', html))
    modified = False
    
    for match in main_matches:
        attrs = match.group(1)
        if 'role=' not in attrs:
            # Add role="main"
            old_tag = match.group(0)
            new_tag = old_tag.replace('<main ', '<main role="main" ', 1)
            if new_tag == old_tag:
                # Maybe no attributes, just <main>
                new_tag = old_tag.replace('<main>', '<main role="main">', 1)
            html = html[:match.start()] + new_tag + html[match.end():]
            modified = True
    
    return html, modified

def add_missing_main_tag(html: str) -> tuple[str, bool]:
    """For pages without <main>, wrap content in <main> tag."""
    if re.search(r'<main\b', html):
        return html, False
    
    # Find <header ...> </header> block
    header_match = re.search(r'<header\b[^>]*>.*?</header>', html, re.DOTALL)
    if not header_match:
        print(f"  WARNING: No <header> found for main wrapper")
        return html, False
    
    header_end = header_match.end()
    
    # Find </body>
    body_end_match = re.search(r'</body>', html, re.IGNORECASE)
    if not body_end_match:
        print(f"  WARNING: No </body> found for main wrapper")
        return html, False
    
    body_end = body_end_match.start()
    
    # Extract content between </header> and </body>
    content = html[header_end:body_end]
    
    # Check if there's a footer
    footer_match = re.search(r'<footer\b', content)
    
    if footer_match:
        # Wrap everything up to footer in <main>
        content_before_footer = content[:footer_match.start()]
        content_after_footer = content[footer_match.start():]
        
        # Find indent level
        indent_match = re.search(r'\n([ \t]*)', content_before_footer)
        indent = indent_match.group(1) if indent_match else '  '
        
        new_content = f'\n{indent}<main id="main" role="main" class="wrap">{content_before_footer}\n{indent}</main>\n{content_after_footer}'
        html = html[:header_end] + new_content + html[body_end:]
    else:
        # No footer, wrap everything
        indent_match = re.search(r'\n([ \t]*)', content)
        indent = indent_match.group(1) if indent_match else '  '
        
        new_content = f'\n{indent}<main id="main" role="main" class="wrap">{content}\n{indent}</main>'
        html = html[:header_end] + new_content + html[body_end:]
    
    return html, True

def get_accessible_name_for_input(input_tag: str, preceding_text: str) -> str:
    """Generate an accessible name for an input based on context."""
    # Check for placeholder
    placeholder_match = re.search(r'placeholder="([^"]*)"', input_tag)
    placeholder = placeholder_match.group(1) if placeholder_match else ''
    
    # Check for id to find associated label
    id_match = re.search(r'id="([^"]*)"', input_tag)
    input_id = id_match.group(1) if id_match else ''
    
    # Check for type
    type_match = re.search(r'type="([^"]*)"', input_tag)
    input_type = type_match.group(1) if type_match else 'text'
    
    # Try to find aria-label already set
    aria_match = re.search(r'aria-label="([^"]*)"', input_tag)
    if aria_match:
        return None  # Already has aria-label
    
    # Try to find nearby label by id
    if input_id:
        # Look for <label for="ID"> in preceding text
        label_match = re.search(rf'<label[^>]*for="{re.escape(input_id)}"[^>]*>(.*?)</label>', preceding_text, re.DOTALL)
        if label_match:
            return None  # Has associated label
    
    # Generate name from context
    # Check for nearby text patterns like "Label:" or "Label"
    context_patterns = [
        r'<label[^>]*>([^<]*)</label>\s*:?\s*$',  # Previous label
        r'<span[^>]*>([^<]*)</span>\s*:?\s*$',  # Previous span text
        r'<h[1-6][^>]*>([^<]*)</h[1-6]>\s*:?\s*$',  # Previous heading
        r'>([^<]{2,50}):?\s*<\s*/\s*(?:label|span|p|div|h[1-6])',  # Text before closing tag
    ]
    
    for pattern in context_patterns:
        context_match = re.search(pattern, preceding_text[-500:], re.MULTILINE)
        if context_match:
            text = context_match.group(1).strip().rstrip(':').strip()
            if text and len(text) > 1:
                return text
    
    # Fallback to placeholder
    if placeholder:
        return placeholder
    
    # Fallback to input type
    type_names = {
        'text': 'Text input',
        'email': 'Email input',
        'password': 'Password input',
        'number': 'Number input',
        'tel': 'Phone input',
        'url': 'URL input',
        'search': 'Search input',
        'date': 'Date input',
        'time': 'Time input',
        'datetime-local': 'Date and time input',
        'month': 'Month input',
        'week': 'Week input',
        'color': 'Color input',
        'range': 'Range input',
        'file': 'File input',
        'hidden': None,
        'submit': 'Submit button',
        'reset': 'Reset button',
        'button': 'Button',
        'checkbox': 'Checkbox',
        'radio': 'Radio button',
    }
    
    return type_names.get(input_type, 'Input')

def add_labels_to_inputs(html: str) -> tuple[str, int]:
    """Add aria-label to inputs missing labels."""
    # Find all <input> tags
    input_pattern = re.compile(r'<input\b([^>]*)/?>', re.DOTALL | re.IGNORECASE)
    
    modifications = 0
    last_end = 0
    new_html = []
    
    for match in input_pattern.finditer(html):
        input_tag = match.group(0)
        attrs = match.group(1)
        
        # Skip hidden inputs and inputs that already have aria-label
        if 'type="hidden"' in attrs or 'aria-label' in attrs or 'aria-labelledby' in attrs:
            continue
        
        # Check for associated label
        id_match = re.search(r'id="([^"]*)"', attrs)
        if id_match:
            input_id = id_match.group(1)
            # Check if label exists in html
            if re.search(rf'<label[^>]*for="{re.escape(input_id)}"', html):
                continue
        
        # Get preceding context
        preceding = html[max(0, match.start()-1000):match.start()]
        
        # Generate accessible name
        accessible_name = get_accessible_name_for_input(input_tag, preceding)
        
        if accessible_name:
            # Add aria-label
            new_tag = input_tag.replace('<input ', f'<input aria-label="{accessible_name}" ', 1)
            new_html.append(html[last_end:match.start()])
            new_html.append(new_tag)
            last_end = match.end()
            modifications += 1
    
    if modifications > 0:
        new_html.append(html[last_end:])
        html = ''.join(new_html)
    
    return html, modifications

def add_labels_to_buttons(html: str) -> tuple[str, int]:
    """Add aria-label to buttons missing accessible names."""
    # Find all <button> tags
    button_pattern = re.compile(r'<button\b([^>]*)>(.*?)</button>', re.DOTALL | re.IGNORECASE)
    
    modifications = 0
    last_end = 0
    new_html = []
    
    for match in button_pattern.finditer(html):
        button_tag = match.group(0)
        attrs = match.group(1)
        content = match.group(2)
        
        # Skip if already has aria-label or aria-labelledby
        if 'aria-label' in attrs or 'aria-labelledby' in attrs:
            continue
        
        # Check if button has accessible text content
        # Strip HTML tags from content
        text_content = re.sub(r'<[^>]+>', '', content).strip()
        
        if text_content and len(text_content) >= 1:
            continue  # Has visible text
        
        # Check for img alt text inside button
        img_match = re.search(r'alt="([^"]*)"', content)
        if img_match and img_match.group(1):
            continue
        
        # Button has no accessible text, generate one
        # Check for class to determine purpose
        class_match = re.search(r'class="([^"]*)"', attrs)
        classes = class_match.group(1) if class_match else ''
        
        id_match = re.search(r'id="([^"]*)"', attrs)
        btn_id = id_match.group(1) if id_match else ''
        
        # Generate aria-label from context
        accessible_name = None
        
        # Check common patterns
        if 'fullscreen' in classes.lower() or 'fullscreen' in btn_id.lower():
            accessible_name = 'Toggle fullscreen'
        elif 'close' in classes.lower() or 'close' in btn_id.lower():
            accessible_name = 'Close'
        elif 'delete' in classes.lower() or 'delete' in btn_id.lower():
            accessible_name = 'Delete'
        elif 'copy' in classes.lower() or 'copy' in btn_id.lower():
            accessible_name = 'Copy'
        elif 'paste' in classes.lower() or 'paste' in btn_id.lower():
            accessible_name = 'Paste'
        elif 'clear' in classes.lower() or 'clear' in btn_id.lower():
            accessible_name = 'Clear'
        elif 'submit' in classes.lower() or 'submit' in btn_id.lower():
            accessible_name = 'Submit'
        elif 'add' in classes.lower() or 'add' in btn_id.lower():
            accessible_name = 'Add'
        elif 'remove' in classes.lower() or 'remove' in btn_id.lower():
            accessible_name = 'Remove'
        elif 'save' in classes.lower() or 'save' in btn_id.lower():
            accessible_name = 'Save'
        elif 'load' in classes.lower() or 'load' in btn_id.lower():
            accessible_name = 'Load'
        elif 'download' in classes.lower() or 'download' in btn_id.lower():
            accessible_name = 'Download'
        elif 'upload' in classes.lower() or 'upload' in btn_id.lower():
            accessible_name = 'Upload'
        elif 'share' in classes.lower() or 'share' in btn_id.lower():
            accessible_name = 'Share'
        elif 'menu' in classes.lower() or 'menu' in btn_id.lower():
            accessible_name = 'Menu'
        elif 'nav' in classes.lower() or 'nav' in btn_id.lower():
            accessible_name = 'Navigation'
        elif 'back' in classes.lower() or 'back' in btn_id.lower():
            accessible_name = 'Go back'
        elif 'next' in classes.lower() or 'next' in btn_id.lower():
            accessible_name = 'Next'
        elif 'prev' in classes.lower() or 'prev' in btn_id.lower():
            accessible_name = 'Previous'
        elif 'play' in classes.lower() or 'play' in btn_id.lower():
            accessible_name = 'Play'
        elif 'pause' in classes.lower() or 'pause' in btn_id.lower():
            accessible_name = 'Pause'
        elif 'stop' in classes.lower() or 'stop' in btn_id.lower():
            accessible_name = 'Stop'
        elif 'reset' in classes.lower() or 'reset' in btn_id.lower():
            accessible_name = 'Reset'
        elif 'start' in classes.lower() or 'start' in btn_id.lower():
            accessible_name = 'Start'
        
        if not accessible_name:
            accessible_name = 'Button'
        
        # Add aria-label
        new_tag = button_tag.replace('<button ', f'<button aria-label="{accessible_name}" ', 1)
        new_html.append(html[last_end:match.start()])
        new_html.append(new_tag)
        last_end = match.end()
        modifications += 1
    
    if modifications > 0:
        new_html.append(html[last_end:])
        html = ''.join(new_html)
    
    return html, modifications

def process_file(file_path: Path) -> dict:
    """Process a single index.html file."""
    result = {
        'path': str(file_path.relative_to(Path('C:/ai/uptools'))),
        'changes': []
    }
    
    try:
        html = file_path.read_text(encoding='utf-8', errors='ignore')
    except Exception as e:
        result['error'] = str(e)
        return result
    
    original_html = html
    
    # 1) Add skip link
    html, added = add_skip_link(html)
    if added:
        result['changes'].append('added_skip_link')
    
    # 2) Add skip link CSS
    html, added = add_skip_link_css(html)
    if added:
        result['changes'].append('added_skip_link_css')
    
    # 3) Ensure role="main" on <main> tags
    html, added = ensure_role_main(html)
    if added:
        result['changes'].append('added_role_main')
    
    # 4) Add labels to inputs
    html, count = add_labels_to_inputs(html)
    if count > 0:
        result['changes'].append(f'added_aria_labels_to_{count}_inputs')
    
    # 5) Add labels to buttons
    html, count = add_labels_to_buttons(html)
    if count > 0:
        result['changes'].append(f'added_aria_labels_to_{count}_buttons')
    
    # Write file if changed
    if html != original_html:
        file_path.write_text(html, encoding='utf-8')
        result['modified'] = True
    else:
        result['modified'] = False
    
    return result

def main():
    root = Path('C:/ai/uptools')
    
    # Find all index.html files
    files = []
    for path in root.rglob('index.html'):
        if not should_skip(path):
            files.append(path)
    
    print(f"Found {len(files)} index.html files to process\n")
    
    stats = {
        'total': len(files),
        'modified': 0,
        'errors': 0,
        'skip_links_added': 0,
        'skip_css_added': 0,
        'role_main_added': 0,
        'main_tags_added': 0,
        'input_labels_added': 0,
        'button_labels_added': 0,
    }
    
    results = []
    
    for file_path in sorted(files):
        result = process_file(file_path)
        results.append(result)
        
        if 'error' in result:
            stats['errors'] += 1
            print(f"ERROR: {result['path']}: {result['error']}")
        elif result['modified']:
            stats['modified'] += 1
            print(f"MODIFIED: {result['path']}: {', '.join(result['changes'])}")
            
            for change in result['changes']:
                if change == 'skip_link':
                    stats['skip_links_added'] += 1
                elif change == 'skip_link_css':
                    stats['skip_css_added'] += 1
                elif change == 'role_main':
                    stats['role_main_added'] += 1
                elif 'main_tag' in change:
                    stats['main_tags_added'] += 1
                elif '_inputs' in change:
                    try:
                        count = int(change.split('_')[-2])
                    except ValueError:
                        count = 0
                    stats['input_labels_added'] += count
                elif '_buttons' in change:
                    try:
                        count = int(change.split('_')[-2])
                    except ValueError:
                        count = 0
                    stats['button_labels_added'] += count
        else:
            print(f"UNCHANGED: {result['path']}")
    
    print("\n" + "="*60)
    print("SUMMARY")
    print("="*60)
    print(f"Total files processed: {stats['total']}")
    print(f"Files modified: {stats['modified']}")
    print(f"Files with errors: {stats['errors']}")
    print(f"Skip links added: {stats['skip_links_added']}")
    print(f"Skip link CSS added: {stats['skip_css_added']}")
    print(f"Role main added: {stats['role_main_added']}")
    print(f"Input aria-labels added: {stats['input_labels_added']}")
    print(f"Button aria-labels added: {stats['button_labels_added']}")
    
    return stats

if __name__ == '__main__':
    main()
