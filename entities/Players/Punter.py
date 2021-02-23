from entities.Players.Palyer import Player

class Punter(Player):

    def __init__(self, chips_amount: str, nickname: str=None, deck: str=None):
        self.chips_amount = chips_amount
        super().__init__(nickname, deck)
    
    @property
    def chips_amount(self):
        return self.__chips_amount

    @chips_amount.setter
    def chips_amount(self, chips_amount: int):
        if isinstance(chips_amount, int):
            self.__chips_amount = chips_amount
        else:
            raise ValueError("The 'chips_amount' must be an instance of "+
                " int, got"+str(type(chips_amount)))
    
    def credit_chips_amount(self, chips_amount: int):
        if self.__chips_amount + chips_amount > 0:
            self.__chips_amount += chips_amount
        else:
            raise ValueError("The 'chips_amount' must be a positive"+
                " number")    
    
    def debit_chips_amount(self, chips_amount: int):
        if self.__chips_amount - chips_amount >= 0:
            self.__chips_amount -= chips_amount
        else:
            raise ValueError("The 'chips_amount' must be a positive"+
                " number") 
    
    def can_bet(self, amount):
        if isinstance(amount, int):
            if self.chips_amount - amount >= 0:
                return True
        else:
            raise ValueError("The 'amount' param must be an instance of int, got"+
                str(type(amount)))

        return False
    
    def __str__(self):
        return super().__str__()+f'. Chips: ${self.chips_amount}'