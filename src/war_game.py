import time
from entities.Deck import Deck
from entities.Players.Palyer import Player

RANK_VALUES = {
    'Two': 2,
    'Three': 3,
    'Four': 4,
    'Five': 5,
    'Six': 6,
    'Seven': 7,
    'Eight': 8,
    'Nine': 9,
    'Ten': 10,
    'Jack': 11,
    'Queen': 12,
    'King': 13,
    'Ace': 14,
}

def play(deck):
    # instantiating players
    player_1 = Player(input("Type the player 1 name: "), Deck())
    player_2 = Player(input("Type the player 2 name: "), Deck())
    
    # dividing the deck into two halfs
    players_cards = deck.divide_deck_cards(2, deck.cards)

    # adding the halfs to the players
    player_1.deck.add_cards(players_cards[0])
    player_2.deck.add_cards(players_cards[1])

    # dismissing unused varible
    del players_cards

    victory_cards = []
    war = False

    # game's main loop
    while True:
        # checking whether the player 2 ran out of cards (player1's victory)
        if len(player_2.deck) == 0:
            print(f"{player_1.nickname} Won the game!")
            player_1.deck.add_cards(victory_cards)
            
            print(player_1, 'and', player_2, '\n')
            break
        # checking whether the player 1 ran out of cards (player2's victory)
        elif len(player_1.deck) == 0:
            print(f"{player_2.nickname} Won the game!")
            player_2.deck.add_cards(victory_cards)
            
            print(player_1, 'and', player_2, '\n')
            break

        # picking a card for each player
        player_1_card = player_1.deck.pick_card()
        player_2_card = player_2.deck.pick_card()

        # checking whether player1 wins the turn
        if player_1_card > player_2_card:
            print(f"Player 1 wins this turn. {player_1_card}"+
                  f" > {player_2_card}")

            # if war was declared, checks whether player2 still have cards to play
            if war:
                try:
                    for _ in range(0, 3):
                        victory_cards.append(player_2.deck.pick_card())
                except IndexError:
                    print("Player 2 ran out of cards during the a war :(\n")
                
            victory_cards.extend((player_1_card, player_2_card))
            player_1.deck.add_cards(victory_cards)

            victory_cards.clear()
            war = False
        # checking whether player2 wins the turn
        elif player_1_card < player_2_card:
            print(f"Player 2 wins this turn. {player_1_card}"+
                  f" < {player_2_card}")

            # if war was declared, checks whether player1 still have cards to play
            if war:
                try:
                    for _ in range(0, 3):
                        victory_cards.append(player_1.deck.pick_card())
                except IndexError:
                    print("Player 1 ran out of cards during the a war :(\n")
                
            victory_cards.extend((player_1_card, player_2_card))
            player_2.deck.add_cards(victory_cards)

            victory_cards.clear()
            war = False
        # if it's a draw, then war is declared
        else:
            print("WAR DECLARED!!!")
            print(f"{player_1_card} == {player_2_card}", '\n')
            victory_cards.extend((player_1_card, player_2_card))
            war = True
        
        # use this to see the match slower or faster
        # time.sleep(0.01)
        
        print(player_1, 'and', player_2, '\n')



if __name__ == '__main__':
    # instantiates a new Deck for the match
    game_deck = Deck()
    game_deck.create_ordered_deck(RANK_VALUES)
    game_deck.shuffle()
    play(game_deck)