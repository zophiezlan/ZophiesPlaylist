#!/usr/bin/env python3
"""
Fix Python 2 to Python 3 issues in the pbl library
"""

import os
import re
from pathlib import Path


def fix_print_statements(content):
    """Convert Python 2 print statements to Python 3 print functions"""
    # Pattern for print statement without parentheses
    patterns = [
        (r"\bprint\s+([^(\n][^\n]*)", r"print(\1)"),  # print something
        (r"print\s*$", r"print()"),  # bare print
    ]

    for pattern, replacement in patterns:
        content = re.sub(pattern, replacement, content)

    return content


def fix_relative_imports(content):
    """Fix relative imports for Python 3"""
    # Already handled in __init__.py manually
    return content


def fix_file(filepath):
    """Fix a single Python file"""
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()

    original_content = content

    # Apply fixes
    content = fix_print_statements(content)

    # Only write if changes were made
    if content != original_content:
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(content)
        return True
    return False


def main():
    pbl_dir = Path("server/pbl")
    if not pbl_dir.exists():
        print(f"❌ Directory {pbl_dir} not found!")
        return

    files_fixed = 0
    files_checked = 0

    for py_file in pbl_dir.glob("*.py"):
        files_checked += 1
        if fix_file(py_file):
            files_fixed += 1
            print(f"✅ Fixed: {py_file.name}")

    print(f"\n✨ Checked {files_checked} files, fixed {files_fixed} files")


if __name__ == "__main__":
    main()
