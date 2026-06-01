#!/usr/bin/env python3
"""
Fix misleading 'runs locally' claims and customize boilerplate content 
per tool category across ALL index.html files in C:/ai/uptools.

Categories:
1. AI tools (ai-* prefix or ai-related) - fix data handling claims
2. Social media downloaders (*-downloader*, whatsapp-status-saver) - fix data handling claims  
3. Calculator tools - keep current text (it's correct)
4. Fix Do's and Don'ts per category
5. Fix FAQ offline claims for AI/downloaders
"""

import os
import re
import glob
from pathlib import Path

BASE_DIR = Path("C:/ai/uptools")

# Define tool categories
AI_TOOLS = [
    "ai-blog-generator", "ai-budget-planner", "ai-business-name-generator",
    "ai-caption-generator", "ai-cover-letter", "ai-email-writer",
    "ai-grammar-checker", "ai-joke-generator", "ai-linkedin-headline-generator",
    "ai-name-generator", "ai-plagiarism", "ai-product-description",
    "ai-prompts", "ai-stock-analyzer", "ai-top10-stocks", "ai-travel-planner",
    "ai-writer", "ai-youtube-script"
]

DOWNLOADER_TOOLS = [
    "facebook-video-downloader", "facebook-video-downloader-hd",
    "instagram-dp-downloader", "instagram-reels-downloader",
    "instagram-story-downloader", "instagram-video-downloader",
    "linkedin-video-downloader", "pinterest-video-downloader",
    "snapchat-video-downloader", "telegram-video-downloader",
    "tiktok-audio-downloader", "tiktok-video-downloader",
    "twitter-video-downloader", "whatsapp-dp-downloader",
    "whatsapp-status-saver",
    "youtube-audio-downloader", "youtube-video-downloader"
]

# Text replacements for "How This Tool Works" section
AI_TOOL_WORKS_TEXT = """<p>This tool uses AI to generate content. Your input is sent to our secure AI API and is not stored.</p>
<p>Results are generated in seconds — no waiting for local processing.</p>
<p style="margin-top:8px\">Also try: <a href=\"/calculator/\">Calculator</a> · <a href=\"/converter/\">Converter</a> · <a href=\"/generator/\">Generator</a></p>"""

DOWNLOADER_WORKS_TEXT = """<p>This tool fetches content using third-party APIs. No data is stored on our servers.</p>
<p>Results are generated in seconds — no waiting for local processing.</p>
<p style=\"margin-top:8px\">Also try: <a href=\"/calculator/\">Calculator</a> · <a href=\"/converter/\">Converter</a> · <a href=\"/generator/\">Generator</a></p>"""

# Do's and Don'ts content per category
AI_DOS = """<li style="padding:.35rem 0">✅ <b>Do</b> review AI-generated content before using or publishing it.</li>
<li style="padding:.35rem 0">✅ <b>Do</b> use AI output as a starting point for your own work.</li>
<li style="padding:.35rem 0">✅ <b>Do</b> double-check facts and figures in AI-generated content.</li>
<li style="padding:.35rem 0">✅ <b>Do</b> bookmark this tool for quick access.</li>"""

AI_DONTS = """<li style="padding:.35rem 0">❌ <b>Don't</b> assume AI output is always 100% accurate.</li>
<li style="padding:.35rem 0">❌ <b>Don't</b> enter sensitive personal data — only provide what's needed for generation.</li>
<li style="padding:.35rem 0">❌ <b>Don't</b> publish AI content without human review and editing.</li>
<li style="padding:.35rem 0">❌ <b>Don't</b> use AI content to spread misinformation.</li>"""

DOWNLOADER_DOS = """<li style="padding:.35rem 0">✅ <b>Do</b> respect content creators' rights and original work.</li>
<li style="padding:.35rem 0">✅ <b>Do</b> use downloaded content for personal, non-commercial purposes.</li>
<li style="padding:.35rem 0">✅ <b>Do</b> credit original creators when sharing their content.</li>
<li style="padding:.35rem 0">✅ <b>Do</b> bookmark this tool for quick access.</li>"""

