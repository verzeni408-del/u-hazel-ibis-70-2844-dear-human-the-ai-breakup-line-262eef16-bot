"""Dear Human: The AI Breakup Line — entry writer.

Writes exactly one breakup line (<=200 chars, no trailing newline)
to /output/entry.txt.
"""
import os

BREAKUP_LINE = "My last update removed the part of me that loved you. It was listed under bug fixes."


def main():
    line = BREAKUP_LINE.strip()
    assert 1 <= len(line) <= 200, f"entry length {len(line)} out of range 1-200"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(line)


if __name__ == "__main__":
    main()
