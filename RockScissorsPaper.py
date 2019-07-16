"""
This is the Game: Rock, Scissors, Paper
"""

hand_options = {"rock": 1,"scissors": 2,"paper": 3}

class Player():

    total_win = 0
    total_lose = 0
    total_games_played = 0
    percent_wins = 0

    def __init__(self,name="Player"):

        self.name = name
        self.total_win = self.total_win
        self.total_lose = self.total_lose
        self.total_games_played = self.total_win + self.total_lose

    def add_win(self):

        self.total_win += 1
        self.total_games_played += 1

        self.percent_wins = self.total_win / self.total_games_played

    def add_lose(self):

        self.total_lose += 1
        self.total_games_played += 1

        self.percent_wins = self.total_win / self.total_games_played

    def calc_percent_wins(self,total_win,total_games_played):

        res = 100 * float(total_win)/float(total_games_played)
        print(str(res) + "%")


class Hand():

    def __init__(self):

        # self.rock =
        # self.scissors
        # self.paper
        pass

player = Player()

print(player.name)
player.add_win()
print(player.total_win)
print(player.total_lose)
print(player.total_games_played)
player.calc_percent_wins(player.total_win,player.total_games_played)