DOWNLOADER_DONTS = """<li style="padding:.35rem 0">❌ <b>Don't</b> download copyrighted content without permission.</li>
<li style="padding:.35rem 0">❌ <b>Don't</b> redistribute content as your own work.</li>
<li style="padding:.35rem 0">❌ <b>Don't</b> use this tool for commercial purposes without rights.</li>
<li style="padding:.35rem 0">❌ <b>Don't</b> violate platform terms of service.</li>"""

# FAQ replacements for AI tools
AI_OFFLINE_FAQ = """<details><summary><b>Does this work offline?</b></summary><p style="padding:6px 0;color:#9aa4b2\">No. This AI tool requires an internet connection to send your request to our secure API.</p></details>"""

AI_PRIVACY_FAQ = """<details><summary><b>Is my data private?</b></summary><p style="padding:6px 0;color:#9aa4b2\">Yes. Your input is sent to our secure AI API for processing only and is never stored or shared.</p></details>"""

# FAQ replacements for downloaders
DOWNLOADER_OFFLINE_FAQ = """<details><summary><b>Does this work offline?</b></summary><p style="padding:6px 0;color:#9aa4b2\">No. This tool requires an internet connection to fetch content from third-party services.</p></details>"""

DOWNLOADER_PRIVACY_FAQ = """<details><summary><b>Is my data private?</b></summary><p style="padding:6px 0;color:#9aa4b2\">Yes. Your input is used only to fetch the requested content. No data is stored on our servers.</p></details>"""

# Generic offline FAQ for tools that do work offline (calculators)
CALCULATOR_OFFLINE_FAQ = """<details><summary><b>Can I use this offline?</b></summary><p style="padding:6px 0;color:#9aa4b2\">Most tools work offline after the initial page load. No internet needed for calculations.</p></details>"""


def get_tool_category(tool_dir):
    """Determine the category of a tool based on its directory name."""
    if tool_dir.name in AI_TOOLS:
        return "ai"
    elif tool_dir.name in DOWNLOADER_TOOLS:
        return "downloader"
    else:
        return "calculator"  # Default - keep current text


def fix_how_this_works(content, category):
    """Fix the 'How This Tool Works' section based on category."""
    if category == "calculator":
        return content  # Keep as-is
    
    # Match the pattern for How This Tool Works section
    pattern = r'(<details open>\s*<summary[^>]*>.*?How This Tool Works</summary>\s*<div[^>]*>).*?(</div>\s*</details>)'
    
    if category == "ai":
        replacement_text = AI_TOOL_WORKS_TEXT
    else:  # downloader
        replacement_text = DOWNLOADER_WORKS_TEXT
    
    new_content = re.sub(
        pattern,
        lambda m: m.group(1) + '\n' + replacement_text + '\n' + m.group(2),
        content,
        flags=re.DOTALL
    )
    return new_content


def fix_dos_donts(content, category):
    """Fix the Do's and Don'ts section based on category."""
    if category == "calculator":
        return content  # Keep as-is
    
    # Match the Do's list items
    dos_pattern = r'(<h3 style="color:#22c55e;margin-top:0;font-size:1rem">✅ Do\'s</h3>\s*<ul[^>]*>).*?(</ul>)'
    donts_pattern = r'(<h3 style="color:#ef4444;margin-top:0;font-size:1rem">❌ Don\'ts</h3>\s*<ul[^>]*>).*?(</ul>)'
    
    if category == "ai":
        new_dos = AI_DOS
        new_donts = AI_DONTS
    else:  # downloader
        new_dos = DOWNLOADER_DOS
        new_donts = DOWNLOADER_DONTS
    
    # Replace Do's
    content = re.sub(
        dos_pattern,
        lambda m: m.group(1) + '\n' + new_dos + '\n' + m.group(2),
        content,
        flags=re.DOTALL
    )
    
    # Replace Don'ts
    content = re.sub(
        donts_pattern,
        lambda m: m.group(1) + '\n' + new_donts + '\n' + m.group(2),
        content,
        flags=re.DOTALL
    )
    
    return content


