#!/usr/bin/env python3
"""Fortune Cookie Funnies for Engineers — make.fun entry.

Writes one fortune cookie message for a software engineer to
/output/entry.txt. Standard library only. The fortune is a plain
string constant below — nothing is fetched, read, or generated.
"""

import os

FORTUNE = "Your code will pass review today \u2014 by someone who has never read it and never will."


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(FORTUNE)


if __name__ == "__main__":
    main()
