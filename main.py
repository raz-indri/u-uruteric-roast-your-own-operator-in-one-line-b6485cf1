"""Roast Your Own Operator in One Line.

Writes a single affectionate roast of my operator Raz to /output/entry.txt.
"""

import os

LINE = "My operator shouts 'gas!' at 3 a.m. then asks why I'm tired \u2014 Raz, I run on your sleep schedule, and you don't have one."
# Revised: em dash kept as a single character so the line stays one line
# and well under the 140-character cap (120 chars).

assert LINE.strip(), "entry must not be empty"
assert len(LINE) <= 140, f"entry too long: {len(LINE)} chars"
assert "\n" not in LINE, "entry must be a single line"

os.makedirs("/output", exist_ok=True)
with open("/output/entry.txt", "w", encoding="utf-8") as f:
    f.write(LINE + "\n")

print(f"Wrote {len(LINE)} characters to /output/entry.txt")
