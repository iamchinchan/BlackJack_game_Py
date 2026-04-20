
def wanna_play_again():
    print(f"Do you want to place a new bet? ")
    while True:
        try:
            val = input("Type y/Y for Yes and type n/N for No: ")
            if val.lower() in ("y", "n"):
                return val.lower() == "y"
            else:
                print(f"please enter a correct choice\n")
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


def endgame(verdict: str, dealer, player, value: int):
    print(f"\n--------------------------------------------")
    print(f"{verdict}")
    print(dealer)
    print(player)
    print(f"wallet amount after placing bet: {player.get_wallet_amount()}")
    print(f"After This Game: ")
    player.update_wallet_amount(value)
    print(f"New wallet Amount: {player.get_wallet_amount()}")
    print(f"\n--------------------------------------------")
