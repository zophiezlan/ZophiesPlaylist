#!/usr/bin/env python3
"""
Complete Python 2 to 3 conversion for pbl library
Handles: print statements, xrange, relative imports, except syntax, print-to-file
"""

import re
from pathlib import Path


def fix_all_python2_issues(content, filename):
    """Apply all Python 2 to 3 fixes"""
    lines = content.split("\n")
    fixed_lines = []

    for line in lines:
        # Fix relative imports (only in __init__.py)
        if filename == "__init__.py":
            line = re.sub(
                r"^from\s+(engine|standard_plugs|spotify_plugs|echonest_plugs|track_manager|cache_manager)\s+import",
                r"from .\1 import",
                line,
            )

        # Fix relative imports in other files
        if filename in [
            "standard_plugs.py",
            "spotify_plugs.py",
            "echonest_plugs.py",
            "test.py",
            "engine.py",
        ]:
            line = re.sub(
                r"^from\s+(engine|track_manager|standard_plugs|spotify_plugs|frog)\s+import",
                r"from .\1 import",
                line,
            )
            line = re.sub(
                r"^import\s+(engine|standard_plugs|track_manager)$",
                r"from . import \1",
                line,
            )

        # Fix xrange to range
        line = re.sub(r"\bxrange\(", "range(", line)

        # Fix except syntax: except Exception, e: -> except Exception as e:
        line = re.sub(r"except\s+(\w+)\s*,\s*(\w+):", r"except \1 as \2:", line)

        # Fix print >> file syntax
        if "print(" in line and ">>" in line:
            # print(>> f, ...) -> print(..., file=f)
            match = re.search(r"print\(>>\s*(\w+),\s*(.+)\)", line)
            if match:
                file_var, content_expr = match.groups()
                line = re.sub(
                    r"print\(>>\s*\w+,\s*.+\)",
                    f"print({content_expr}, file={file_var})",
                    line,
                )

        # Fix bare print and print statements (not already print())
        if (
            "print" in line
            and "print(" not in line
            and not line.strip().startswith("#")
        ):
            # Bare print
            if re.match(r"^(\s*)print\s*$", line):
                line = re.sub(r"^(\s*)print\s*$", r"\1print()", line)
            # print something
            elif re.match(r"^(\s*)print\s+(?![=(])", line):
                match = re.match(r"^(\s*)print\s+(.+)$", line)
                if match:
                    indent, rest = match.groups()
                    line = f"{indent}print({rest})"

        fixed_lines.append(line)

    return "\n".join(fixed_lines)


def main():
    pbl_dir = Path("server/pbl")
    if not pbl_dir.exists():
        print(f"❌ Directory {pbl_dir} not found!")
        return

    files_fixed = 0
    print("🔧 Converting pbl library from Python 2 to Python 3...")
    print()

    for py_file in sorted(pbl_dir.glob("*.py")):
        try:
            with open(py_file, "r", encoding="utf-8", errors="ignore") as f:
                content = f.read()

            fixed_content = fix_all_python2_issues(content, py_file.name)

            if fixed_content != content:
                with open(py_file, "w", encoding="utf-8") as f:
                    f.write(fixed_content)
                files_fixed += 1
                print(f"✅ Fixed: {py_file.name}")
        except Exception as e:
            print(f"❌ Error processing {py_file.name}: {e}")

    print()
    print(f"✨ Fixed {files_fixed} files")
    print("🎉 pbl library is now Python 3 compatible!")


if __name__ == "__main__":
    main()
