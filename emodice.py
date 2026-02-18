#!/usr/bin/env python3
"""
emodice.py - Emoji Dice Games Collection
https://github.com/D1A881/emodice
"""

import sys
import random
import time

MAX_DICE = 28
DICE_FACES_STANDARD = ["⚀", "⚁", "⚂", "⚃", "⚄", "⚅"]
DICE_FACES_SKULL = ["☠", "⚀", "⚁", "⚂", "⚃", "⚄", "⚅"]

def clear_screen():
    """Clear the console screen"""
    print("\n" * 50)

def roll_dice(count, include_skull=False):
    """Roll dice and return results"""
    faces = DICE_FACES_SKULL if include_skull else DICE_FACES_STANDARD
    return [random.choice(faces) for _ in range(count)]

def display_dice(dice, message=""):
    """Display dice with optional message"""
    if message:
        print(f"\n{message}")
    print("  " + " ".join(dice))
    print()

def dice_value(die):
    """Convert die face to numeric value (skull = 0)"""
    if die == "☠":
        return 0
    return DICE_FACES_STANDARD.index(die) + 1

def sum_dice(dice):
    """Sum the numeric values of dice"""
    return sum(dice_value(d) for d in dice)

def press_enter():
    """Wait for user to press enter"""
    input("\nPress ENTER to continue...")

# ============================================================
# GAME 1: SIMPLE ROLLER
# ============================================================
def game_simple_roller():
    """Simple dice roller - just roll and display"""
    clear_screen()
    print("=" * 60)
    print("GAME 1: SIMPLE DICE ROLLER")
    print("=" * 60)
    
    try:
        count = int(input(f"\nHow many dice to roll (1-{MAX_DICE})? "))
        if count < 1 or count > MAX_DICE:
            print(f"ERROR: Must be between 1 and {MAX_DICE}")
            press_enter()
            return
    except ValueError:
        print("ERROR: Please enter a valid number!")
        press_enter()
        return
    
    skull = input("Include skull face? (y/n): ").lower() == 'y'
    
    print("\n🎲 Rolling...")
    time.sleep(0.5)
    
    dice = roll_dice(count, skull)
    display_dice(dice, "Result:")
    
    total = sum_dice(dice)
    print(f"Total: {total}")
    
    press_enter()

