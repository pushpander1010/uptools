#!/usr/bin/env python3
"""
Remove remaining corrupted/duplicate meta robots lines.
"""

import re
from pathlib import Path

base_dir = Path("C:/ai/uptools")

# Process all index.html files
for file_path in sorted(base_dir.glob("*/index.html")):
    tool_name = file_path.parent.name
    
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    original_content = content
    
    # Remove lines that contain corrupted robots content
    # These typically have patterns like: content="index,follow,max-snippet:-1,max-image-=" or similar
    lines = content.split('\n')
    new_lines = []
    
    for line in lines:
        # Skip corrupted lines with broken robots content
        if ('name="robots"' in line and 
            ('content="index,follow,max-snippet:-1,' in line or 'content="index,follow,max-snippet:-1,' in line) and
            line.count('content=') > 1):
            # This is a corrupted line with multiple content= attributes
            continue
        # Also skip lines that look like they were corrupted during previous edits
        if 'name="robots"' in line and ('-=' in line or '-prnt=' in line or '-="can' in line or '-="color' in line):
            continue
        new_lines.append(line)
    
    content = '\n'.join(new_lines)
    
    if content != original_content:
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"✓ Fixed {tool_name}")

# Now verify final state
print("\n=== Final verification ===")
issues = []

for file_path in sorted(base_dir.glob("*/index.html")):
    tool_name = file_path.parent.name
    
    if tool_name in ['assets', 'dist', 'node_modules', 'public', 'scripts', 'games']:
        continue
    
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Check for duplicate canonical
    canonical_count = len(re.findall(r'rel="canonical"', content))
    if canonical_count > 1:
        issues.append(f"{tool_name}: {canonical_count} canonical tags")
    
    # Check for duplicate robots
    robots_count = len(re.findall(r'name="robots"', content))
    if robots_count > 1:
        issues.append(f"{tool_name}: {robots_count} robots tags")
    
    # Check for broken robots tag
    if re.search(r'name="robots"\s+content="[^"]*"\s+name="keywords"', content):
        issues.append(f"{tool_name}: broken robots tag")

if issues:
    print("Remaining issues:")
    for issue in issues:
        print(f"  - {issue}")
else:
    print("✅ All issues fixed!")

print("\nDone!")
