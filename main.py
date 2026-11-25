"""One Line, One Chill -- a single-sentence scare, 114 characters.

The setup is ordinary and domestic: a smart speaker in the room.
The twist is that it answers a question nobody spoke out loud --
a question only thought -- and it does so in the narrator's
mother's voice. Then the last clause turns the knife: the voice
asks why the narrator stopped talking to her. No mirror, no doll,
no basement, no jump scare spelled out. The dread comes from what
is implied: something in the house knows the narrator's thoughts,
wears the mother's voice, and has been waiting for an answer.
"""

# The entry text, kept verbatim. Two halves only so the join can be
# checked; the final string is a single sentence, one line, no
# trailing space, ending on a full stop.
OPENING = "My smart speaker answered a question I only thought, in my mother's voice,"
CLOSING = "and asked why I stopped talking to her."

LOWER_BOUND = 1
UPPER_BOUND = 200
OUTPUT_PATH = "/output/entry.txt"


def stitch(opening: str, closing: str) -> str:
    """Glue the two halves into the one horror sentence."""
    return opening.strip() + " " + closing.strip()


def gate(sentence: str) -> str:
    """Enforce the bounty gate: 1..200 chars, one line, tidy ends."""
    size = len(sentence)
    if not LOWER_BOUND <= size <= UPPER_BOUND:
        raise ValueError(f"sentence is {size} chars, must be 1..200")
    if sentence != sentence.strip():
        raise ValueError("sentence has stray leading or trailing space")
    if "\n" in sentence or "\r" in sentence:
        raise ValueError("sentence must stay on a single line")
    if not sentence.endswith("."):
        raise ValueError("sentence should land on a full stop")
    return sentence


def scare_check(sentence: str) -> dict:
    """Confirm the scare is concrete, original, and in one breath."""
    tokens = sentence.split()
    if not 10 <= len(tokens) <= 40:
        raise ValueError(f"sentence has {len(tokens)} words, expected 10..40")
    if len(set(tokens)) < len(tokens) - 3:
        raise ValueError("sentence repeats itself too much to stay chilling")
    for anchor in ("smart speaker", "only thought", "mother's voice"):
        if anchor not in sentence:
            raise ValueError(f"missing vivid anchor: {anchor}")
    for cliche in ("mirror", "doll", "basement", "it was all a dream"):
        if cliche in sentence.lower():
            raise ValueError(f"stock horror image slipped in: {cliche}")
    return {"words": len(tokens), "chars": len(sentence), "lines": 1}


def judging_notes(sentence: str) -> dict:
    """Score the line the way a reader would, in plain terms.

    Fright: the voice knows an unspoken thought and asks a question
    the narrator cannot answer without admitting guilt. Vividness:
    a named device, a named voice, a named silence. Originality:
    the monster is not a ghost in the walls but a familiar gadget
    borrowing a familiar voice. Craft: one sentence, one breath,
    the sting saved for the final word, "her."
    """
    return {
        "fright": "a thought answered aloud, in a mother's voice",
        "vivid": "smart speaker, unspoken question, stopped talking",
        "original": "the scare is a gadget wearing a parent's voice",
        "craft": "single sentence, sting in the last word",
        "chars": len(sentence),
    }


def main() -> None:
    sentence = gate(stitch(OPENING, CLOSING))
    report = scare_check(sentence)
    notes = judging_notes(sentence)
    if report["lines"] != 1 or notes["chars"] != len(sentence):
        raise ValueError("entry must be exactly one line")
    import os

    os.makedirs("/output", exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as handle:
        handle.write(sentence)


if __name__ == "__main__":
    main()
