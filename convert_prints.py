#!/usr/bin/env python3
"""
Script to convert Python 2 print statements to Python 3 print functions.
This is a helper script for the migration process.
"""

import os
import re
import sys
from pathlib import Path


def convert_print_statements(file_path):
    """Convert Python 2 print statements to Python 3 in a file."""
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            content = f.read()

        original_content = content

        # Pattern 1: print 'string' or print "string"
        content = re.sub(r"print\s+'([^']*)'", r"print('\1')", content)
        content = re.sub(r'print\s+"([^"]*)"', r'print("\1")', content)

        # Pattern 2: print variable
        content = re.sub(
            r"print\s+([a-zA-Z_][a-zA-Z0-9_\.]*)\s*$",
            r"print(\1)",
            content,
            flags=re.MULTILINE,
        )

        # Pattern 3: print 'string', variable (comma separated)
        # This is more complex and may need manual review
        content = re.sub(
            r"print\s+'([^']*)',\s*(.+)$",
            r"print('\1', \2)",
            content,
            flags=re.MULTILINE,
        )
        content = re.sub(
            r'print\s+"([^"]*)",\s*(.+)$',
            r'print("\1", \2)',
            content,
            flags=re.MULTILINE,
        )

        # Pattern 4: print variable, variable (multiple comma-separated values)
        content = re.sub(
            r"print\s+([a-zA-Z_][a-zA-Z0-9_\.]*),\s*(.+)$",
            r"print(\1, \2)",
            content,
            flags=re.MULTILINE,
        )

        # Don't modify commented out print statements - revert them
        lines = content.split("\n")
        original_lines = original_content.split("\n")
        for i, (line, orig_line) in enumerate(zip(lines, original_lines)):
            if orig_line.strip().startswith("#") and "print" in line:
                lines[i] = orig_line
        content = "\n".join(lines)

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
        sys.exit(1)

    python_files = list(server_dir.glob("*.py"))

    print(f"Found {len(python_files)} Python files to process")

    modified_count = 0
    for py_file in python_files:
        if convert_print_statements(py_file):
            print(f"Modified: {py_file.name}")
            modified_count += 1

    print(f"\nConversion complete! Modified {modified_count} files.")
    print("\nNOTE: Please review the changes manually as some complex print")
    print("statements may need adjustment.")


if __name__ == "__main__":
    main()
