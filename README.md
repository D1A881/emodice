# 🎲 emodice

A collection of emoji dice games playable in your terminal. No dependencies — just Python 3.

## Requirements

- Python 3.6+
- A terminal that supports Unicode/emoji (most modern terminals do)

## Usage

```bash
python3 emodice.py
```

You'll be dropped into an interactive menu. Enter the number of the game you want to play, or `0` to quit.

## Games

| # | Name | Description |
|---|------|-------------|
| 1 | **Simple Roller** | Choose how many dice to roll (optionally with a skull face). Results and totals are displayed instantly. |
| 2 | **Highest Wins** | Two players take turns rolling. Whoever rolls the highest total wins the round. Great for settling disputes. |
| 3 | **Target Number** | Pick a target number and try to roll it exactly within 10 attempts. The closer you get, the more the tension builds. |
| 4 | **Skull Survival** | Dice include a ☠ skull face. Keep rolling to rack up points, but three skulls and it's game over. A push-your-luck classic. |
| 5 | **Doubles (Pairs)** | Roll 6 dice and score points for matching faces. Pairs, three-of-a-kinds, and beyond — all the way up to 100 points for six of a kind. |
| 6 | **Sequences** | Roll 6 dice and score for consecutive runs. A full ⚀⚁⚂⚃⚄⚅ sequence nets you a perfect 200 points. |
| 7 | **Beat the House** | Best-of-3 match against the computer. Roll 5 dice each round; highest total takes the point. First to 2 wins. |
| 8 | **Yahtzee** | Full 13-round Yahtzee with a live scorecard. Roll up to 3 times per turn, hold any dice between rolls, and strategically fill your categories to maximize your final score. Upper section bonus (+35) awarded for scoring 63 or more in ones through sixes. |

## Yahtzee Scoring Reference

**Upper Section** — score the sum of the matching faces (e.g., four 3s = 12 points):

| Category | Score |
|----------|-------|
| Ones through Sixes | Sum of that face value |
| **Upper Bonus** | +35 if upper total ≥ 63 |

**Lower Section:**

| Category | Score |
|----------|-------|
| Three of a Kind | Sum of all dice |
| Four of a Kind | Sum of all dice |
| Full House | 25 |
| Small Straight (4 in a row) | 30 |
| Large Straight (5 in a row) | 40 |
| YAHTZEE (5 of a kind) | 50 |
| Chance | Sum of all dice |

## Controls

- Most games are driven by **ENTER** to roll and numbered inputs to make choices.
- In Yahtzee, when prompted to keep dice enter the **position numbers** separated by spaces (e.g., `1 3 5`), type `all` to keep everything, or press ENTER to reroll all.
- Press **Ctrl+C** at any time to exit.

## Notes

- Up to 28 dice can be rolled at once in games that support a custom count.
- The skull face (☠) used in Game 4 scores 0 and counts toward your bust total.
- Yahtzee scores of 300+ are considered excellent; 250+ is great; 200+ is solid.

## License

MIT
