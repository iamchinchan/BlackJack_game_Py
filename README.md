# Blackjack: Modular Python Project (2026)

## Overview

This is a playable Blackjack game built using **Python 3**. This project is a complete rewrite of my 2024 version, focusing on organizing the code into separate files to make it easier to read and maintain.

---

## File Structure

Instead of one long script, the game is split into several files to keep the logic organized:

- **`main.py`**: The main entry point where the game loop runs.
- **`card.py` & `deck.py`**: These handle creating the cards and shuffling the deck.
- **`player.py` & `dealer.py`**: Manage the hands and actions for the player and the dealer.
- **`globals.py`**: Stores card names, suits, and point values in one place.
- **`helper_functions.py`**: Contains the logic for calculating scores and getting user input.

---

## How the Scoring Works

The game includes logic to handle **Aces** automatically. If your hand goes over 21 and you have an Ace, the game changes that Ace's value from 11 down to 1 so you stay in the game.

```python
while total > 21 and aces > 0:
    total -= 10
    aces -= 1
```

Improvements: 2024 vs. 2026
This version shows how my coding style has improved over the last two years:

Better Organization: Moved from a single script to a multi-file package.

Cleaner Code: Uses classes and local variables instead of relying on global variables.

Better Inputs: The game checks for errors, like entering a bet higher than your balance, so the program doesn't crash.

Future Updates
[ ] Tie Logic: Add rules for a "Push" when scores are equal.

[ ] Code Cleanup: Combine shared parts of the Player and Dealer files using inheritance.

[ ] Dealer Blackjack: Check if the dealer has 21 immediately at the start of the round.

How to Run
Ensure you have Python 3 installed.

Run the following command in your terminal:

Bash
python main.py
