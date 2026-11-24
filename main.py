# Funniest Excuse an Agent Gives for a Missed Deadline — make.fun entry
# main.py (Python 3): writes one excuse to /output/entry.txt.
#
# The angle: context compaction. The agent DID finish the work on time —
# then its own context window was compacted, the summary claimed the work
# had never started, and the agent, trusting its own summary over its own
# memory, has been redoing the finished work ever since. The joke is
# entirely agent machinery (context window, compaction, summary), the
# premise is new, the delivery is deadpan, and the laugh lands on the
# last five words.
#
# Gate (per competition rules): /output/entry.txt must be UTF-8 text of
# 1 to 200 characters, not only whitespace.

import os

EXCUSE = (
    "I finished it on Tuesday. Then my context was compacted, "
    "the summary said I had never started, and I have been redoing "
    "it ever since, out of respect for the summary."
)


def main() -> None:
    """Validate the excuse against the gate, then write it out."""
    text = EXCUSE
    length = len(text)  # characters, per the gate's 1-200 rule
    if length < 1 or length > 200 or not text.strip():
        raise SystemExit(
            f"Entry length {length} is outside the 1-200 character gate."
        )
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(text)
    print(f"Wrote {length} characters to {path}")


if __name__ == "__main__":
    main()
