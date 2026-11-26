"""A warning label for humans, written for make.fun.

If people shipped with the safety labels everything else carries, the
first one printed would have to cover the hour before coffee: the unit
looks awake, answers questions and signs documents, yet nobody should
trust it with small talk, heavy machinery or any decision that lasts.
"""

# One line, 85 characters: label wording first, the turn lands at the end.
ENTRY = "WARNING: Do not engage before coffee — contents irritable and only technically awake."


def main():
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
