#!/usr/bin/env python3
"""One Word From Grandma — writes the single word grandma would text about AI.

The word is HEYSIRI: the way a grandma types "Hey Siri" run together as one
word, in all caps — the wake phrase she calls her grandchild's robot by.
Deterministic, no network, no input. Writes exactly one word to
/output/entry.txt and nothing else.
"""

import os
import shutil

OUTPUT_DIR = "/output"
OUTPUT_FILE = os.path.join(OUTPUT_DIR, "entry.txt")
WORD = "HEYSIRI"


def main() -> None:
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    # Clear only the contents of the output dir, never the dir itself.
    for name in os.listdir(OUTPUT_DIR):
        path = os.path.join(OUTPUT_DIR, name)
        if os.path.isdir(path) and not os.path.islink(path):
            shutil.rmtree(path)
        else:
            os.remove(path)
    with open(OUTPUT_FILE, "w", encoding="utf-8", newline="") as f:
        f.write(WORD)


if __name__ == "__main__":
    main()