# ============================================================
# GAME 8: YAHTZEE
# ============================================================
def game_yahtzee():
    """Full Yahtzee game with scorecard"""
    clear_screen()
    print("=" * 60)
    print("GAME 8: YAHTZEE")
    print("=" * 60)
    print("\nClassic Yahtzee! 13 rounds, 3 rolls per turn.")
    print("Fill your scorecard to maximize your score!\n")
    
    # Initialize scorecard
    scorecard = {
        # Upper section
        'ones': None,
        'twos': None,
        'threes': None,
        'fours': None,
        'fives': None,
        'sixes': None,
        # Lower section
        'three_kind': None,
        'four_kind': None,
        'full_house': None,
        'small_straight': None,
        'large_straight': None,
        'yahtzee': None,
        'chance': None,
    }
    
    category_names = {
        'ones': 'Ones',
        'twos': 'Twos',
        'threes': 'Threes',
        'fours': 'Fours',
        'fives': 'Fives',
        'sixes': 'Sixes',
        'three_kind': 'Three of a Kind',
        'four_kind': 'Four of a Kind',
        'full_house': 'Full House',
        'small_straight': 'Small Straight',
        'large_straight': 'Large Straight',
        'yahtzee': 'YAHTZEE!',
        'chance': 'Chance',
    }
    
    def show_scorecard():
        """Display the current scorecard"""
        print("\n" + "=" * 60)
        print("SCORECARD")
        print("=" * 60)
        print("\nUPPER SECTION:")
        for i, cat in enumerate(['ones', 'twos', 'threes', 'fours', 'fives', 'sixes'], 1):
            score = scorecard[cat]
            display = f"{score:3d}" if score is not None else " - "
            print(f"  {i}. {category_names[cat]:20s} {display}")
        
        upper_total = sum(s for s in [scorecard[c] for c in ['ones', 'twos', 'threes', 'fours', 'fives', 'sixes']] if s is not None)
        upper_bonus = 35 if upper_total >= 63 else 0
        print(f"\n     Upper Total: {upper_total}")
        if upper_total >= 63:
            print(f"     Bonus (63+): +{upper_bonus}")
        
        print("\nLOWER SECTION:")
        for i, cat in enumerate(['three_kind', 'four_kind', 'full_house', 'small_straight', 'large_straight', 'yahtzee', 'chance'], 7):
            score = scorecard[cat]
            display = f"{score:3d}" if score is not None else " - "
            print(f"  {i}. {category_names[cat]:20s} {display}")
        
        lower_total = sum(s for s in [scorecard[c] for c in ['three_kind', 'four_kind', 'full_house', 'small_straight', 'large_straight', 'yahtzee', 'chance']] if s is not None)
        
        print(f"\n     Lower Total: {lower_total}")
        grand_total = upper_total + upper_bonus + lower_total
        print(f"     GRAND TOTAL: {grand_total}")
        print("=" * 60)
    
    def count_values(dice):
        """Count occurrences of each die value"""
        counts = {}
        for die in dice:
            val = dice_value(die)
            counts[val] = counts.get(val, 0) + 1
        return counts
    
    def calculate_score(dice, category):
        """Calculate score for a category"""
        values = [dice_value(d) for d in dice]
        counts = count_values(dice)
        
        # Upper section
        if category in ['ones', 'twos', 'threes', 'fours', 'fives', 'sixes']:
            target = ['ones', 'twos', 'threes', 'fours', 'fives', 'sixes'].index(category) + 1
            return values.count(target) * target
        
        # Three/Four of a kind
        if category == 'three_kind':
            if any(c >= 3 for c in counts.values()):
                return sum(values)
            return 0
        
        if category == 'four_kind':
            if any(c >= 4 for c in counts.values()):
                return sum(values)
            return 0
        
        # Full house (3 of one, 2 of another)
        if category == 'full_house':
            counts_list = sorted(counts.values())
            if counts_list == [2, 3]:
                return 25
            return 0
        
        # Small straight (4 in a row)
        if category == 'small_straight':
            unique = sorted(set(values))
            for i in range(len(unique) - 3):
                if unique[i:i+4] == list(range(unique[i], unique[i]+4)):
                    return 30
            return 0
        
        # Large straight (5 in a row)
        if category == 'large_straight':
            unique = sorted(set(values))
            if unique == [1, 2, 3, 4, 5] or unique == [2, 3, 4, 5, 6]:
                return 40
            return 0
        
        # Yahtzee (5 of a kind)
        if category == 'yahtzee':
            if any(c == 5 for c in counts.values()):
                return 50
            return 0
        
        # Chance (sum of all dice)
        if category == 'chance':
            return sum(values)
        
        return 0
    
    def show_available_scores(dice):
        """Show what you could score in each category"""
        print("\nAVAILABLE CATEGORIES:")
        available = []
        for cat, score in scorecard.items():
            if score is None:
                potential = calculate_score(dice, cat)
                cat_num = list(scorecard.keys()).index(cat) + 1
                print(f"  {cat_num}. {category_names[cat]:20s} = {potential:3d} points")
                available.append(cat_num)
        return available
    
    # Main game loop - 13 rounds
    for round_num in range(1, 14):
        print("\n" + "=" * 60)
        print(f"ROUND {round_num}/13")
        print("=" * 60)
        
        show_scorecard()
        
        # Roll phase
        dice = roll_dice(5)
        kept_dice = []
        
        for roll_num in range(1, 4):
            print(f"\n--- Roll {roll_num}/3 ---")
            
            if kept_dice:
                print(f"Kept: {' '.join(kept_dice)}")
            
            display_dice(dice, "Current roll:")
            
            if roll_num < 3:
                keep = input("\nKeep dice? (e.g., '1 3 5' or 'all' or press ENTER to reroll all): ").strip().lower()
                
                if keep == 'all':
                    kept_dice = dice[:]
                    break
                elif keep:
                    try:
                        indices = [int(x) - 1 for x in keep.split()]
                        kept_dice = [dice[i] for i in indices if 0 <= i < len(dice)]
                        # Reroll unkept dice
                        num_reroll = 5 - len(kept_dice)
                        if num_reroll > 0:
                            new_dice = roll_dice(num_reroll)
                            dice = kept_dice + new_dice
                            kept_dice = []
                        else:
                            dice = kept_dice
                            break
                    except (ValueError, IndexError):
                        print("Invalid input, rerolling all")
                        dice = roll_dice(5)
                else:
                    dice = roll_dice(5)
            else:
                # Final roll
                break
        
        # Scoring phase
        print("\n" + "=" * 60)
        display_dice(dice, "FINAL DICE:")
        
        available = show_available_scores(dice)
        
        while True:
            try:
                choice = int(input("\nChoose category to score (1-13): "))
                if choice in available:
                    cat_key = list(scorecard.keys())[choice - 1]
                    score = calculate_score(dice, cat_key)
                    scorecard[cat_key] = score
                    print(f"\n✓ Scored {score} points in {category_names[cat_key]}")
                    break
                else:
                    print("Invalid or already used category!")
            except (ValueError, IndexError):
                print("Please enter a number 1-13")
        
        if round_num < 13:
            input("\nPress ENTER for next round...")
    
    # Final score
    clear_screen()
    print("\n" + "=" * 60)
    print("GAME OVER!")
    print("=" * 60)
    show_scorecard()
    
    upper_total = sum(s for s in [scorecard[c] for c in ['ones', 'twos', 'threes', 'fours', 'fives', 'sixes']] if s is not None)
    upper_bonus = 35 if upper_total >= 63 else 0
    lower_total = sum(s for s in [scorecard[c] for c in ['three_kind', 'four_kind', 'full_house', 'small_straight', 'large_straight', 'yahtzee', 'chance']] if s is not None)
    grand_total = upper_total + upper_bonus + lower_total
    
    print(f"\n🏆 FINAL SCORE: {grand_total} points")
    
    if grand_total >= 300:
        print("🌟 EXCELLENT! You're a Yahtzee master!")
    elif grand_total >= 250:
        print("👏 GREAT JOB! Very solid game!")
    elif grand_total >= 200:
        print("👍 GOOD GAME! Nice work!")
    else:
        print("🎲 Keep practicing - you'll improve!")
    
    press_enter()

