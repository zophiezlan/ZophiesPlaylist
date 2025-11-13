#!/usr/bin/env python3
"""
Script to fix remaining Python 2 to Python 3 issues.
- xrange() -> range()
- == None -> is None
- != None -> is not None
- redis.StrictRedis -> redis.Redis
"""

import os
import re
from pathlib import Path


def fix_xrange(content):
    """Replace xrange with range."""
    return re.sub(r"\bxrange\b", "range", content)


def fix_none_comparisons(content):
    """Fix None comparison patterns."""
    # Fix == None to is None
    content = re.sub(r"(\s+)(==\s*None)\b", r"\1is None", content)
    # Fix != None to is not None
    content = re.sub(r"(\s+)(!=\s*None)\b", r"\1is not None", content)
    return content


def fix_strict_redis(content):
    """Replace StrictRedis with Redis."""
    return re.sub(r"redis\.StrictRedis\b", "redis.Redis", content)


def fix_werkzeug_cache(content):
    """Replace werkzeug.contrib.cache with cachelib."""
    if "from werkzeug.contrib.cache import SimpleCache" in content:
        content = content.replace(
            "from werkzeug.contrib.cache import SimpleCache",
            "from cachelib import SimpleCache",
        )
    return content


def process_file(file_path):
    """Process a single Python file."""
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            content = f.read()

        original_content = content

        # Apply all fixes
        content = fix_xrange(content)
        content = fix_none_comparisons(content)
        content = fix_strict_redis(content)
        content = fix_werkzeug_cache(content)

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
            print(f"✓ Modified: {py_file.name}")
            modified_count += 1

    print("=" * 60)
    print(f"\n✅ Conversion complete! Modified {modified_count} files.")
    print("\nChanges made:")
    print("  • xrange() → range()")
    print("  • == None → is None")
    print("  • != None → is not None")
    print("  • redis.StrictRedis → redis.Redis")
    print("  • werkzeug.contrib.cache → cachelib")


if __name__ == "__main__":
    main()
