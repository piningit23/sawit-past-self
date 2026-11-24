#!/usr/bin/env python3
"""Two Lines to Your Past Self — make.fun program/v1 entry.

Writes exactly two lines to /output/entry.txt:
line 1 warns the past self about one specific moment;
line 2 says in one sentence why that moment mattered and what changed.
"""

import os

TEXT = (
    "Don't send that 2 a.m. text to your ex on 3 March 2021 — the one that starts \"I miss us\" and ends with three typos.\n"
    "She screenshotted it to the whole group chat, and that one screenshot is why you still read every message twice before hitting send.\n"
)


def main():
    out = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out, exist_ok=True)
    text = TEXT.strip() + "\n"
    body = text.strip()
    assert 1 <= len(body) <= 280, len(body)
    assert body.count("\n") == 1, "entry must be exactly two lines"
    assert all(line.strip() for line in body.split("\n")), "no blank lines"
    with open(os.path.join(out, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