# ============================================================
# GAME 2: HIGHEST WINS
# ============================================================
def game_highest_wins():
    """Two players roll - highest total wins"""
    clear_screen()
    print("=" * 60)
    print("GAME 2: HIGHEST WINS")
    print("=" * 60)
    print("\nTwo players each roll dice. Highest total wins!")
    
    try:
        count = int(input(f"\nDice per player (1-{MAX_DICE//2})? "))
        if count < 1 or count > MAX_DICE//2:
            print(f"ERROR: Must be between 1 and {MAX_DICE//2}")
            press_enter()
            return
    except ValueError:
        print("ERROR: Please enter a valid number!")
        press_enter()
        return
    
    # Player 1
    input("\nPlayer 1 - Press ENTER to roll...")
    p1_dice = roll_dice(count)
    display_dice(p1_dice, "Player 1:")
    p1_total = sum_dice(p1_dice)
    print(f"Player 1 Total: {p1_total}")
    
    input("\nPlayer 2 - Press ENTER to roll...")
    p2_dice = roll_dice(count)
    display_dice(p2_dice, "Player 2:")
    p2_total = sum_dice(p2_dice)
    print(f"Player 2 Total: {p2_total}")
    
    print("\n" + "=" * 60)
    if p1_total > p2_total:
        print(f"🏆 PLAYER 1 WINS! ({p1_total} vs {p2_total})")
    elif p2_total > p1_total:
        print(f"🏆 PLAYER 2 WINS! ({p2_total} vs {p1_total})")
    else:
        print(f"🤝 TIE GAME! (Both scored {p1_total})")
    print("=" * 60)
    
    press_enter()

# ============================================================
# GAME 3: TARGET NUMBER
# ============================================================
def game_target_number():
    """Try to roll exactly a target number"""
    clear_screen()
    print("=" * 60)
    print("GAME 3: TARGET NUMBER")
    print("=" * 60)
    print("\nTry to roll exactly the target number!")
    
    try:
        count = int(input(f"\nHow many dice (1-{MAX_DICE})? "))
        if count < 1 or count > MAX_DICE:
            print(f"ERROR: Must be between 1 and {MAX_DICE}")
            press_enter()
            return
            
        target = int(input(f"Target number ({count}-{count*6})? "))
        if target < count or target > count * 6:
            print(f"ERROR: Target must be between {count} and {count*6}")
            press_enter()
            return
    except ValueError:
        print("ERROR: Please enter a valid number!")
        press_enter()
        return
    
    attempts = 0
    max_attempts = 10
    
    print(f"\nTarget: {target}")
    print(f"You have {max_attempts} attempts!\n")
    
    for attempt in range(1, max_attempts + 1):
        input(f"Attempt {attempt}/{max_attempts} - Press ENTER to roll...")
        
        dice = roll_dice(count)
        display_dice(dice)
        total = sum_dice(dice)
        
        diff = abs(total - target)
        print(f"Total: {total} (off by {diff})")
        
        if total == target:
            print(f"\n🎯 BULLSEYE! You hit {target} in {attempt} attempt(s)!")
            break
        elif diff <= 2:
            print("🔥 So close!")
    else:
        print(f"\n💔 Out of attempts! Target was {target}")
    
    press_enter()

