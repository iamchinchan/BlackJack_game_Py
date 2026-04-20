from user import User
from helper_functions import get_bet_amount


class Player(User):
    def __init__(self, amount, name="player1"):
        super().__init__(name)
        self.wallet_amount = amount

    def get_wallet_amount(self):
        return self.wallet_amount

    def place_bet(self):
        while True:
            bet_amount = get_bet_amount()
            if (bet_amount <= self.wallet_amount):
                self.wallet_amount -= bet_amount
                break
            else:
                print(
                    f"place a bet under your wallet amount : {self.wallet_amount}\n")
                continue
        print(
            f"Your wallet amount after placing Bet is: {self.wallet_amount}")
        return bet_amount

    def update_wallet_amount(self, value: int):
        self.wallet_amount += value
