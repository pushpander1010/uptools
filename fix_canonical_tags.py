#!/usr/bin/env python3
"""
Fix missing canonical tags that were accidentally removed.
"""

from pathlib import Path

# Files that need canonical tags restored
files_to_fix = {
    "ai-prompts": "https://www.uptools.in/ai-prompts/",
    "ai-stock-analyzer": "https://www.uptools.in/ai-stock-analyzer/",
    # Check for other files that might be missing canonical
}

base_dir = Path("C:/ai/uptools")

for tool_name, canonical_url in files_to_fix.items():
    file_path = base_dir / tool_name / "index.html"
    
    if not file_path.exists():
        print(f"✗ File not found: {file_path}")
        continue
    
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Check if canonical is missing
    if 'rel="canonical"' not in content:
        # Find the right place to insert (after theme-color or after keywords)
        import re
        
        # Try to insert after theme-color
        theme_color_match = re.search(r'<meta\s+content="[^"]*"\s+name="theme-color"\s*/?>', content)
        if not theme_color_match:
            theme_color_match = re.search(r'<meta\s+name="theme-color"\s+content="[^"]*"\s*/?>', content)
        
        if theme_color_match:
            insert_pos = theme_color_match.end()
            canonical_tag = f'\n<link href="{canonical_url}" rel="canonical"/>'
            content = content[:insert_pos] + canonical_tag + content[insert_pos:]
            
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"✓ Restored canonical tag for {tool_name}")
        else:
            print(f"✗ Could not find insertion point for {tool_name}")
    else:
        print(f"  {tool_name} already has canonical tag")

# Also search for any other files that might be missing canonical
print("\nChecking all files for missing canonical tags...")
import re

for file_path in sorted(base_dir.glob("*/index.html")):
    tool_name = file_path.parent.name
    
    # Skip non-tool directories
    if tool_name in ['assets', 'dist', 'node_modules', 'public', 'scripts']:
        continue
    
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    if 'rel="canonical"' not in content:
        # Find theme-color to determine the URL pattern
        theme_match = re.search(r'<meta\s+[^>]*name="theme-color"[^>]*/>', content)
        if not theme_match:
            theme_match = re.search(r'<meta\s+name="theme-color"\s+content="[^"]*"\s*/>', content)
        
        if theme_match:
            canonical_url = f"https://www.uptools.in/{tool_name}/"
            insert_pos = theme_match.end()
            canonical_tag = f'\n<link href="{canonical_url}" rel="canonical"/>'
            content = content[:insert_pos] + canonical_tag + content[insert_pos:]
            
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"✓ Added canonical tag for {tool_name}")
        else:
            print(f"✗ Could not find insertion point for {tool_name}")

print("\n✅ Canonical tag restoration complete!")
