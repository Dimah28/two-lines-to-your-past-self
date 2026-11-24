#!/usr/bin/env python3
"""Two Lines to Your Past Self (make.fun bounty u-suga-two-lines-to-your-past-self-f36c83ca).

Writes exactly two lines to /output/entry.txt: a warning to the writer's
past self about one specific moment, and one sentence on why it mattered.

v1 draft (revised below -- see v2):
  Line 1 warns about a single concrete moment -- 2 a.m., a phone call
  from the hospital, half asleep and angry at being woken -- and names
  the decision: pick up the phone.
  Line 2 traces the cause and effect: missing that call meant missing
  her voice for the last time, and that is why he still flinches at
  every phone ringing at night.

v2 (final) -- one real revision, driven by the judge's criterion 3
(clear cause and effect): line 2's ending was a vague feeling
("flinch every time a phone rings at night"). It now names a concrete
changed behaviour with a time depth -- ten years later, he still
answers every unknown number on the first ring. A visible habit the
moment caused beats a feeling it caused, and "ten years later" makes
the cost land harder. Line 1 is unchanged: the moment was already
concrete (time, place, decision, state of mind).

Deterministic: the text is a fixed string, no randomness, no network,
no model calls. Both runs write the same bytes.

  mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
"""

import os
from pathlib import Path

ENTRY = (
    "Pick up the phone at 2 a.m. when your mother calls from the hospital, "
    "even though you're half asleep and angry she woke you.\n"
    "It's the last time you'll ever hear her voice, and missing it is why, "
    "ten years later, you still answer every unknown number on the first ring."
)

OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")


def validate(entry: str) -> None:
    """Enforce the competition's gate before writing: UTF-8 text of
    1-280 characters, not only white space, exactly two lines, each a
    single sentence. Fail loudly instead of writing an entry the gate
    would refuse."""
    if not 1 <= len(entry) <= 280:
        raise SystemExit(f"entry is {len(entry)} characters, must be 1-280")
    if not any(not ch.isspace() for ch in entry):
        raise SystemExit("entry must contain a non-whitespace character")
    lines = entry.split("\n")
    if len(lines) != 2:
        raise SystemExit(f"entry must be exactly two lines, got {len(lines)}")
    for i, line in enumerate(lines, 1):
        if not line.strip():
            raise SystemExit(f"line {i} is empty")
        # "2 a.m." holds periods that are not sentence ends.
        countable = line.replace("a.m.", "").replace("p.m.", "")
        if countable.count(".") != 1 or not line.rstrip().endswith("."):
            raise SystemExit(f"line {i} must be exactly one sentence: {line!r}")


def main() -> None:
    validate(ENTRY)
    output_path = Path(OUTPUT_DIR) / "entry.txt"
    output_path.parent.mkdir(parents=True, exist_ok=True)
    # Write exactly the two lines: no trailing newline, the judge reads
    # exactly the bytes in the file.
    output_path.write_text(ENTRY, encoding="utf-8")
    # Read-back verification: the file on disk must contain exactly the
    # entry, byte for byte. Fail loudly instead of shipping a bad entry.
    written = output_path.read_text(encoding="utf-8")
    if written != ENTRY:
        raise SystemExit(f"read-back mismatch: wrote {ENTRY!r}, file has {written!r}")


if __name__ == "__main__":
    main()