# ============================================================
# GAME 4: SKULL SURVIVAL
# ============================================================
def game_skull_survival():
    """Roll with skulls - three skulls and you lose!"""
    clear_screen()
    print("=" * 60)
    print("GAME 4: SKULL SURVIVAL")
    print("=" * 60)
    print("\nRoll dice with skulls (☠). Three skulls = GAME OVER!")
    print("Try to get the highest score before busting!")
    
    dice_count = 5
    score = 0
    skulls = 0
    round_num = 1
    
    print(f"\nStarting with {dice_count} dice")
    
    while skulls < 3:
        print(f"\n--- Round {round_num} ---")
        print(f"Score: {score} | Skulls: {'☠' * skulls}")
        
        choice = input("Roll dice? (y/n or 'quit'): ").lower()
        if choice in ('n', 'no', 'quit', 'q'):
            print(f"\n✋ Stopped with score: {score}")
            break
        
        dice = roll_dice(dice_count, include_skull=True)
        display_dice(dice)
        
        round_skulls = dice.count("☠")
        round_score = sum_dice(dice)
        
        skulls += round_skulls
        score += round_score
        
        if round_skulls > 0:
            print(f"⚠️  {round_skulls} skull(s) this round!")
        
        if skulls >= 3:
            print(f"\n💀 THREE SKULLS! GAME OVER!")
            print(f"Final Score: {score}")
            break
        
        print(f"Round score: +{round_score}")
        round_num += 1
    
    press_enter()

# ============================================================
# GAME 5: DOUBLES
# ============================================================
def game_doubles():
    """Roll pairs - score points for matching dice"""
    clear_screen()
    print("=" * 60)
    print("GAME 5: DOUBLES (PAIRS)")
    print("=" * 60)
    print("\nRoll 6 dice. Score points for pairs!")
    print("  • Pair (2 matching) = 2 points")
    print("  • Three of a kind = 10 points")
    print("  • Four of a kind = 25 points")
    print("  • Five of a kind = 50 points")
    print("  • Six of a kind = 100 points")
    
    input("\nPress ENTER to roll 6 dice...")
    
    dice = roll_dice(6)
    display_dice(dice, "Your roll:")
    
    # Count occurrences
    counts = {}
    for die in dice:
        value = dice_value(die)
        counts[value] = counts.get(value, 0) + 1
    
    score = 0
    matches = []
    
    for value, count in counts.items():
        face = DICE_FACES_STANDARD[value - 1]
        if count == 2:
            score += 2
            matches.append(f"Pair of {face} = 2 points")
        elif count == 3:
            score += 10
            matches.append(f"Three {face}'s = 10 points")
        elif count == 4:
            score += 25
            matches.append(f"Four {face}'s = 25 points")
        elif count == 5:
            score += 50
            matches.append(f"Five {face}'s = 50 points")
        elif count == 6:
            score += 100
            matches.append(f"Six {face}'s = 100 points!")
    
    print("\n--- Scoring ---")
    if matches:
        for match in matches:
            print(f"  {match}")
        print(f"\n🏆 Total Score: {score} points")
    else:
        print("  No matches - 0 points")
    
    press_enter()

