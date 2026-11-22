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
    # Enforce the competition's gate in-program: 1-280 Unicode code
    # points, not only whitespace. Fail loudly instead of writing an
    # entry the gate would refuse.
    if not 1 <= len(TEXT) <= 280 or not TEXT.strip():
        raise ValueError("entry text violates the 1-280 character gate")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(TEXT)
    # Read back and confirm the file holds exactly the intended bytes.
    with open("/output/entry.txt", encoding="utf-8") as f:
        if f.read() != TEXT:
            raise ValueError("entry.txt does not match the intended text")


if __name__ == "__main__":
    main()
