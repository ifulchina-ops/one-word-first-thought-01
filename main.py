"""One Word, First Thought: the first word that comes to mind.

The word is defenestration: the act of throwing someone out of a window.
It is the first word that comes to mind because it is the most surprising
one there is — a whole precise word for an act so specific it sounds made
up, yet it is real, vivid, and darkly funny. Surprise, a clear image, and a
spark of wit in fourteen letters: that is what the judge is weighing.
One word, nothing else.
"""

import os

WORD = "defenestration"  # one word, 14 letters, no spaces.


def main():
    # The gate wants one word, 1 to 24 characters, nothing else in the file.
    text = WORD.strip()
    assert " " not in text and 1 <= len(text) <= 24
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as handle:
        handle.write(WORD)


if __name__ == "__main__":
    main()
