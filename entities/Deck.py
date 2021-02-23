import random
from entities.Card import Card, CARD_SUITS, CARD_RANKS

class Deck:

    def __init__(self):
        self.__cards = []

    @property
    def cards(self):
        return self.__cards
    
    def create_ordered_deck(self, ordered_card_rank: dict):
        if isinstance(ordered_card_rank, dict):
            for suit in CARD_SUITS:
                for rank, value in ordered_card_rank.items():
                    if rank in CARD_RANKS:
                        self.__cards.append(Card(suit, rank, value))
                    else:
                        raise ValueError("All the 'ordered_card_rank' param "+
                        " values must be equal to some of these: "+
                        str(CARD_RANKS)+". With Case Sensitivity")
        else:
            raise ValueError("The 'ordered_card_rank' must be an instace of "+
                "dict, got"+str(type(ordered_card_rank)))
    
    def shuffle(self):
        random.shuffle(self.cards)

    def pick_card(self, position: int=-1):
        return self.cards.pop(position)
    
    def add_cards(self, cards, position: int=0):
        try:
            if isinstance(cards, Card):
                self.cards.insert(position, cards)
            else:
                for card in cards:
                    if isinstance(card, Card):
                        self.cards.insert(position, card)
                    else:
                        raise TypeError("The 'cards' param must only contain "+
                            "Card objects")
        except TypeError:
            raise TypeError("The 'cards' param must be an iterable containig "
                +" Card objects or a Card object itself")

    @staticmethod
    def divide_deck_cards(division: int, cards: list) -> list:
        if len(cards) != 52:
            raise ValueError("The 'deck' must have a complete cards deck (52 cards) "+
                str(len(cards))+" found.")
        
        divided_deck = []
        tmp = []
        count = 0

        for _ in range(0, division):
            while count < (52 / division):
                tmp.append(cards.pop())
                count += 1
            
            divided_deck.append(tmp.copy())
            tmp.clear()
            count = 0
        
        return divided_deck
    
    def __len__(self):
        return len(self.cards)
    
    def __str__(self):
        deck = []
        for item in self.cards:
            deck.append(str(item))
        
        return '{'+', '.join(deck)+'}'
