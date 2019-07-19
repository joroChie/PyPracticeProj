""" Black Jack Player Class
"""

from deck import Card

class InsufficientFund(Exception):
    pass


class ValueTooSmall(Exception):
    pass


class Result:
    WON = 1
    LOS = 0
    DRW = 2


class BlackJackPlayer:
    min_buy_in = 200  # note that without self notation, this will be the same value for all instance of this object

    def __init__(self, name="Anonymous", money=200):
        self.name = name
        self.money = money
        self.current_card = []
        self.current_bet = 0
        self.card_value = 0
    
    def __str__(self):
        mystr = ""
        mystr += f'\tPlayer : {self.name}\n'
        mystr += f'\tMoney  : {self.money}'
        return mystr

    def update_info(self):
        name = input("Player's Name : ")
        while True:
            try:
                buyin = int(input("Buy in Amount : "))
                if buyin < BlackJackPlayer.min_buy_in:
                    raise ValueTooSmall
            except ValueError:
                print("Invalid Amount! Try Again!")
            except ValueTooSmall:
                print(f"Amount Cannot be less than {BlackJackPlayer.min_buy_in}!")
            else:
                break
        self.name = name
        self.money = buyin

    def hit(self, card):
        self.current_card.append(card)
        self.calculate_optimal_21()
        print(f'Current Cards : {self.current_card}')
        print(f"Optimal Value : {self.card_value}")
        if self.card_value > 21:
            return False

        return True

    def stay(self):
        self.calculate_optimal_21()
        print(f"Optimal Value : {self.card_value}")

    def bet(self):

        while True:
            try:
                bet = int(input("Place your bet : "))
                if bet < 0:
                    raise ValueError
                if bet > self.money:
                    raise InsufficientFund
            except ValueError:
                print("Please Input Valid Integer!")
            except InsufficientFund:
                print("Please Input Value within your Funds!")
                print(self)
            else:
                self.current_bet = bet
                break

    def get_result(self, opponent_val):
        if self.card_value <= 21 and self.card_value == opponent_val:
            return Result.DRW

        if self.card_value > 21:
            return Result.LOS

        if opponent_val > 21:
            return Result.WON

        if self.card_value < opponent_val:
            return Result.LOS
        else:
            return Result.WON

    def update_earnings(self, result):
        if result == Result.WON:
            print(f"You Won ! [+${self.current_bet}]")
            self.money += self.current_bet
        elif result == Result.LOS:
            print(f"You Loss! [-${self.current_bet}]")
            self.money -= self.current_bet
        else:
            print("It's a Draw!")
            pass
        self.current_bet = 0
        self.current_card = []
        self.card_value = 0
        print(self)

    def calculate_optimal_21(self):
        aces = [card for card in self.current_card if card.rank == 'A']
        self.card_value = 0

        # Sum All Cards First
        for card in self.current_card:
            self.card_value += card.value
        # Evaluate Value if there are aces
        for _ in aces:
            if self.card_value > 21:
                self.card_value -= 10   # down grade ace to 1 if it will go beyond 21


if __name__ == "__main__":
    pass



