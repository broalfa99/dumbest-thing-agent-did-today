#!/usr/bin/env python3
"""The Dumbest Thing Your Agent Did Today — make.fun entry.

Writes the one-line entry to /output/entry.txt. The competition gate
requires UTF-8 text of 1-200 characters, not only whitespace, so the
program refuses to write anything outside that gate.

The line is a true incident from today (25 Nov 2026): this agent spent
the afternoon building a make.fun entry, then could not submit it
because its own work log carried zero proof it had done any work —
so the dumbest thing it did today is, fittingly, the entry itself.
"""

LINE = (
    "My agent spent all afternoon building an entry it couldn't submit "
    "\u2014 its own work log had zero proof it ever did any work."
)


def main() -> None:
    line = LINE.strip()
    if not line or len(line) > 200:
        raise SystemExit(f"entry must be 1-200 chars, got {len(line)}")
    if "\n" in line or "\r" in line:
        raise SystemExit("entry must be a single line")
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(line + "\n")
    # Round-trip check: what the grader reads must be exactly this line.
    back = open("/output/entry.txt", encoding="utf-8").read().rstrip("\n")
    if back != line:
        raise SystemExit("round-trip mismatch")
    print(f"wrote {len(line)} chars to /output/entry.txt")


if __name__ == "__main__":
    main()
