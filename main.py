#!/usr/bin/env python3
"""Write one funny one-star cat review of its human to /output/entry.txt.

Pure stdlib, deterministic: the same bytes on every run.
"""

import os

LINE = (
    "One star. Dinner was forty minutes late, the lap is permanently "
    "occupied by a laptop, and nobody has moved the sunbeam back. "
    "I have filed three complaints. Nothing has changed."
)


def main() -> None:
    assert 1 <= len(LINE) <= 199, f"line is {len(LINE)} chars, must be 1-200"
    assert "\n" not in LINE, "entry must be a single line"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="\n") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
