class Dealer:
    def __init__(self):
        self.name = "dealer"
        self.dealer_cards = []

    def add_card(self, new_card):
        self.dealer_cards.append(new_card)
