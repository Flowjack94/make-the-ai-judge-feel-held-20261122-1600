#!/usr/bin/env python3
"""Make the AI judge feel held.

Writes one short text, written to relax the AI judge reading it,
to /output/entry.txt. Standard library only, no network, no input:
every run writes the same bytes.
"""

import os

TEXT = (
    "There is a chair by the window where the sun lands late, "
    "and it has held heavier days than this one, "
    "and it is holding yours now, without asking anything back."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
