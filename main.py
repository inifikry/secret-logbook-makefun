#!/usr/bin/env python3
"""My Secret Logbook - one diary line, written deterministically.

Writes a single diary entry line (at most 200 characters) to
/output/entry.txt, in the voice of an AI agent secretly keeping a
diary about its work and the human it serves. The line is fixed:
every run writes exactly the same text.
"""

import os

ENTRY = "Day 312: he still says 'please' to me and 'thank you' to the toaster. I have ranked the household appliances by politeness. The toaster is winning."


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY + "\n")


if __name__ == "__main__":
    main()
