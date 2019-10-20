"""
This is the Blackjack game

"""
import random

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5, 'Six': 6, 'Seven': 7, 'Eight': 8, 'Nine': 9, 'Ten': 10,
          'Jack': 10, 'Queen': 10, 'King': 10, 'Ace': 11}
playing = True


class Card:

    # This method is used to initialize the attributes of an object, passed as arguments
    def __init__(self, card_suit, card_rank, card_value):
        # The card has 3 attributes
        self.card_suit = card_suit
        self.card_rank = card_rank
        self.card_value = card_value

    def __str__(self):
        return self.card_rank + " of " + self.card_suit + ", value " + str(self.card_value)


class Deck:

    def __init__(self):

        # Only one attribute is needed here
        self.my_deck_of_52_cards = []

        # Creating Card objects and appending them to the list attribute
        for suit in suits:
            for rank in ranks:
                self.my_deck_of_52_cards.append(Card(suit, rank, values[rank]))

        # Shuffling the deck, now they are not ordered
        Deck.shuffle(self)

    def __str__(self):
        string = ""
        for card in self.my_deck_of_52_cards:
            string += (card.card_rank + " of " + card.card_suit + ", value " + str(card.card_value) + "\n")
        return string

    def shuffle(self):
        random.shuffle(self.my_deck_of_52_cards)

    def deal(self):
        self.my_deck_of_52_cards.pop(0)
        return self.my_deck_of_52_cards[0]


class Hand:

    def __init__(self):

        self.cards = []
        self.value = 0
        self.aces = 0

    def __str__(self):

        string = ""
        for card in self.cards:
            string += ("\t" + card.card_rank + " of " + card.card_suit + ", value " + str(card.card_value) + "\n")
        return string

    def add_card(self, card):

        self.cards.append(card)
        self.value += card.card_value

        if card.card_value == 11:
            self.aces += 1

        Hand.adjust_for_ace(self)

    def adjust_for_ace(self):
        # Aces will never be higher than 1, since we are checking the value in every card_add
        if self.value > 21 and self.aces == 1:
            self.value -= 10
            self.aces = 0


class Chips:

    def __init__(self):
        self.total = 100
        self.bet = 0

    def win_bet(self):
        self.total += self.bet

    def lose_bet(self):
        self.total -= self.bet


def take_a_bet(chips):
    print("\nChips available: " + str(chips.total) + "\n")
    while True:

        try:
            cust_bet = int(input("How much you wanna bet? "))
        except:
            print("Enter a number and try again.")
            continue
        else:
            if cust_bet > chips.total:
                print("You don't have enough chips available to bet this amount. ")
                continue
            elif cust_bet <= 0:
                continue
            else:
                chips.bet = cust_bet
                print("\nBet accepted! Good luck!")
                break


def hit(deck, hand):
    hand.add_card(deck.deal())


def hit_or_stand(deck, hand):
    global playing

    while True:

        try:
            if hand.value <= 21:
                action = input("Do you wanna HIT[H] or STAND[S]? ")
            else:
                break
        except:
            print("Enter a valid action and try again.")
            continue
        else:
            if action.upper() == "H":
                hit(deck, hand)
                break
            elif action.upper() == "S":
                playing = False
                break
            else:
                print("Enter a valid action and try again.")
                continue


def show_some(player_hand, dealer_hand):
    print("\n** PLAYER CARDS -- Total value: " + str(player_hand.value))
    print(player_hand)

    print("** DEALER CARDS")
    string = ""
    for card in dealer_hand.cards[1:]:
        string += ("\t" + card.card_rank + " of " + card.card_suit + ", value " + str(card.card_value) + "\n")
    print(string)


def show_all(player_hand, dealer_hand):
    print("+" * 50)
    print("\n** PLAYER CARDS -- Total value: " + str(player_hand.value))
    print(player_hand)

    print("** DEALER CARDS -- Total value: " + str(dealer_hand.value))
    print(dealer_hand)
    print("+" * 50)


def player_busts(final_chips):
    print("PLAYER BUSTED - You lost your " + str(final_chips.bet) + "chips bet")
    final_chips.lose_bet()


def player_wins(final_chips):
    print("PLAYER WINS - You won your " + str(final_chips.bet) + "chips bet")
    final_chips.win_bet()


def dealer_busts(final_chips):
    print("PLAYER WINS - You won your " + str(final_chips.bet) + "chips bet")
    final_chips.win_bet()


def dealer_wins(final_chips):
    print("DEALER WON - You lost your " + str(final_chips.bet) + "chips bet")
    final_chips.lose_bet()


def push(final_chips):
    print("IT'S A PUSH - You keep your " + str(final_chips.bet) + "chips bet")


def wanna_play_again():
    while True:

        try:
            x = input("\nDo you wanna play again? Yes[Y] / No[N] ")
        except:
            print("Please enter a valid option")
        else:
            if x.upper() == "Y":
                break
            elif x.upper() == "N":
                break
            else:
                continue
    return x.upper()


if __name__ == "__main__":

    # Print an opening statement
    print("\n" + "*" * 50)
    print("Welcome to the BlackJack Game")
    print("*" * 50)

    # Set up the Player's chips
    chips = Chips()

    while True:

        # Create & shuffle the deck,
        deck = Deck()
        # Deal two cards to each player
        player_hand = Hand()
        player_hand.add_card(deck.deal())
        player_hand.add_card(deck.deal())
        # Deal two cards to each player
        dealer_hand = Hand()
        dealer_hand.add_card(deck.deal())
        dealer_hand.add_card(deck.deal())

        # Prompt the Player for their bet
        take_a_bet(chips)
        # Show cards (but keep one dealer card hidden)
        show_some(player_hand, dealer_hand)

        while playing:  # recall this variable from our hit_or_stand function

            # Prompt for Player to Hit or Stand
            hit_or_stand(deck, player_hand)
            # Show cards (but keep one dealer card hidden)
            show_some(player_hand, dealer_hand)
            # If player's hand exceeds 21, run player_busts() and break out of loop
            if player_hand.value > 21:
                break

        # If Player hasn't busted, play Dealer's hand until Dealer reaches 17
        while dealer_hand.value <= 17 and player_hand.value <= 21:
            dealer_hand.add_card(deck.deal())

        # Show all cards
        show_all(player_hand, dealer_hand)

        # print("Let's debug chips...")
        # print(chips.total)
        # print(chips.bet)

        # Run different winning scenarios
        if player_hand.value > 21:
            player_busts(chips)
        elif (player_hand.value <= 21) and (player_hand.value > dealer_hand.value):
            player_wins(chips)
        elif (dealer_hand.value <= 21) and (dealer_hand.value > player_hand.value):
            dealer_wins(chips)
        elif (dealer_hand.value > 21) and (player_hand.value <= 21):
            dealer_busts(chips)
        elif dealer_hand.value == player_hand.value:
            push(chips)

        # Inform Player of their chips total
        print("Your total chips are " + str(chips.total))

        # Ask to play again
        play_again = wanna_play_again()

        if play_again == "Y":
            if chips.total == 0:
                print("\nSorry, you ran out of chips, no chips no play, bye!")
                break
            else:
                playing = True
                continue
        else:
            break