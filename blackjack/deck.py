from random import shuffle, randint
import operator


class Card:
    def __init__(self, suit, rank, value):
        self.suit = suit
        self.rank = rank
        self.value = value

    def __str__(self):
        return f"{self.rank} of {self.suit}"

    def __repr__(self):
        return str(self)


class Deck:

    value = (11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10)
    cards = ('A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K')
    suits = ('H', 'S', 'C', 'D')

    def __init__(self):
        self.reset_deck()
        self.cardlist = []

    def __str__(self):
        str = ""
        hearts = ""
        clovers = ""
        diamonds = ""
        spades = ""
        sorted_deck = sorted(self.cardlist, key=operator.attrgetter('value'))

        str += "Remaining Cards : \n"

        for card in sorted_deck:
            if card.suit == 'H':
                hearts += f'{card.rank} '
            if card.suit == 'S':
                spades += f'{card.rank} '
            if card.suit == 'C':
                clovers += f'{card.rank} '
            if card.suit == 'D':
                diamonds += f'{card.rank} '

        str += " Hearts:\n"
        str += "    " + hearts + "\n"
        #  Remaining Diamonds
        str += " Diamonds :\n"
        str += "    " + diamonds + "\n"
        #  Remaining Clovers
        str += " Clovers :\n"
        str += "    " + clovers + "\n"
        #  Remaining Spades
        str += " Spades :\n"
        str += "    " + spades + "\n"
        return str

    def deal_a_card(self):
        return self.cardlist.pop(0)

    def reset_deck(self):
        self.cardlist = []
        cardval = list(zip(self.cards, self.value))
        for suit in self.suits:
            for rank, val in cardval:
                self.cardlist.append(Card(suit, rank, val))
        #  Rearrange the Card / Shuffle!
        #  determine how many times we shuffle
        shuffle_time = randint(1, 5)
        # print(f'Shuffle {shuffle_time} times')
        # shuffle the deck
        while shuffle_time != 0:
            # print('Shuffle!')
            shuffle(self.cardlist)
            shuffle_time -= 1
        # print(self.current_deck)


if __name__ == '__main__':
    print("Testing Deck Module")
    mydeck = Deck()
    print(mydeck.deal_a_card())
    print(mydeck.deal_a_card())
    print(mydeck.deal_a_card())
    print(mydeck)
