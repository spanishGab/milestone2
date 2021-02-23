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
    player_1 = Player(input("Type the player 1 name: "), Deck())
    player_2 = Player(input("Type the player 2 name: "), Deck())
    
    players_cards = deck.divide_deck_cards(2, deck.cards)

    player_1.deck.add_cards(players_cards[0])
    player_2.deck.add_cards(players_cards[1])

    del deck, players_cards

    victory_cards = []
    war = False
    while True:
        if len(player_2.deck) == 0:
            print(f"{player_1.nickname} Won the game!")
            player_1.deck.add_cards(victory_cards)
            
            print(player_1, 'and', player_2, '\n')
            break
        
        elif len(player_1.deck) == 0:
            print(f"{player_2.nickname} Won the game!")
            player_2.deck.add_cards(victory_cards)
            
            print(player_1, 'and', player_2, '\n')
            break

        player_1_card = player_1.deck.pick_card()
        player_2_card = player_2.deck.pick_card()

        if player_1_card > player_2_card:
            print(f"Player 1 wins this turn. {player_1_card}"+
                  f" > {player_2_card}")

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
        
        elif player_1_card < player_2_card:
            print(f"Player 2 wins this turn. {player_1_card}"+
                  f" < {player_2_card}")

            try:
                if war:
                    for _ in range(0, 3):
                        victory_cards.append(player_1.deck.pick_card())
            except IndexError:
                print("Player 1 ran out of cards during the a war :(\n")
                
            victory_cards.extend((player_1_card, player_2_card))
            player_2.deck.add_cards(victory_cards)

            victory_cards.clear()
            war = False
        
        else:
            print("WAR DECLARED!!!")
            print(f"{player_1_card} == {player_2_card}", '\n')
            victory_cards.extend((player_1_card, player_2_card))
            war = True
        
        time.sleep(0.2)
        
        print(player_1, 'and', player_2, '\n')
        


if __name__ == '__main__':
    game_deck = Deck()
    game_deck.create_ordered_deck(RANK_VALUES)
    game_deck.shuffle()
    play(game_deck)