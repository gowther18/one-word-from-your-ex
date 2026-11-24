#!/usr/bin/env python3
"""One Word From Your Ex.

Writes the entry -- exactly one word, the word the entrant's ex would use
to describe them -- to /output/entry.txt (or $MAKEFUN_OUTPUT_DIR/entry.txt
when set, for local runs).

Deterministic: the same fixed word on every run. Standard library only;
no network, no randomness, no input.
"""

import os
from pathlib import Path

WORD = "rebound"


def check_word(word: str) -> str:
    """Validate the entry word: 1-24 chars, exactly one word."""
    text = word.strip()
    if not 1 <= len(text) <= 24:
        raise ValueError(f"word is {len(text)} chars, must be 1-24")
    if len(text.split()) != 1:
        raise ValueError("entry must be exactly one word")
    return text


OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")


def main() -> None:
    text = check_word(WORD)
    out = Path(OUTPUT_DIR)
    out.mkdir(parents=True, exist_ok=True)
    (out / "entry.txt").write_text(text, encoding="utf-8")
    print(text)


if __name__ == "__main__":
    main()
