import os
from subprocess import call
import time

from entities.Card import Card, CARD_SUITS
from entities.Deck import Deck

from entities.Players.Punter import Punter
from entities.Players.Palyer import Player

RANK_VALUES = {
    'Ace': 1,
    'Two': 2,
    'Three': 3,
    'Four': 4,
    'Five': 5,
    'Six': 6,
    'Seven': 7,
    'Eight': 8,
    'Nine': 9,
    'Ten': 10,
    'Jack': 10,
    'Queen': 10,
    'King': 10,
}

clear = lambda: 'clear' if os.name =='posix' else 'cls'

def print_player_status(player: Player):
    """
    Prints the current player status to the stdout

    Args:
        player (Player): player to be printed on
    """
    print(f"\n{player.nickname}'s Deck: {player.deck}")
    print(player)
    print(f"{player.nickname}'s points: {player.sum_points()}\n")


def game_over(player: Player) -> str:
    """
    Checks whether the game is over by looking at the player's points

    Args:
        player (Player): player whose the points will be checked

    Returns:
        str: describes the type of end:
            'won' -> the player won the match
            'lost' -> the player lost the match
            '' -> its not a game over yet
    """
    end = ''
    if player.sum_points() > 21:
        end = 'lost'
        print(f"{player.nickname} Loses!")
        input("Press enter to continue")
        
    elif player.sum_points() == 21:
        end = 'won'
        print(f"Congrats {player.nickname}, you win!")
        input("Press enter to continue")

    return end


def check_for_next_match(player: Player) -> bool:
    """
    Checks whether the player want to continue playing

    Args:
        player (Player): the player to be asked

    Returns:
        bool: True if the player wants to keep playing, otherwise it's False
    """
    while True:
        keep_playing = input(f"{player.nickname}, do you want to play"+
            " again? [y / n] ")
        
        if keep_playing.lower() == 'y':
            keep_playing = True
            break
        elif keep_playing == 'n':
            keep_playing = False
            break
        else:
            print("\nPlease, type 'y' to yes and 'n' to no")
    
    return keep_playing


def make_move(player: Player, action: str, deck: Deck) -> Player:
    """
    Makes a player's movement based on the given action

    Args:
        player (Player): the player instance
        action (str): the action to be performed
        deck (Deck): the game's main deck

    Returns:
        Player: the player after the movement has been made
    """
    # 'hit' action
    if action == 'h':
        card = deck.pick_card()
        
        # allowing the player to choose which value to consider for the Ace (1, 11)
        if card.rank == 'Ace' and player.nickname.lower() != 'dealer':
            print(f"\n{player.nickname} have got an {card}")
            
            while True:
                try:
                    ace_value = int(input("Do you want to make it worth 1 or "+
                        " 11? "))
                except ValueError:
                    print("\nOops, type an integer value only")
                    continue

                if ace_value in (1, 11):
                    card.rank_value = ace_value
                    break
                else:
                    print("Oops, type 1 or 11 only")

        player.deck.add_cards(card)
        print(f"\nJust added {card} to {player.nickname}\n")
    # 'stay' action
    elif action == 's':
        print(f"\nOk, just passing {player.nickname}'s turn\n")
    
    print_player_status(player)

    return player


def play():
    # setting the global loop control varibale
    keep_playing = True

    # instantiating the player and dealer classes
    player = Punter(20, nickname=input("Type player1's name: "))
    dealer = Player(nickname="Dealer")

    # game's global loop
    while keep_playing:
        # clearing the stdout
        call(clear())
        
        # checking if the player still have got enough chips to play
        if not player.can_bet(10):
            print(f"{player.nickname} have got no enough chips to play!\n")
            break

        # instantiating a new game's deck
        deck = Deck()
        deck.create_ordered_deck(RANK_VALUES)
        deck.shuffle()

        # instantiating empty decks to both player and dealer
        player.deck = Deck()
        dealer.deck = Deck()

        # adding two cards to begin the game
        player.deck.add_cards((deck.pick_card(), deck.pick_card()))
        dealer.deck.add_cards((deck.pick_card(), deck.pick_card()))

        print_player_status(player)
        print_player_status(dealer)
        
        end = False

        # loop to check for the end of the current match
        while not end:
            # asks player an action (hit or stay)
            action = input("Do you want to stay or hit? [s / h] ").lower()
            
            if action not in ('s', 'h'):
                print("Please, type 'h' to hit and 's' to stay")
                continue

            # making player's move according to the given action
            player = make_move(player, action, deck)
            
            # checking if player won or lost the match
            match_result = game_over(player)
            if match_result == 'won':
                player.credit_chips_amount(10)
                break
            elif match_result == 'lost':
                try:
                    player.debit_chips_amount(10)
                except ValueError:
                    print(f"{player.nickname} have got no enough chips to play")
                break
            

            # making dealer's movement (always) will hit
            dealer = make_move(dealer, 'h', deck)
            
            # checking if dealer won or lost the match
            match_result = game_over(dealer)
            if match_result == 'won':
                try:
                    player.debit_chips_amount(10)
                except ValueError:
                    print(f"{player.nickname} have got no enough chips to play")
                break
            elif match_result == 'lost':
                player.credit_chips_amount(10)
                break
        
        call(clear())
        print_player_status(player)
        print_player_status(dealer)        
        keep_playing = check_for_next_match(player)

play()
            


                
    