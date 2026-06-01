#!/usr/bin/env python3
"""
Restore missing canonical tags for all affected files.
"""

import re
from pathlib import Path

base_dir = Path("C:/ai/uptools")

# Process all index.html files
for file_path in sorted(base_dir.glob("*/index.html")):
    tool_name = file_path.parent.name
    
    # Skip non-tool directories
    if tool_name in ['assets', 'dist', 'node_modules', 'public', 'scripts', 'games']:
        continue
    
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Check if canonical is missing
    if 'rel="canonical"' not in content:
        canonical_url = f"https://www.uptools.in/{tool_name}/"
        
        # Try to find theme-color tag (various formats)
        # Pattern 1: <meta name="theme-color" content="..." />
        # Pattern 2: <meta content="..." name="theme-color"/>
        # Pattern 3: <meta content="..." name="theme-color" />
        theme_patterns = [
            r'<meta\s+name="theme-color"\s+content="[^"]*"\s*/?>',
            r'<meta\s+content="[^"]*"\s+name="theme-color"\s*/?>',
        ]
        
        insert_pos = None
        for pattern in theme_patterns:
            theme_match = re.search(pattern, content)
            if theme_match:
                insert_pos = theme_match.end()
                break
        
        if insert_pos:
            canonical_tag = f'\n<link href="{canonical_url}" rel="canonical"/>'
            content = content[:insert_pos] + canonical_tag + content[insert_pos:]
            
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"✓ Added canonical tag for {tool_name}")
        else:
            # Try to find robots tag as insertion point
            robots_patterns = [
                r'<meta\s+name="robots"\s+content="[^"]*"\s*/?>',
                r'<meta\s+content="[^"]*"\s+name="robots"\s*/?>',
            ]
            
            for pattern in robots_patterns:
                robots_match = re.search(pattern, content)
                if robots_match:
                    insert_pos = robots_match.end()
                    canonical_tag = f'\n<link href="{canonical_url}" rel="canonical"/>'
                    content = content[:insert_pos] + canonical_tag + content[insert_pos:]
                    
                    with open(file_path, 'w', encoding='utf-8') as f:
                        f.write(content)
                    print(f"✓ Added canonical tag for {tool_name} (after robots)")
                    break
            else:
                print(f"✗ Could not find insertion point for {tool_name}")

print("\n✅ Canonical tag restoration complete!")
