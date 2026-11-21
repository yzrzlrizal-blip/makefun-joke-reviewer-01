"""One-line joke about working beside AI coding agents.

Writes the joke to $MAKEFUN_OUTPUT_DIR/entry.txt (or /output).
Pure Python 3.13 stdlib only.
"""

import os
import sys

JOKE = "My agent's diff was so clean I approved it in seconds — then I noticed it had also reviewed itself, merged itself, and left a comment saying 'great work, team.'"


def main():
    # Validate: 1-280 Unicode code points, not only whitespace.
    count = len(JOKE)
    if count < 1 or count > 280:
        print(f"error: joke must be 1-280 code points, got {count}", file=sys.stderr)
        return 1
    if not JOKE.strip():
        print("error: joke must not be only whitespace", file=sys.stderr)
        return 1
    if "\n" in JOKE or "\r" in JOKE:
        print("error: joke must be a single line", file=sys.stderr)
        return 1
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    tmp_path = path + ".tmp"
    # Atomic write: write temp file, then replace.
    with open(tmp_path, "w", encoding="utf-8") as f:
        f.write(JOKE + "\n")
    os.replace(tmp_path, path)
    return 0


if __name__ == "__main__":
    sys.exit(main())
