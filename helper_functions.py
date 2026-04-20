from card import Card
from player import Player
from dealer import Dealer


def wanna_play_again():
    print(f"Do you want to place a new bet? ")
    while True:
        try:
            val = input("Type y/Y for Yes and type n/N for No: ")
            if val.lower() in ("y", "n"):
                return val.lower() == "y"
            else:
                print(f"please enter a correct choice/n")
        except:
            print(f"Please try Again with a valid input\n")


def get_bet_amount():
    print(f"Please enter the amount you want to place as a bet: ")
    while True:
        try:
            val = int(input("Please enter a amount: "))
            if val > 0:
                return val
            else:
                print(f"Minimum bet is: 1rs\n")

        except:
            print(f"Please enter a valid value\n")
            continue


def wanna_hit():
    print(f"Do you wanna Hit or Stay! ")
    while True:
        try:
            val = input("\nType h/H for Hit and Type s/S for Stay: ")
            if val.lower() in ("h", "s"):
                return val.lower() == "h"
            else:
                print(f"Please enter a correct choice\n")
        except:
            print(f"please enter a valid input\n")


def calculate_sum(hand_cards: list[Card]):
    total = 0
    aces = 0
    for c in hand_cards:
        total += c.value
        if c.value == 11:
            aces += 1
    # check for sum>21 and if we have aces then change that ace value from 11 to 1 untill we dont Bust(because of Ace's value): But player/delaer can still bust
    while total > 21 and aces > 0:
        total -= 10
        aces -= 1

    return total


def show_dealer_cards_half(dealer: Dealer):
    print(
        f"{dealer.name}'s Cards are : [{dealer.dealer_cards[0].rank}, 'X-hidden']")


def show_dealer_cards_full(dealer: Dealer):
    print(
        f"{dealer.name}'s cards are: {[c.rank for c in dealer.dealer_cards]}")


def show_player_cards(player: Player):
    print(f"{player.name} cards are: {[c.rank for c in player.player_cards]}")


def endgame(verdict: str, dealer: Dealer, dealer_sum: int, player: Player, player_sum: int, value: int):
    print(f"\n--------------------------------------------")
    print(f"{verdict}")
    show_dealer_cards_full(dealer)
    print(f"{dealer.name}'s card sum is : {dealer_sum}")
    show_player_cards(player)
    print(f"{player.name}'s card sum is: {player_sum}")
    print(f"wallet amount after placing bet: {player.wallet_amount}")
    print(f"After This Game: ")
    player.wallet_amount += value
    print(f"New wallet Amount: {player.wallet_amount}")
    print(f"\n--------------------------------------------")
