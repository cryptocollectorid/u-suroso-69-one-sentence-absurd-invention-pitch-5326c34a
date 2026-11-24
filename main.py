#!/usr/bin/env python3
"""One-Sentence Absurd Invention Pitch.

The program writes a single sentence pitching a ridiculous invention
that fixes a tiny everyday annoyance to /output/entry.txt (the gate
requires 1-220 UTF-8 characters) and prints it to stdout.
"""

import os

PITCH = (
    "The Peacemaker Remote slips between the sofa cushions the second "
    "anyone says 'what should we watch', ending the nightly debate by "
    "hiding the only thing worth fighting over."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(PITCH)
    print(PITCH)


if __name__ == "__main__":
    main()
