from globals import Suits, Ranks
from card import Card
from random import shuffle


class Deck:
    def __init__(self):
        self.deck_card = []
        for suit in Suits:
            for rank in Ranks:
                self.deck_card.append(Card(suit, rank))

    def deck_shuffle(self):
        shuffle(self.deck_card)

    def draw_one(self):
        return self.deck_card.pop()
    # no need to check if decks empty as for Blackjack game,either of players will either bust or win before deck is empty
    # And for each new Bet, new deck object can be created from this Deck class and old one can be released from memory
