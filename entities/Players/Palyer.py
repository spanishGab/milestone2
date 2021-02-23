from entities.Card import Card
from entities.Deck import Deck

class Player():

    def __init__(self, nickname: str=None, deck: Deck=None):
        self.nickname = nickname
        self.deck = deck
    
    @property
    def nickname(self):
        return self.__nickname
    
    @nickname.setter
    def nickname(self, nickname: str):
        if nickname is not None:
            if isinstance(nickname, str):
                if nickname.strip() != '':
                    self.__nickname = nickname.strip()
                else:
                    raise TypeError("The nickname attribute cannot be blank")    
            else:
                raise TypeError("The nickname attribute must be an instance of str")
        
        else:
            self.__nickname = None
    
    @property
    def deck(self):
        return self.__deck
    
    @deck.setter
    def deck(self, deck: Deck):
        if deck is not None:
            if isinstance(deck, Deck):
                self.__deck = deck
            else:
                raise TypeError("The deck attribute must be an instance of Deck")
        else:
            self.__deck = None
    
    def sum_points(self) -> int:
        return sum([card.rank_value for card in self.deck.cards])
    
    def __str__(self):
        return f'{self.nickname} has {len(self.deck.cards)} cards'

    