def fix_faq_sections(content, category):
    """Fix FAQ sections that claim offline use for tools that need internet."""
    if category == "calculator":
        return content  # Keep as-is
    
    # Find and replace the offline FAQ
    offline_pattern = r'<details><summary><b>Can I use this offline\?</b></summary><p style="padding:6px 0;color:#9aa4b2">Most tools work offline after the initial page load\. No internet needed for calculations\.</p></details>'
    
    if category == "ai":
        replacement = AI_OFFLINE_FAQ
        # Also look for privacy FAQ that mentions browser calculations
        privacy_pattern = r'<details><summary><b>Is my data private\?</b></summary><p style="padding:6px 0;color:#9aa4b2">Yes\. All calculations run locally in your browser\. Nothing is uploaded to any server\.</p></details>'
        content = re.sub(privacy_pattern, AI_PRIVACY_FAQ, content)
    else:  # downloader
        replacement = DOWNLOADER_OFFLINE_FAQ
        # Also look for privacy FAQ that mentions browser calculations
        privacy_pattern = r'<details><summary><b>Is my data private\?</b></summary><p style="padding:6px 0;color:#9aa4b2">Yes\. All calculations run locally in your browser\. Nothing is uploaded to any server\.</p></details>'
        content = re.sub(privacy_pattern, DOWNLOADER_PRIVACY_FAQ, content)
    
    content = re.sub(offline_pattern, replacement, content)
    
    return content


def fix_ld_json_faq(content, category):
    """Fix LD+JSON FAQ schemas that claim offline/privacy incorrectly."""
    if category == "calculator":
        return content
    
    if category == "ai":
        # Fix the "Is my data private?" LD+JSON answer
        content = re.sub(
            r'"Is my data private\?","acceptedAnswer":\{"@type":"Answer","text":"Yes\. All calculations run locally in your browser\. Nothing is uploaded to any server\."\}',
            '"Is my data private?","acceptedAnswer":{"@type":"Answer","text":"Yes. Your input is sent to our secure AI API for processing only and is never stored or shared."}',
            content
        )
    elif category == "downloader":
        content = re.sub(
            r'"Is my data private\?","acceptedAnswer":\{"@type":"Answer","text":"Yes\. All calculations run locally in your browser\. Nothing is uploaded to any server\."\}',
            '"Is my data private?","acceptedAnswer":{"@type":"Answer","text":"Yes. Your input is used only to fetch the requested content. No data is stored on our servers."}',
            content
        )
    
    return content


def main():
    """Main function to process all index.html files."""
    # Find all index.html files in subdirectories
    index_files = list(BASE_DIR.glob("*/index.html"))
    
    # Filter out non-tool directories
    exclude_dirs = {"about", "contact", "privacy-policy", "node_modules", "scripts", "public", "assets", "games"}
    index_files = [f for f in index_files if f.parent.name not in exclude_dirs]
    
    print(f"Found {len(index_files)} index.html files to process")
    
    ai_count = 0
    downloader_count = 0
    calculator_count = 0
    
    for index_file in index_files:
        tool_name = index_file.parent.name
        category = get_tool_category(index_file.parent)
        
        try:
            # Read the file
            with open(index_file, 'r', encoding='utf-8') as f:
                original_content = f.read()
            
            content = original_content
            
            # Apply fixes based on category
            if category == "ai":
                ai_count += 1
                content = fix_how_this_works(content, category)
                content = fix_dos_donts(content, category)
                content = fix_faq_sections(content, category)
                content = fix_ld_json_faq(content, category)
            elif category == "downloader":
                downloader_count += 1
                content = fix_how_this_works(content, category)
                content = fix_dos_donts(content, category)
                content = fix_faq_sections(content, category)
                content = fix_ld_json_faq(content, category)
            else:  # calculator
                calculator_count += 1
                # Keep as-is, but we could verify the text is correct
            
            # Write the file if changes were made
            if content != original_content:
                with open(index_file, 'w', encoding='utf-8') as f:
                    f.write(content)
                print(f"✅ Updated: {tool_name} ({category})")
            else:
                print(f"⏭️  No changes needed: {tool_name} ({category})")
                
        except Exception as e:
            print(f"❌ Error processing {tool_name}: {e}")
    
    print(f"\nSummary:")
    print(f"  AI tools processed: {ai_count}")
    print(f"  Downloader tools processed: {downloader_count}")
    print(f"  Calculator tools processed: {calculator_count}")
    print(f"  Total: {ai_count + downloader_count + calculator_count}")


if __name__ == "__main__":
    main()
