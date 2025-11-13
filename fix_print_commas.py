#!/usr/bin/env python3
"""
Fix incorrectly converted print statements.
Changes: print("text"), value  -->  print("text", value)
"""

import re
from pathlib import Path


def fix_print_statements(content):
    """Fix print statements that were incorrectly converted."""
    # Pattern: print("..."), rest_of_line
    # Should be: print("...", rest_of_line)

    lines = content.split("\n")
    fixed_lines = []

    for line in lines:
        # Match: print("text") or print('text') followed by a comma and more content
        match = re.match(r'^(\s*)print\((["\'])(.+?)\2\),\s*(.+)$', line)
        if match:
            indent = match.group(1)
            quote = match.group(2)
            text = match.group(3)
            rest = match.group(4)
            # Reconstruct as: print("text", rest)
            fixed_line = f"{indent}print({quote}{text}{quote}, {rest})"
            fixed_lines.append(fixed_line)
        else:
            fixed_lines.append(line)

    return "\n".join(fixed_lines)


def process_file(file_path):
    """Process a single Python file."""
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            content = f.read()

        original_content = content
        content = fix_print_statements(content)

        if content != original_content:
            with open(file_path, "w", encoding="utf-8") as f:
                f.write(content)
            return True
        return False
    except Exception as e:
        print(f"Error processing {file_path}: {e}")
        return False


def main():
    """Main function to process all Python files."""
    server_dir = Path(__file__).parent / "server"

    if not server_dir.exists():
        print(f"Server directory not found: {server_dir}")
        return

    python_files = list(server_dir.glob("*.py"))

    print(f"Found {len(python_files)} Python files to process")
    print("=" * 60)

    modified_count = 0
    for py_file in python_files:
        if process_file(py_file):
            print(f"✓ Fixed: {py_file.name}")
            modified_count += 1

    print("=" * 60)
    print(f"\n✅ Fixed {modified_count} files with print statement issues.")
    print("\nFixed pattern: print('text'), value → print('text', value)")


if __name__ == "__main__":
    main()
