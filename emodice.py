#!/usr/bin/env python3
# emodice.py - emoji dice roller

import sys
import random

MAX_DICE = 28
DICE_FACES = ["☠", "⚀", "⚁", "⚂", "⚃", "⚄", "⚅"]

def main():
    if len(sys.argv) < 2:
        print("ERROR: Argument required! Enter how many dice to roll!")
        sys.exit(0)

    try:
        count = int(sys.argv[1])
    except ValueError:
        print("ERROR: Please enter a valid number!")
        sys.exit(0)

    if count > MAX_DICE:
        print(f"ERROR: Enter how many dice to roll!\n{count} entered! ({MAX_DICE} max)")
        sys.exit(0)

    if len(sys.argv) != 3 or sys.argv[2] != "x":
            DICE_FACES.pop(0)

    result = "".join(random.choice(DICE_FACES) for _ in range(count))
    print(result)

if __name__ == "__main__":
    main()
