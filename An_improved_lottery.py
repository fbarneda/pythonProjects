import random

# This line creates a set with 6 random numbers
lottery_numbers = set(random.sample(range(22), 6))

# Here are your players; find out who has the most numbers matching lottery_numbers!
players = [
    {'name': 'Rolf', 'numbers': {1, 3, 5, 7, 9, 11}},
    {'name': 'Charlie', 'numbers': {2, 7, 9, 22, 10, 5}},
    {'name': 'Anna', 'numbers': {13, 14, 15, 16, 17, 18}},
    {'name': 'Jen', 'numbers': {19, 20, 12, 7, 3, 5}}
]

max_seen = 0
numbers_matched = 0
winner = str()

for player in players:

    player_name = player["name"]
    player_numbers = player["numbers"]
    num_player_matches = int((len(player_numbers.intersection(lottery_numbers))))

    if num_player_matches > max_seen:
        max_seen = num_player_matches
        winner = player_name, num_player_matches

# The winnings are calculated with the formula:
winner_name = winner[0]
winnings = 100 ** int(winner[1])

# Then, print out a line such as "Jen won 1000.".
print("{} won {}".format(winner_name, winnings))
