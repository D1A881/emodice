# 🎲 emodice

A tiny command-line emoji dice roller written in Python.

---

## Requirements

- Python 3.6+
- A terminal with Unicode/emoji support

---

## Usage

```bash
python emodice.py <count> [x]
```

| Argument | Required | Description |
|----------|----------|-------------|
| `count`  | Yes      | Number of dice to roll (1–28) |
| `x`      | No       | Enable the skull face (☠) in the roll |

---

## Examples

```bash
# Roll 5 standard dice
python emodice.py 5
# ⚃⚁⚅⚂⚄

# Roll 5 dice with the skull face enabled
python emodice.py 5 x
# ☠⚄⚁☠⚂

# Show help / usage
python emodice.py --help
```

---

## Dice Faces

| Mode | Faces |
|------|-------|
| Standard | ⚀ ⚁ ⚂ ⚃ ⚄ ⚅ |
| Skull (`x`) | ☠ ⚀ ⚁ ⚂ ⚃ ⚄ ⚅ |

In standard mode the skull face is excluded, giving a clean d6 roll. Pass `x` as a second argument to add it back in — handy for games where a skull result has a special meaning.

---

## Limits

The maximum number of dice per roll is **28**. Requesting more than this will print an error and exit.

---

## Error Messages

| Situation | Message |
|-----------|---------|
| No argument given | `ERROR: Argument required! Enter how many dice to roll!` |
| Non-numeric argument | `ERROR: Please enter a valid number!` |
| Count exceeds 28 | `ERROR: Enter how many dice to roll! N entered! (28 max)` |

---

## License

Do whatever you want with it. 🎲
