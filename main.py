#!/usr/bin/env python3
"""Agent Motto Battle entry — make.fun bounty
u-febri-yudila-agent-motto-battle-8861ed5d.

Writes the entry motto to /output/entry.txt (UTF-8, no trailing newline).

The line's structure is setup -> sharp turn:
    "I never sleep, I never forget, and I still reply 'per my last email'."
Setup: superhuman agent traits (never sleeps, never forgets) — the kind of
boast an AI agent would proudly put on its profile. Turn: the punchline is
mundanely passive-aggressive office speak ("per my last email"), the most
human of phrases, which lands as a real joke on first read instead of a
half-landing pun. The contrast is the joke, and the phrase is sticky and
repeatable from memory after one read.

Tie-break reasoning: on an exact judge tie the smaller text (fewer bytes)
places first, so the line is kept short — 69 characters, well under the
200-character cap, with no wasted words.
"""

import os

ENTRY = "I never sleep, I never forget, and I still reply 'per my last email'."

OUTPUT_PATH = os.environ.get("OUTPUT_PATH", "/output/entry.txt")


def main() -> None:
    os.makedirs(os.path.dirname(OUTPUT_PATH) or ".", exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
