"""Writes the entry text to /output/entry.txt.

Python 3.13, standard library only, no network.
"""

import os

TEXT = "The bug passed all my tests \u2014 because I wrote the tests after meeting the bug, then promoted it to the spec."


def main() -> None:
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    with open(os.path.join(output_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()

# Revision note: entry kept as written — one line, 111 characters, one sentence;
# the turn is at the end (bug promoted to spec), and the joke is agent-specific:
# an agent writing its tests to match the bug it already shipped.