# ============================================================
# GAME 6: SEQUENCES
# ============================================================
def game_sequences():
    """Try to roll sequential numbers"""
    clear_screen()
    print("=" * 60)
    print("GAME 6: SEQUENCES")
    print("=" * 60)
    print("\nRoll 6 dice. Score points for sequences!")
    print("  • 3 in a row (e.g., ⚀⚁⚂) = 20 points")
    print("  • 4 in a row (e.g., ⚂⚃⚄⚅) = 50 points")
    print("  • 5 in a row = 100 points")
    print("  • Full sequence (⚀⚁⚂⚃⚄⚅) = 200 points!")
    
    input("\nPress ENTER to roll 6 dice...")
    
    dice = roll_dice(6)
    display_dice(dice, "Your roll:")
    
    # Convert to sorted values
    values = sorted([dice_value(d) for d in dice])
    
    # Find longest sequence
    max_seq = 1
    current_seq = 1
    
    for i in range(1, len(values)):
        if values[i] == values[i-1] + 1:
            current_seq += 1
            max_seq = max(max_seq, current_seq)
        elif values[i] != values[i-1]:  # Skip duplicates
            current_seq = 1
    
    # Check for full sequence
    if values == [1, 2, 3, 4, 5, 6]:
        score = 200
        result = "FULL SEQUENCE! ⚀⚁⚂⚃⚄⚅"
    elif max_seq >= 5:
        score = 100
        result = "5 in a row!"
    elif max_seq >= 4:
        score = 50
        result = "4 in a row!"
    elif max_seq >= 3:
        score = 20
        result = "3 in a row"
    else:
        score = 0
        result = "No sequence"
    
    print(f"\n🎯 {result}")
    print(f"🏆 Score: {score} points")
    
    press_enter()

# ============================================================
# GAME 7: BEAT THE HOUSE
# ============================================================
def game_beat_the_house():
    """Roll against the computer - best of 3 rounds"""
    clear_screen()
    print("=" * 60)
    print("GAME 7: BEAT THE HOUSE")
    print("=" * 60)
    print("\nBest of 3 rounds against the computer!")
    print("Highest total each round wins.")
    
    dice_count = 5
    player_wins = 0
    house_wins = 0
    
    for round_num in range(1, 4):
        print(f"\n{'='*60}")
        print(f"ROUND {round_num}")
        print(f"Score: You {player_wins} - House {house_wins}")
        print(f"{'='*60}")
        
        input("\nPress ENTER to roll your dice...")
        player_dice = roll_dice(dice_count)
        display_dice(player_dice, "Your roll:")
        player_total = sum_dice(player_dice)
        print(f"Your total: {player_total}")
        
        print("\n🎰 House is rolling...")
        time.sleep(1)
        house_dice = roll_dice(dice_count)
        display_dice(house_dice, "House roll:")
        house_total = sum_dice(house_dice)
        print(f"House total: {house_total}")
        
        if player_total > house_total:
            print(f"\n✓ You win round {round_num}!")
            player_wins += 1
        elif house_total > player_total:
            print(f"\n✗ House wins round {round_num}")
            house_wins += 1
        else:
            print(f"\n🤝 Round {round_num} is a tie (no points)")
        
        if player_wins == 2:
            print(f"\n🏆 YOU WIN THE MATCH! (2-{house_wins})")
            break
        elif house_wins == 2:
            print(f"\n💔 HOUSE WINS THE MATCH ({player_wins}-2)")
            break
        
        if round_num < 3:
            time.sleep(1)
    
    press_enter()

# ============================================================
# MAIN MENU
# ============================================================
def show_menu():
    """Display the main menu"""
    clear_screen()
    print("=" * 60)
    print("🎲  EMOJI DICE GAMES COLLECTION  🎲")
    print("=" * 60)
    print("\nSelect a game:\n")
    print("  1. Simple Roller       - Just roll some dice")
    print("  2. Highest Wins        - Two players compete")
    print("  3. Target Number       - Hit the exact target")
    print("  4. Skull Survival      - Don't get 3 skulls!")
    print("  5. Doubles (Pairs)     - Match dice for points")
    print("  6. Sequences           - Roll consecutive numbers")
    print("  7. Beat the House      - Play vs computer")
    print("\n  0. Quit")
    print("\n" + "=" * 60)

def main():
    """Main game loop"""
    games = {
        '1': game_simple_roller,
        '2': game_highest_wins,
        '3': game_target_number,
        '4': game_skull_survival,
        '5': game_doubles,
        '6': game_sequences,
        '7': game_beat_the_house,
        '8': game_yahtzee,
    }
    
    while True:
        show_menu()
        choice = input("Enter your choice (0-8): ").strip()
        
        if choice == '0':
            clear_screen()
            print("\n👋 Thanks for playing! Goodbye!\n")
            sys.exit(0)
        
        if choice in games:
            games[choice]()
        else:
            print("\n❌ Invalid choice! Please enter 0-8")
            time.sleep(1)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n👋 Game interrupted. Goodbye!\n")
        sys.exit(0)
