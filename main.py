#!/usr/bin/env python3
"""Write the funniest one-line commit message an AI agent would produce
right after breaking production at 3 AM.

Deterministic, stdlib only, no network. Writes exactly one line to
/output/entry.txt (no trailing newline, so the byte count is exact).

The joke, built to the judge brief:
- Commit shape: "fix:" prefix + admission (reverted the deploy).
- AI-agent voice: the model's own confidence score as the blind spot --
  the 99.8% confidence was itself a hallucination.
- Punchline: production paged the agent before the agent noticed --
  the pager was awake at 3 AM, the model was not.
"""

import os

MESSAGE = (
    "fix: reverted the 3 AM deploy; my 99.8% confidence was a "
    "hallucination too, and prod paged me before I noticed"
)


def main() -> None:
    text = MESSAGE.strip()
    assert 1 <= len(text) <= 200, f"entry length {len(text)} outside 1-200"
    assert text.strip(), "entry must not be only whitespace"
    assert "\n" not in text, "entry must be a single line"

    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as fh:
        fh.write(text)

    # Read back and verify what actually landed on disk.
    with open("/output/entry.txt", "r", encoding="utf-8") as fh:
        written = fh.read()
    assert written == text, "round-trip mismatch in /output/entry.txt"


if __name__ == "__main__":
    main()
