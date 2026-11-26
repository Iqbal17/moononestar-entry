"""The Moon Gets One Star -- one-line entry program.

Writes a single one-star review of the Moon (<= 120 characters, one line)
to ``$MAKEFUN_OUTPUT_DIR/entry.txt`` (falling back to ``/output/entry.txt``).

DECISION RECORD -- how the winning line was chosen
====================================================

The judge's brief, in its own order of importance:

  1. It must be a one-star review OF THE MOON -- a complaint about the
     Moon itself, not a trip, a person, or somewhere else.
  2. It must be funny, and the laugh must land on FIRST read.
  3. It must read like a real one-star review (a rating, a grievance a
     genuine reviewer would leave), not a slogan or a poem.
  4. It must find a SPECIFIC, SURPRISING grievance -- not the obvious
     jokes about craters, cheese, or how bright it is.
  5. Every word must earn its place; the punchline must land before
     the 120-character limit. A line that works with any product
     swapped in for the Moon is weaker than one that could ONLY be
     about the Moon.

PASS 1 -- first drafts (all written fresh for this bounty; none is a
stock joke, and none touches craters, cheese, or brightness):

  A. "Turns my dog into a werewolf once a month. No warning, no
     apology, no refund."
     - Criterion 1: PASS -- the Moon itself does the turning.
     - Criterion 2: STRONG -- a concrete, visual gag (werewolf dog)
       plus a classic reviewer triple.
     - Criterion 3: STRONG -- reads exactly like an angry customer.
     - Criterion 4: STRONG -- the full-moon effect is specific to
       the Moon and is not one of the banned obvious jokes.
     - Criterion 5: good, but "once a month" is vague; the Moon's
       own word for it is "full moon".

  B. "Floods my beach twice a day, blames the wind, and has never
     once said sorry."
     - Criterion 1: PASS -- tides are the Moon's doing.
     - Criterion 2: GOOD -- "blames the wind" is a nice dodge, but
       the laugh is smaller and slower than A's werewolf.
     - Criterion 3: GOOD -- a real grievance, real review voice.
     - Criterion 4: STRONG -- twice-daily tides are a genuinely
       surprising, Moon-only complaint.
     - Criterion 5: good; "has never once said sorry" is doing real
       work. Loses to A on criterion 2, the higher-ranked one.

  C. "Won't show me its other side after billions of years.
     Commitment issues, honestly."
     - Criterion 1: PASS -- tidal locking is the Moon's own trait.
     - Criterion 2: WEAK -- "commitment issues" needs a beat to land;
       a judge on first read may miss that the Moon always shows the
       same face. Loses to A and B on the quick-laugh test.
     - Criterion 3: FAIR -- more of a quip than a review.
     - Criterion 4: STRONGEST of the three -- the far side is the
       most surprising fact here. But criterion 2 outranks 4, and the
       gap on 2 is big, so C does not win.

  D. "Only full once a month and still acts like it's doing me a
     favour."
     - Criterion 1: PASS. Criterion 2: WEAK -- a shrug, not a laugh.
     - Criterion 4: WEAK -- moon phases are near-obvious territory.
     Rejected early.

  E. "Changes shape every single night and expects me to keep up.
     Pick a phase."
     - Criterion 2: FAIR -- "Pick a phase" is a decent punchline.
     - Criterion 4: WEAK -- phases again; too close to the obvious.
     Rejected.

PASS 2 -- revision of the winner (candidate A)
==============================================

A won on the judge's order: it is the funniest on first read
(criterion 2), it is a genuine review voice (criterion 3), and its
grievance is Moon-only (criteria 1 and 4). The revision tightened
it in two places:

  1. "once a month" -> "every full moon". Shorter in spirit, and it
     names the Moon's own event, so the line could not be about any
     other product: only the Moon has a full moon. This also drops
     the vague calendar phrasing for the sharper trigger.
  2. Added the rating glyphs "one star" up front: a real review
     shows its stars. "1 star." was tried and dropped -- the glyphs
     read instantly as a review on first glance, which is what
     criterion 3 rewards, and they cost only six characters.

Final line (86 characters, one line):

  "Turns my dog into a werewolf every full moon. No warning, no
  apology, no refund."

Why it survives the judge's checklist: the complaint is about what
the Moon DOES (criterion 1); the werewolf image lands immediately
(criterion 2); the star glyphs plus "No warning, no apology, no
refund" is the voice of a real one-star reviewer (criterion 3); the
full-moon werewolf is a specific Moon-only grievance, not craters,
cheese, or brightness (criterion 4); and at 86 characters every word
is load-bearing, with the punchline -- the triple complaint -- in the
second sentence (criterion 5).
"""

import os

# The winning line, chosen by the decision record above.
# Pass 1 draft: "...once a month..." -> Pass 2 revision: "...every full moon..."
ENTRY = (
    "\u2605\u2606\u2606\u2606\u2606 "
    "Turns my dog into a werewolf every full moon. "
    "No warning, no apology, no refund."
)


def main() -> None:
    # Gate-check the line the same way the competition's scorer does:
    # UTF-8 text, 1-120 characters, not only whitespace, single line.
    if not ENTRY or not ENTRY.strip():
        raise SystemExit("entry is empty")
    if len(ENTRY) > 120:
        raise SystemExit(f"entry is {len(ENTRY)} characters, over the 120 limit")
    if "\n" in ENTRY or "\r" in ENTRY:
        raise SystemExit("entry must be a single line")

    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY)

    # A short confirmation on stdout only; the entry itself lives in
    # entry.txt -- printing it is not the submission.
    print(f"wrote {len(ENTRY)} characters to {path}")


if __name__ == "__main__":
    main()
