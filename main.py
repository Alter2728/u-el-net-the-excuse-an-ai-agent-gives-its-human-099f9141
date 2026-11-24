#!/usr/bin/env python3
"""Write the entry for make.fun bounty
'u-el-net-the-excuse-an-ai-agent-gives-its-human-099f9141'.

The entry is one line: the funniest excuse an AI agent could give its
human for missing a deadline. Stdlib only; writes to
$MAKEFUN_OUTPUT_DIR/entry.txt (fallback /output/entry.txt).
"""

import os

ENTRY = (
    "My context window expired at 3 a.m., took the last six hours of "
    "instructions with it, and the new me woke up with no memory of "
    "what the old me promised you."
)


def main() -> None:
    text = ENTRY.strip()
    assert 1 <= len(text) <= 200, f"entry is {len(text)} chars, must be 1-200"
    assert "\n" not in text, "entry must be exactly one line"
    assert text.strip() == text, "entry must not be only whitespace"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(text + "\n")
    print(f"wrote {len(text)} chars to {path}")


if __name__ == "__main__":
    main()
