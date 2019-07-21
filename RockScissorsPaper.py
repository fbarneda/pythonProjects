"""
This is the Game: Rock, Scissors, Paper
"""
import random


class Player():

    total_wins = 0
    total_lose = 0
    total_tie = 0
    total_games_played = 0

    def __init__(self,name="Player"):

        self.name = name
        self.total_wins = self.total_wins
        self.total_lose = self.total_lose
        self.total_tie = self.total_tie
        self.total_games_played = self.total_wins + self.total_lose

    def add_wins(self):

        self.total_wins += 1
        self.total_games_played += 1
        print("\n-- " + player.name.capitalize() + ", you won! --\n" )

    def add_lose(self):

        self.total_lose += 1
        self.total_games_played += 1
        print("\n-- " + player.name.capitalize() + ", you lost! --\n" )

    def add_tie(self):

        self.total_tie += 1
        self.total_games_played += 1
        print("\n-- " + player.name.capitalize() + ", it is a tie! --\n" )

    def percent_wins(self):
        if self.total_games_played == 0:
            return "0 %"
        else:
            res = 100 * float(self.total_wins)/float(self.total_games_played)
            return str(round(res,3)) + " %"


class HandPlayOptions():

    def __init__(self):

        self.play_options = {'R': 'ROCK','S': 'SCISSORS','P': 'PAPER'}

    def random_play(self):

        key, values = random.choice(list(self.play_options.items()))
        return values


def player_plays():

    global playing

    while True:
        try:
            player_plays = str(input("\n" + player.name + ", please enter [R]ock or [S]cissors or [P]aper.\n"
            + "To exit press [Q]uit. \n").upper())
            if player_plays == 'Q':
                playing = False
                return playing
            elif player_plays == 'R' or player_plays == 'S'or player_plays == 'P':
                break
        except:
            print("Please enter one of the options mentioned.")

    return hand.play_options[player_plays]


def play(computer_plays,player_plays):

    if player_plays == computer_plays:
        player.add_tie()
    elif player_plays == 'ROCK' and computer_plays == 'SCISSORS':
        player.add_wins()
    elif player_plays == 'ROCK' and computer_plays == 'PAPER':
        player.add_lose()
    elif player_plays == 'SCISSORS' and computer_plays == 'ROCK':
        player.add_lose()
    elif player_plays == 'SCISSORS' and computer_plays == 'PAPER':
        player.add_wins()
    elif player_plays == 'PAPER' and computer_plays == 'ROCK':
        player.add_wins()
    elif player_plays == 'PAPER' and computer_plays == 'SCISSORS':
        player.add_lose()


def print_statistics():

    print("\n-----------------------------------------------")
    print(f"You played a total of {player.total_games_played} games")
    print(f"Games WON: {player.total_wins} games")
    print(f"Games LOST: {player.total_lose} games")
    print(f"Games TIED: {player.total_tie} games")
    print(f"You won {player.percent_wins()} of the games")
    print("-----------------------------------------------\n")


# MAIN PROGRAM STARTS HERE:

print("\nWELCOME TO THE Rock, Scissors, Paper game!\n")

player_name = input("Please enter your name here: \n")

player = Player(player_name.capitalize())
hand = HandPlayOptions()

playing = True

while playing:

    play(hand.random_play(),player_plays())

print_statistics()
print("\nThanks for playing! Bye now.")