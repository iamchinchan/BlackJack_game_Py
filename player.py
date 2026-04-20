

class Player:
    def __init__(self, amount, name="player1"):
        self.name = name
        self.player_cards = []
        self.wallet_amount = amount

    def add_card(self, new_card):
        self.player_cards.append(new_card)
