from user import User


class Dealer(User):
    def __init__(self, name="Dealer"):
        super().__init__(name)

    def show_dealer_cards_half(self):
        print(
            f"{self.name}'s Cards are : [{self.hand_cards[0].rank}, 'X-hidden']")
