from player import Player
from dealer import Dealer
from deck import Deck
from helper_functions import wanna_play_again
from helper_functions import get_bet_amount
from helper_functions import calculate_sum
from helper_functions import endgame
from helper_functions import show_dealer_cards_half, show_player_cards
from helper_functions import wanna_hit

player = Player(500, "Jatin")
dealer = Dealer()

wanna_play = True
while wanna_play:
    deck = Deck()
    deck.deck_shuffle()
    player.player_cards = []
    dealer.dealer_cards = []
    print(f"\n--------------------------------------------")
    print(f"Your wallet Amount: {player.wallet_amount}")
    while True:
        bet_amount = get_bet_amount()
        if (bet_amount <= player.wallet_amount):
            player.wallet_amount -= bet_amount
            break
        else:
            print(
                f"place a bet under your wallet amount : {player.wallet_amount}\n")
            continue
    print(f"Your wallet amount after placing Bet is: {player.wallet_amount}")
    # We have a bet Amount: Now we can start the game
    for _ in range(2):
        player.add_card(deck.draw_one())
        dealer.add_card(deck.draw_one())
    # now both have 2 cards in their hand

    player_sum = calculate_sum(player.player_cards)
    dealer_sum = calculate_sum(dealer.dealer_cards)

    # check for a BlackJack
    if player_sum == 21:
        verdict = f"BlackJack!!, {player.name} won, and will get 9* bet amount: {9*bet_amount}! as winning amount!"
        endgame(verdict, dealer, dealer_sum,
                player, player_sum, bet_amount*9)
    else:
        # Not a black Jack
        while player_sum <= 21:
            print(f"\n-------New State Of cards in Both player Hands:--------\n")
            show_dealer_cards_half(dealer)
            show_player_cards(player)
            print(f"Your card sum is: {player_sum}")
            hit = wanna_hit()
            if hit:
                player.add_card(deck.draw_one())
                player_sum = calculate_sum(player.player_cards)
            else:
                # wanna stay : so delaer's turn then break(important)
                # Dealer's turn
                while dealer_sum <= 21:
                    if player_sum < dealer_sum <= 21:
                        verdict = f"{dealer.name} Won with higher card sum <=21, {player.name} lost the bet!"
                        endgame(verdict, dealer, dealer_sum,
                                player, player_sum, 0)
                        break
                    else:
                        # must draw a card from deck
                        dealer.add_card(deck.draw_one())
                        dealer_sum = calculate_sum(dealer.dealer_cards)
                else:
                    # no break means: dealer Busted
                    verdict = f"{dealer.name} Busted!, {player.name} Won!, and {player.name} wins 2*bet amount: {2*bet_amount}"
                    endgame(verdict, dealer, dealer_sum,
                            player, player_sum, 2*bet_amount)
                break
        else:
            # came out without breaking means pplayer sum is greater than 21 and player busted!
            verdict = f"{player.name} Busted!, and will loose the bet amount now!"
            endgame(verdict, dealer, dealer_sum,
                    player, player_sum, 0)

    if (player.wallet_amount > 0):
        wanna_play = wanna_play_again()
    else:
        print(
            f"You cant play more bets: You wallet Amount: {player.wallet_amount}")
        break
