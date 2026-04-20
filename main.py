from player import Player
from dealer import Dealer
from deck import Deck
from helper_functions import wanna_play_again
from helper_functions import wanna_hit
from helper_functions import endgame


player = Player(500, "Jatin")
dealer = Dealer()

wanna_play = True
while wanna_play:
    deck = Deck()
    deck.deck_shuffle()

    # Release the old cards from last Bet
    player.reset_hand()
    dealer.reset_hand()
    print(f"\n--------------------------------------------")
    print(f"Your wallet Amount: {player.get_wallet_amount()}")
    bet_amount = player.place_bet()

    # We have a bet Amount: Now we can start the game
    for _ in range(2):
        player.add_card(deck.draw_one())
        dealer.add_card(deck.draw_one())
    # now both have 2 cards in their hand

    # update card sum for both
    player.update_card_sum()
    dealer.update_card_sum()

    # check for a BlackJack
    if player.has_blackjack() and dealer.has_blackjack():
        # Tie
        verdict = f"Its a Tie! as Both Players got Blackjack!! adding Bet amount back to the {player.get_user_name()}"
        endgame(verdict, dealer, player, bet_amount)
    elif player.has_blackjack():
        # but dealer does not have blackjack!
        verdict = f"BlackJack!!, {player.get_user_name()} won, and will get 5* bet amount: {5*bet_amount}! as winning amount!"
        endgame(verdict, dealer, player, bet_amount*5)
    elif dealer.has_blackjack():
        # but player does not have blackjack!
        verdict = f"{dealer.get_user_name()} got BlackJack!! and {player.get_user_name()} lost the Round and Bet Money!!"
        endgame(verdict, dealer, player, 0)
    else:
        # No blackJack for anyone!!
        while player.get_card_sum() < 21:
            print(f"\n-------New State Of cards in Both player Hands:--------\n")
            dealer.show_dealer_cards_half()
            print(player)
            hit = wanna_hit()
            if hit:
                player.add_card(deck.draw_one())
                player.update_card_sum()
            else:
                # sum==21 or Busted(>21)
                break
        if player.get_card_sum() <= 21:
            # player stayed or sum==21: falls into this if condition

            # Dealers Turn
            while dealer.get_card_sum() < 17:
                # According to Rules: Dealer must Hit until it's Sum >=17
                dealer.add_card(deck.draw_one())
                dealer.update_card_sum()

            if dealer.get_card_sum() > 21:
                # Dealer Busted, Player Won
                verdict = f"{dealer.get_user_name()} Busted!, {player.get_user_name()} Won!, and {player.get_user_name()} wins 2*bet amount: {2*bet_amount}"
                endgame(verdict, dealer, player, 2*bet_amount)

            # now sum<=21 but comparing with player
            elif dealer.get_card_sum() == player.get_card_sum():
                # tie
                verdict = f"Its a Push/Tie! as Both Players got same sum!! adding Bet amount back to the {player.get_user_name()}"
                endgame(verdict, dealer, player, bet_amount)

            elif dealer.get_card_sum() > player.get_card_sum():
                # Dealer Won, Player lost! But no one Busted.
                verdict = f"{dealer.get_user_name()} Won with higher card sum <=21, {player.get_user_name()} lost the bet!"
                endgame(verdict, dealer, player, 0)
            else:
                # Player Won!, Dealer lost. But no one Busted.
                verdict = f"{player.get_user_name()} Won with higher card sum <=21, {dealer.get_user_name()} lost the bet!, adding 2*bet amount: {2*bet_amount}"
                endgame(verdict, dealer, player, 2*bet_amount)

        else:
            # sum>21 and player busted!
            verdict = f"{player.get_user_name()} Busted!, and will loose the bet amount now!"
            endgame(verdict, dealer, player, 0)

    if (player.get_wallet_amount() > 0):
        wanna_play = wanna_play_again()
    else:
        print(
            f"You cant play more bets: You wallet Amount: {player.get_wallet_amount()}")
        break
