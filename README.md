# Blackjack: Modular Python Project (2026)

## 📌 Overview

This is a fully playable, object-oriented Blackjack game built with **Python 3**. This project represents a complete redesign of my original 2024 script, focusing on clean code, modularity, and better organization.

---

## 🏗️ Project Structure

Instead of one long file, the game is split into specific modules to keep the logic clear and easy to manage:

- **`main.py`**: The entry point that controls the game flow and betting rounds.
- **`user.py`**: A parent class that handles shared logic like card sums and Blackjack checks for both the Player and Dealer.
- **`player.py` & `dealer.py`**: Specific classes that inherit from `User` to manage wallets and dealer-specific card views.
- **`card.py` & `deck.py`**: Logic for creating cards and managing a 52-card deck that shuffles automatically if it runs out.
- **`globals.py`**: A central file for game constants like Suits, Ranks, and card Values.
- **`helper_functions.py`**: Handles all user inputs and the final game results.

---

## 🧠 Key Features

### 1. Automatic Ace Handling

The game automatically calculates whether an Ace should be worth **11 or 1**. If your total goes over 21, it reduces the Ace value to keep you in the game.

```python
while self.card_sum > 21 and aces > 0:
    self.card_sum -= 10
    aces -= 1

```

2. Standard Dealer Rules (The 17 Rule)
   The dealer follows professional casino rules: they must keep drawing cards until their total is at least 17, after which they must stay.

3. Error-Proof Inputs
   The game is designed to stay running even if a user makes a mistake. It uses validation loops to ensure you enter valid bets and choices without crashing the program.

📈 The Journey: 2024 vs. 2026
This version highlights my growth in software development over the last two years:

From Scripts to Systems: Moved from a single procedural script to an Object-Oriented (OOP) structure using Inheritance.

Better Memory Management: Objects like the Deck and Hand are reset properly between rounds to keep the game efficient.

Clean Logic: Replaced messy global variables with a dedicated globals.py and local class attributes.

🛠️ Future Roadmap
[ ] Double Down: Add the option for players to double their bet for one extra card.

🚀 How to Run
Ensure you have Python 3 installed on your system.

Download or clone this repository.

Open your terminal in the project folder and run:
python main.py
