CARD_SUITS_SKIN = {
    'black-spade': '\u2660',
    'white-heart': '\u2661',
    'white-diamond': '\u2662',
    'black-club': '\u2663',
}

CARD_SUITS = tuple(CARD_SUITS_SKIN.keys())

CARD_RANKS = (
    'Ace',
    'Two',
    'Three',
    'Four',
    'Five',
    'Six',
    'Seven',
    'Eight',
    'Nine',
    'Ten',
    'Jack',
    'Queen',
    'King',
)

class Card:
    """
    A simple Card class that holds a card's rank, suit and value.
    """

    def __init__(self, suit: str, rank: str, rank_value: int):
        self.suit = suit
        self.rank = rank
        self.rank_value = rank_value

    @property
    def suit(self):
        return self.__suit

    @suit.setter
    def suit(self, suit: str):
        if suit in CARD_SUITS:
            self.__suit = suit
        else:
            raise TypeError("The suit param must be one of the valid card suits: "+
                str(CARD_SUITS))

    @property
    def rank(self):
        return self.__rank

    @rank.setter
    def rank(self, rank: str):
        if rank in CARD_RANKS:
            self.__rank = rank
        else:
            raise TypeError("The 'rank' param must be one of the valid ranks: "+
                str(CARD_RANKS))

    @property
    def rank_value(self):
        return self.__value
    
    @rank_value.setter
    def rank_value(self, rank_value: int):
        if isinstance(rank_value, int):
            self.__value = rank_value
        else:
            raise TypeError("The 'rank_value' param must be an instance of "+
                "int, got"+str(type(rank_value)))

    def __str__(self):
        return str(self.rank) +" of "+ CARD_SUITS_SKIN[self.suit]

    def __eq__(self, rank_value):
        if isinstance(rank_value, Card):
            return self.rank_value == rank_value.rank_value
        else:
            raise TypeError("The 'rank_value' param must be an instance of Card")

    def __lt__(self, rank_value):
        if isinstance(rank_value, Card):
            return self.rank_value < rank_value.rank_value
        else:
            raise TypeError("The 'rank_value' param must be an instance of Card")

    def __gt__(self, rank_value):
        if isinstance(rank_value, Card):
            return self.rank_value > rank_value.rank_value
        else:
            raise TypeError("The 'rank_value' param must be an instance of Card")
