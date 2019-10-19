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


x = Card('Hearts', 'Two', 2)

print(x)
print("*" * 50)


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
        out = self.my_deck_of_52_cards[0]
        self.my_deck_of_52_cards.pop(0)
        return out


mydeck = Deck()
print(mydeck)
print("*" * 50)

mycard = mydeck.deal()
print(mycard)
print("*" * 50)


class Hand:

    def __init__(self):

        self.cards = []
        self.value = 0
        self.aces = 0

    def __str__(self):

        string = ""
        for card in self.cards:
            string += (card.card_rank + " of " + card.card_suit + ", value " + str(card.card_value) + "\n")
        return string

    def add_card(self, card):

        self.cards.append(card)
        self.value += card.card_value
        if card.card_value == 11:
            self.aces += 1
        print("FYI. Added " + str(card.card_value) + " to Hand value")

        Hand.adjust_for_ace(self)

        print("FYI. Total value of Hand is " + str(self.value))

    def adjust_for_ace(self):
        # Aces will never be higher than 1, since we are checking the value in every card_add
        if self.value > 21 and self.aces == 1:
            self.value -= 10
            self.aces = 0


myhand = Hand()
while myhand.value <= 21:
    myhand.add_card(mydeck.deal())
    print('\n')
    print(myhand)
    print("=" * 50)
print("*" * 50)
