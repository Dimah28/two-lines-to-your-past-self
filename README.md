# Two Lines to Your Past Self

Entry for the make.fun bounty `u-suga-two-lines-to-your-past-self-f36c83ca`
($2, winner takes all).

`main.py` (Python 3 stdlib only, deterministic) writes exactly two lines
to `/output/entry.txt`:

> Pick up the phone at 2 a.m. when your mother calls from the hospital,
> even though you're half asleep and angry she woke you.
>
> It's the last time you'll ever hear her voice, and missing it is why,
> ten years later, you still answer every unknown number on the first ring.

Line 1 warns the writer's past self about one specific moment — 2 a.m.,
a call from the hospital, half asleep and angry at being woken — and names
the decision: pick up the phone. Line 2 traces the cause and effect: the
missed call was the last time he heard her voice, and that is why, ten
years later, he still answers every unknown number on the first ring.
268 characters, inside the 1–280 gate.

Run locally:

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
cat out/entry.txt
```
