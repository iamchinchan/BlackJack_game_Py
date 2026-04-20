from card import Card


class User:
    def __init__(self, name):
        self.name = name
        self.hand_cards: list[Card] = []
        self.card_sum = 0

    def get_user_name(self):
        return self.name

    def get_card_sum(self):
        return self.card_sum

    def add_card(self, new_card):
        self.hand_cards.append(new_card)

    def reset_hand(self):
        self.hand_cards = []
        self.card_sum = 0

    def update_card_sum(self):
        # reset card_sum
        self.card_sum = 0
        aces = 0
        for c in self.hand_cards:
            self.card_sum += c.value
            if c.value == 11:
                aces += 1
        # check for self.card_sum>21 and if we have aces then change that ace value from 11 to 1 untill we dont Bust(because of Ace's value): But player/delaer can still bust
        while self.card_sum > 21 and aces > 0:
            self.card_sum -= 10
            aces -= 1

    def has_blackjack(self):
        return self.card_sum == 21 and len(self.hand_cards) == 2

    def __str__(self):
        return (f"{self.name}'s cards are: {[c.rank for c in self.hand_cards]}\nSum of {self.name}'s card is: {self.card_sum}")
