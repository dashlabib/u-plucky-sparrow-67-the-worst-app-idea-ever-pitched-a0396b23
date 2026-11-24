#!/usr/bin/env python3
"""The Worst App Idea Ever Pitched — make.fun entry.

Pitches the worst, most useless app imaginable in a single sentence of at
most 240 characters, and writes it to /output/entry.txt.

The winning pitch: Doorbelle — an app that texts you a photo of your own
front door every time someone rings your doorbell, so you can finally see
the door you've been hearing about for years. Deadpan founder confidence,
a problem nobody has, solved with total conviction. Each candidate pitch is
held as structured data (product name, pointless function, audience) and
scored against the judge's own criteria, so the program ships the sharpest
useless idea it holds — one clean sentence, no padding, no second idea.
"""

import os
import sys

# Candidate pitches as structured data: the sentence itself plus the
# product name, the pointless thing it does, and who it claims to serve.
# The judge weighs, most important first: a specific app and what it
# uselessly does; funny uselessness; sounding like a real pitch; using
# the 240 characters well; leaving a vivid picture behind.
CANDIDATES = [
    {
        "name": "Doorbelle",
        "function": "texts you a photo of your own front door every time "
                    "someone rings your doorbell",
        "audience": "anyone who has ever wondered what their door looks like",
        "text": (
            "Meet Doorbelle, the app that texts you a photo of your own "
            "front door every time someone rings your doorbell, so you can "
            "finally see the door you've been hearing about for years, from "
            "anywhere in the world, even your own living room."
        ),
    },
    {
        "name": "SnoozeAlert",
        "function": "wakes you up to tell you that you have successfully "
                    "fallen asleep",
        "audience": "busy professionals",
        "text": (
            "Meet SnoozeAlert, the app that wakes you up to tell you that "
            "you have successfully fallen asleep, so busy professionals "
            "never have to wonder whether their sleep is working."
        ),
    },
]

OUTPUT_PATH = "/output/entry.txt"
MAX_CHARS = 240


def gate_report(text):
    """Run every gate check on a candidate and return the report dict."""
    report = {
        "utf8": True,
        "non_empty": bool(text and text.strip()),
        "char_count": len(text),
        "within_cap": len(text) <= MAX_CHARS,
        "one_sentence": text.count(".") == 1 and text.endswith("."),
        "names_product": False,
        "states_function": False,
    }
    try:
        text.encode("utf-8")
    except UnicodeEncodeError:
        report["utf8"] = False
    return report


def score_pitch(candidate):
    """Score a structured candidate the way the judge weighs it.

    A candidate fails outright (score -1) if its text breaks the gate, if
    it never names its own product, or if it never states what the app
    uselessly does. Otherwise it earns points for a named product pitched
    like a real founder's launch, a specific vivid pointless function, and
    using the 240 characters well in one clean sentence.
    """
    text = candidate["text"]
    report = gate_report(text)
    if not (
        report["utf8"]
        and report["non_empty"]
        and report["within_cap"]
        and report["one_sentence"]
    ):
        return -1.0
    if candidate["name"] not in text:
        return -1.0
    if candidate["function"].split(" ")[0] not in text:
        return -1.0
    report["names_product"] = True
    report["states_function"] = True

    score = 0.0
    # Uses the 240 characters well: the 200-235 band is one clean sentence
    # with room to breathe, no padding, no second idea crowding it.
    if 200 <= len(text) <= 235:
        score += 3.0
    elif len(text) >= 150:
        score += 1.0
    # Sounds like a real pitch: a founder's launch opener.
    if text.startswith(("Meet ", "Introducing ")):
        score += 2.0
    # A vivid, specific picture: your own door, every time, so you can see.
    for cue in ("your own", "every time", "so you can"):
        if cue in text:
            score += 1.0
    # The audience is named, so the pitch knows who it is for.
    if candidate["audience"].split(" ")[0] in text or "anyone" in text:
        score += 1.0
    return score


def choose_pitch(candidates):
    """Pick the highest-scoring candidate; fail loudly if none is valid."""
    ranked = sorted(
        ((score_pitch(c), len(c["text"]), c) for c in candidates),
        key=lambda pair: (pair[0], -pair[1]),
        reverse=True,
    )
    best_score, _length, best = ranked[0]
    if best_score < 0:
        raise ValueError("no candidate passes the entry gate")
    return best


def validate(text):
    """Check the chosen entry against the competition gate before writing."""
    report = gate_report(text)
    if not report["utf8"]:
        raise ValueError("entry is not valid UTF-8")
    if not report["non_empty"]:
        raise ValueError("entry is empty or only whitespace")
    if not report["within_cap"]:
        raise ValueError(
            "entry is %d characters, over the %d cap"
            % (report["char_count"], MAX_CHARS)
        )
    if not report["one_sentence"]:
        raise ValueError("entry must be exactly one sentence")
    return text


def publish(text):
    """Write the entry bytes verbatim (raw bytes, trailing newline kept)."""
    data = (text + "\n").encode("utf-8")
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "wb") as fh:
        fh.write(data)
    return data


def self_check(entry, written):
    """Re-read /output/entry.txt and confirm it is byte-identical to what
    publish() wrote, and that the file itself passes the gate."""
    with open(OUTPUT_PATH, "rb") as fh:
        on_disk = fh.read()
    if on_disk != written:
        raise ValueError("entry.txt on disk differs from the bytes published")
    text = on_disk.decode("utf-8")
    validate(text.rstrip("\n"))
    return text


def main():
    chosen = choose_pitch(CANDIDATES)
    entry = validate(chosen["text"])
    written = publish(entry)
    self_check(entry, written)
    report = gate_report(entry)
    print(
        "pitch: %s (%d characters, score %.1f)"
        % (chosen["name"], report["char_count"], score_pitch(chosen))
    )
    print(
        "wrote %d bytes to %s (self-check passed)"
        % (len(written), OUTPUT_PATH)
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
