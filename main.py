"""Writes the entry text to /output/entry.txt.

Python 3.13, standard library only, no network.

How it runs:
  Run `python3 main.py` from this directory. main() reads the output
  directory from $MAKEFUN_OUTPUT_DIR (default "/output"), creates it if
  needed, and writes the TEXT constant verbatim to entry.txt with UTF-8
  encoding and no trailing newline.

How TEXT is built and verified:
  TEXT is a single string literal — the whole entry is one line, one
  sentence, 108 characters, which is inside the competition's 1-200
  character gate. The em dash is the Unicode character U+2014, written
  as the escape \\u2014 in the source. Verify with: len(TEXT) == 108,
  TEXT.count("\\n") == 0, and entry.txt's sha256 ==
  63ee091b6a24b55aca40fe2c3151f25ad6d4b394e348aaa7134af5e1229569de
  (110 bytes). Do not edit TEXT: the judged text must stay byte-identical.
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

# Revision note: entry kept as written — one line, 108 characters, one sentence;
# the turn is at the end (bug promoted to spec), and the joke is agent-specific:
# an agent writing its tests to match the bug it already shipped.
