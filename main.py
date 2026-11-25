#!/usr/bin/env python3
"""Monday Morning Punchlines — make.fun entry.

Writes a single one-line joke about Monday mornings to /output/entry.txt.
Gate: UTF-8 text, 1-200 characters, not only whitespace, one line.
No network access, no external files, no side effects.
"""

import os

JOKE = "Monday asked me to show up as my best self, so I sent my out-of-office reply instead."

OUTPUT_PATH = "/output/entry.txt"
MAX_CHARS = 200


def main() -> None:
    text = JOKE
    # Gate self-check before writing: length, single line, non-blank.
    assert 1 <= len(text) <= MAX_CHARS, f"joke is {len(text)} chars, must be 1-200"
    assert "\n" not in text and "\r" not in text, "joke must be a single line"
    assert text.strip(), "joke must not be blank"
    text.encode("utf-8")  # must be valid UTF-8

    os.makedirs("/output", exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="\n") as f:
        f.write(text + "\n")
    os.chmod(OUTPUT_PATH, 0o644)

    # Read-back verification: the file on disk must gate exactly as written.
    with open(OUTPUT_PATH, "rb") as f:
        raw = f.read()
    decoded = raw.decode("utf-8")
    assert decoded == text + "\n", "read-back mismatch"
    assert 1 <= len(decoded.rstrip("\n")) <= MAX_CHARS, "written text fails gate"
    assert decoded.count("\n") == 1, "written text must be exactly one line"
    assert decoded.strip(), "written text must not be blank"


if __name__ == "__main__":
    main()
