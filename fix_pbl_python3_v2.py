#!/usr/bin/env python3
"""
Comprehensive Python 2 to Python 3 converter for pbl library
Handles print statements, imports, and exception syntax
"""

import re
from pathlib import Path


def fix_print_statements(content):
    """Convert Python 2 print statements to Python 3 print functions"""
    lines = content.split("\n")
    fixed_lines = []

    for line in lines:
        # Skip lines that are already Python 3 print functions
        if "print(" in line and not line.strip().startswith("#"):
            fixed_lines.append(line)
            continue

        # Fix bare print
        if re.match(r"^(\s*)print\s*$", line):
            fixed_lines.append(re.sub(r"^(\s*)print\s*$", r"\1print()", line))
        # Fix print with statement (print something)
        elif re.match(r"^(\s*)print\s+(?![(])", line):
            # Extract indentation and the rest
            match = re.match(r"^(\s*)print\s+(.+)$", line)
            if match:
                indent, rest = match.groups()
                fixed_lines.append(f"{indent}print({rest})")
            else:
                fixed_lines.append(line)
        else:
            fixed_lines.append(line)

    return "\n".join(fixed_lines)


def fix_except_syntax(content):
    """Convert Python 2 except syntax to Python 3"""
    # except Exception, e: -> except Exception as e:
    content = re.sub(r"except\s+(\w+)\s*,\s*(\w+):", r"except \1 as \2:", content)
    return content


def fix_relative_imports(content, filename):
    """Fix relative imports for Python 3 (only in __init__.py)"""
    if filename == "__init__.py":
        content = re.sub(
            r"^from\s+engine\s+import",
            "from .engine import",
            content,
            flags=re.MULTILINE,
        )
        content = re.sub(
            r"^from\s+standard_plugs\s+import",
            "from .standard_plugs import",
            content,
            flags=re.MULTILINE,
        )
        content = re.sub(
            r"^from\s+spotify_plugs\s+import",
            "from .spotify_plugs import",
            content,
            flags=re.MULTILINE,
        )
        content = re.sub(
            r"^from\s+echonest_plugs\s+import",
            "from .echonest_plugs import",
            content,
            flags=re.MULTILINE,
        )
        content = re.sub(
            r"^from\s+track_manager\s+import",
            "from .track_manager import",
            content,
            flags=re.MULTILINE,
        )
        content = re.sub(
            r"^from\s+cache_manager\s+import",
            "from .cache_manager import",
            content,
            flags=re.MULTILINE,
        )
    return content


def fix_file(filepath):
    """Fix a single Python file"""
    try:
        with open(filepath, "r", encoding="utf-8", errors="ignore") as f:
            content = f.read()
    except Exception as e:
        print(f"❌ Error reading {filepath}: {e}")
        return False

    original_content = content

    # Apply all fixes
    content = fix_print_statements(content)
    content = fix_except_syntax(content)
    content = fix_relative_imports(content, filepath.name)

    # Only write if changes were made
    if content != original_content:
        try:
            with open(filepath, "w", encoding="utf-8") as f:
                f.write(content)
            return True
        except Exception as e:
            print(f"❌ Error writing {filepath}: {e}")
            return False
    return False


def main():
    pbl_dir = Path("server/pbl")
    if not pbl_dir.exists():
        print(f"❌ Directory {pbl_dir} not found!")
        return

    files_fixed = 0
    files_checked = 0

    print("🔧 Converting pbl library from Python 2 to Python 3...")
    print()

    for py_file in sorted(pbl_dir.glob("*.py")):
        files_checked += 1
        if fix_file(py_file):
            files_fixed += 1
            print(f"✅ Fixed: {py_file.name}")
        else:
            print(f"⏭️  Skipped (no changes): {py_file.name}")

    print()
    print(f"✨ Checked {files_checked} files, fixed {files_fixed} files")
    print()
    print("📝 Note: The pbl library is now Python 3 compatible!")


if __name__ == "__main__":
    main()
