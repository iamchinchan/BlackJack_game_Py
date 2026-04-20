from globals import Values


class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        self.value = Values[rank]

    def __str__(self):
        return f"{self.rank} of {self.suit}"

# card value can be changed now for Ace from 11 to 1 for specific cards when they will be in Hand
