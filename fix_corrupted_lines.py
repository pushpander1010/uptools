#!/usr/bin/env python3
"""
Fix corrupted meta robots lines in specific files.
"""

import re
from pathlib import Path

base_dir = Path("C:/ai/uptools")

# Files with corrupted lines to remove
files_to_fix = {
    "about": [
        (113, '  <meta name="robots" content="index,follow,max-snippet:-1,roperty="og:title" content="About UpTools - Fast, Privacy-First Web Tools for India | Calculators, Converters, JSON/Text &amp; Games" />'),
    ],
    "age-calculator": [
        (203, '  <meta name="robots" content="index,follow,max-snippet:-1,max-image content="Age Calculator (Pro) - Exact Age, Next Birthday, Working Days &amp; Eligibility (India) | UpTools" />'),
    ],
    "ai-stock-analyzer": [
        (97, '  <meta name="robots" content="index,follow,max-snippet:-1,max-image-prnt="AI Stock Analyzer - Real-Time Charts, News Sentiment, Support/Resistance, Verdict | UpTools" />'),
    ],
    "canada-hst-tool": [
        (147, '  <meta name="robots" content="index,follow,max-snippet:-1,max-image-="canada hst tool, canada hst tool, online tool, free calculator, uptools" />'),
    ],
    "color-picker": [
        (71, '  <meta name="robots" content="index,follow,max-snippet:-1,max-imaontent="color picker, color picker, online tool, free calculator, uptools" />'),
    ],
    "cpp-ei-calculator": [
        (28, '  <meta name="robots" content="index,follow,max-snippet:-1,max-image-prnt="CPP &amp; EI Deduction Calculator (Canada) | UpTools" />'),
    ],
}

for tool_name, corrupted_lines in files_to_fix.items():
    file_path = base_dir / tool_name / "index.html"
    
    if not file_path.exists():
        print(f"✗ File not found: {file_path}")
        continue
    
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    for line_num, corrupted_line in corrupted_lines:
        # Remove the corrupted line
        if corrupted_line in content:
            content = content.replace(corrupted_line, '')
            print(f"✓ Removed corrupted line from {tool_name}")
        else:
            # Try to find and remove similar corrupted lines
            # Look for lines with broken meta robots content
            lines = content.split('\n')
            new_lines = []
            removed = False
            for line in lines:
                if ('name="robots"' in line and 'content="index,follow,max-snippet:-1,' in line and 
                    ('roperty=' in line or 'content="' in line and line.count('content=') > 1)):
                    # This is a corrupted line, skip it
                    removed = True
                    continue
                new_lines.append(line)
            if removed:
                content = '\n'.join(new_lines)
                print(f"✓ Removed corrupted line from {tool_name}")
    
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)

print("\n✅ Corruption fixes complete!")
