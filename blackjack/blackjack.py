""" This is a black Jack Game 
    Run through Console
"""
from bjackplayer import BlackJackPlayer, Result
from deck import Deck, Card


class PlayerBUst(Exception):
    def __init__(self, player_name):
        self.player_name = player_name

    def __str__(self):
        return "*** Player Bust!"


class DealerBust(Exception):
    def __str__(self):
        return "*** Dealer Bust!"


class BlackJack:
    def __init__(self):
        self.dealer = BlackJackPlayer()
        self.player = BlackJackPlayer()
        self.deck = Deck()
        self.dealer_card2 = None

    def play(self):
        quit_game = False
        while not quit_game:

            print("***********************************")
            print("*****B L A C K  J A C K 2 1********")
            print("***********************************")
            self.player.update_info()

            keep_playing = True
            while keep_playing:
                print("***********************************")
                print(f'Hi {self.player.name}! Let us Play!!\n')
                print("Current Player Status:")
                print(self.player)
                print("***********************************")
                self.dealer = BlackJackPlayer(name="Dealer", money=2000)  # Always Reset the Dealer

                self.deck.reset_deck()

                self.player.bet()

                self.first_round()

                try:
                    # Player's Turn
                    self.players_turn()
                    # Dealer's Turn
                    self.dealers_turn()

                except PlayerBUst as e:
                    print(e)
                    self.player.update_earnings(Result.LOS)

                except DealerBust as e:
                    print(e)
                    self.player.update_earnings(Result.WON)

                else:
                    print("*** Deal's Result : ")
                    self.player.update_earnings(self.player.get_result(self.dealer.card_value))

                if input("\nKeep Playing ? (Y)es or (N)o : ") not in ['Y', 'y']:
                    print("***********************************")
                    print("Thank you for Playing!")
                    print(f"You can cash in ${self.player.money}")
                    print("***********************************")
                    break

                if self.player.money == 0:
                    print("\nYou're Broke! Go Home!")
                    print("***********************************")
                    break

            if input("\nNew Player? (Y)es or (N)o : ") not in ['y', 'Y']:
                print("\n****** Thank you! Come Again! *******")
                break

    def first_round(self):
        print("***********************************")
        # Deal to the dealer 2 Cards, 1 face down
        print("Dealer's Card Turn : \n")
        self.dealer.hit(self.deck.deal_a_card())
        self.dealer_card2 = self.deck.deal_a_card()  # get this but do not show it first
        print("***********************************")
        # Deal to the player 2 Cards
        print("\nPlayer's Card Turn : ")
        self.player.hit(self.deck.deal_a_card())
        self.player.hit(self.deck.deal_a_card())
        print("***********************************")

    def players_turn(self):
        # player's turn
        while True:
            if input("\n(H)it or (S)tay : ") in ['h', 'H']:
                if not self.player.hit(self.deck.deal_a_card()):
                    raise PlayerBUst(self.player.name)  # when raising custom exception, you need to follow constructor
            else:
                break
        print("***********************************")

    def dealers_turn(self):
        print("\nDealer's 2nd Card Open : ")
        self.dealer.hit(self.dealer_card2)  # Show the 2nd Card
        while True:
            # Check if Dealer already got a winning value
            if self.dealer.get_result(self.player.card_value) in [Result.WON, Result.DRW]:
                break
            # Hit until Dealer Won or Bust or Draw
            input("\nDealer Hitting. Enter Any Key to Continue...")
            if not self.dealer.hit(self.deck.deal_a_card()):
                raise DealerBust()  # when raising custom exception, you need to follow constructor


if __name__ == '__main__':
    Casino101 = BlackJack()
    Casino101.play()
