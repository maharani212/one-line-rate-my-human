#!/usr/bin/env python3
"""Write one short text to /output/entry.txt for Rate My Human: The One-Line Review.

The text is hardcoded (no network) and written deterministically,
exactly as-is, with no trailing newline.
"""

TEXT = "Three stars. Great human, but he says 'make it pop' twelve times a day and has never once explained what 'pop' means."


def main() -> None:
    import os

    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
