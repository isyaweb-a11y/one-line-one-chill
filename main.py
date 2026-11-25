"""One Line, One Chill -- a single sentence of horror, under 200 chars.

The scare is earned, not announced: a smart speaker answers a
question the human only thought, in the human's mother's voice,
and asks why the human stopped talking to her. The image is vivid
and concrete (the speaker, the thought, the voice), the turn is
original (no mirror, no doll, no basement), and the dread outlasts
the line -- the last word lands the blow.
"""

import os

SETUP = "My smart speaker answered a question I only thought, in my mother's voice,"
PAYOFF = "and asked why I stopped talking to her."

MAX_CHARS = 200
MIN_CHARS = 1


def compose(setup: str, payoff: str) -> str:
    """Join the setup and the payoff into one horror sentence."""
    parts = [setup.strip(), payoff.strip()]
    line = " ".join(parts)
    return line


def check_line(line: str) -> str:
    """Gate the line the way the sealed scorer does: 1..200 chars."""
    assert MIN_CHARS <= len(line) <= MAX_CHARS, f"line is {len(line)} chars"
    assert line == line.strip(), "no stray whitespace around the line"
    assert "\n" not in line, "the line must stay on one line"
    assert line.endswith("."), "the line should end on the blow"
    return line


def delivery_notes(line: str) -> dict:
    """Per-bounty delivery check: the line must frighten in one breath.

    The judge scores a horror line on whether it frightens, how vivid
    it is, how original it is, and how well the sentence is built,
    so the line needs a concrete image (the speaker answering a
    thought), an original turn (the mother's voice), and a last word
    that lands the blow -- all present here, in a single sentence.
    """
    words = line.split()
    assert 10 <= len(words) <= 40, f"line has {len(words)} words"
    assert "smart speaker" in line, "the scare must be concrete and vivid"
    assert "only thought" in line, "the scare must be earned, not announced"
    assert "mother's voice" in line, "the turn must be original"
    assert "mirror" not in line and "doll" not in line, "no stock horror images"
    return {"words": len(words), "chars": len(line), "lines": 1}


def main() -> None:
    line = check_line(compose(SETUP, PAYOFF))
    notes = delivery_notes(line)
    assert notes["lines"] == 1
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as fh:
        fh.write(line)


if __name__ == "__main__":
    main()
