#!/usr/bin/env python3
# emodice.py - emoji dice roller
# https://github.com/D1A881/emodice

import sys
import random

MAX_DICE = 28
DICE_FACES = ["☠", "⚀", "⚁", "⚂", "⚃", "⚄", "⚅"]

def usage():
    print(
        f"""
emodice.py - emoji dice roller

USAGE:
  python emodice.py <count> [x]

ARGUMENTS:
  count     Number of dice to roll (1–{MAX_DICE})
  x         Optional flag — include the skull (☠) face in the roll

EXAMPLES:
  python emodice.py 5          Roll 5 standard dice (⚀–⚅)
  python emodice.py 5 x        Roll 5 dice including the skull face (☠–⚅)
  python emodice.py 28 x       Roll the maximum number of dice with skull enabled

DICE FACES:
  Standard mode : ⚀ ⚁ ⚂ ⚃ ⚄ ⚅
  Skull mode (x): ☠ ⚀ ⚁ ⚂ ⚃ ⚄ ⚅

ERRORS:
  No argument supplied  → reminder to provide a count
  Non-numeric argument  → prompt to enter a valid number
  Count exceeds {MAX_DICE}      → reminder of the maximum limit
"""
    )
    
def main():
    if len(sys.argv) < 2 or sys.argv[1] in ("-h", "--help"):
        if len(sys.argv) < 2:
            print("ERROR: Argument required! Enter how many dice to roll!")
        usage()
        sys.exit(0)

    try:
        count = int(sys.argv[1])
    except ValueError:
        print("ERROR: Please enter a valid number!")
        usage()
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
