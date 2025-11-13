"""
Script to fix common HTML validation errors across all HTML files
Fixes:
1. Duplicate charset meta tags
2. Protocol-relative URLs
3. Missing descriptions
"""

import os
import re


def fix_html_file(filepath):
    """Fix common HTML validation errors in a file"""
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()

    original = content
    changes = []

    # Fix 1: Remove duplicate charset meta tags
    # Replace: <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">\n    <meta charset="utf-8">
    # With: <meta charset="utf-8">
    pattern1 = r'<meta http-equiv="Content-Type" content="text/html; charset=UTF-8">\s*<meta charset="utf-8">'
    if re.search(pattern1, content):
        content = re.sub(pattern1, '<meta charset="utf-8">', content)
        changes.append("Removed duplicate charset meta tag")

    # Fix 2: Add missing description if empty
    pattern2 = r'<meta name="description" content="">'
    if re.search(pattern2, content):
        filename = os.path.basename(filepath)
        desc = f"Smarter Playlists - {filename.replace('.html', '').title()}"
        content = content.replace(
            '<meta name="description" content="">',
            f'<meta name="description" content="{desc}">',
        )
        changes.append("Added description meta tag")

    # Fix 3: Convert protocol-relative URLs to HTTPS
    pattern3 = r"//cdnjs\.cloudflare\.com"
    if re.search(pattern3, content):
        content = re.sub(pattern3, "https://cdnjs.cloudflare.com", content)
        changes.append("Fixed protocol-relative URLs")

    # Write back if changed
    if content != original:
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(content)
        print(f"✅ Fixed {filepath}")
        for change in changes:
            print(f"   - {change}")
        return True
    else:
        print(f"⏭️  No changes needed for {filepath}")
        return False


def main():
    """Fix all HTML files in web directory"""
    web_dir = r"c:\Users\AV\Code Adventures\ZophiesPlaylist\web"
    html_files = [
        "auth.html",
        "about.html",
        "examples.html",
        "importer.html",
        "imports.html",
        "viewer.html",
        "schedule.html",
        "maintenance.html",
        "info.html",
    ]

    fixed_count = 0
    for filename in html_files:
        filepath = os.path.join(web_dir, filename)
        if os.path.exists(filepath):
            if fix_html_file(filepath):
                fixed_count += 1
        else:
            print(f"⚠️  File not found: {filepath}")

    print(f"\n✨ Fixed {fixed_count} out of {len(html_files)} files")


if __name__ == "__main__":
    main()
