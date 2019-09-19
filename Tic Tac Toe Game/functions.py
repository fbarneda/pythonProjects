def display_board(board):
    print("\n     |     |     \n", end='')
    print(" " + board[7] + "   |  " + board[8] + "  |   " + board[9] + "  \n", end='')
    print("     |     |     \n", end='')
    print("-" * 17 + "\n", end='')
    print("     |     |     \n", end='')
    print(" " + board[4] + "   |  " + board[5] + "  |   " + board[6] + "  \n", end='')
    print("     |     |     \n", end='')
    print("-" * 17 + "\n", end='')
    print("     |     |     \n", end='')
    print(" " + board[1] + "   |  " + board[2] + "  |   " + board[3] + "  \n", end='')
    print("     |     |     \n", end='')
    print("\n", end='')


def player_input():
    player = ''
    while not (player == "X" or player == "O"):
        player = input("Player 1: Please pick a marker 'X' or 'O':\n").upper()
    return player


def place_marker(board, marker, position):
    board[position] = marker


def win_check(board, mark):
    return (board[1] == mark and board[2] == mark and board[3] == mark) or (
            board[4] == mark and board[5] == mark and board[6] == mark) or (
                   board[7] == mark and board[8] == mark and board[9] == mark) or (
                   board[1] == mark and board[5] == mark and board[9] == mark) or (
                   board[3] == mark and board[5] == mark and board[7] == mark)


def choose_first():
    import random
    res = random.randint(1, 11)
    if res % 2 == 0:
        res = "Player 1"
    else:
        res = "Player 2"
    print("\n" + res + " goes first.")
    return res


def space_check(board, position):
    print()
    a = board[position]
    print(type(a))
    print(type(board))
    print(type(position))
    return a == ' '


def full_board_check(board):
    if ' ' in board:
        return False
    else:
        return True


def player_choice(board):
    position = int(input("Please enter a number:\n"))

    if space_check(board, position):
        return position
    else:
        return board[0]


def replay():
    playagain = ''

    while not (playagain == "yes" or playagain == "no"):
        playagain = input("Please pick a marker 'X' or 'O':\n").upper()

    if playagain[0] == 'N':
        return False
    else:
        return True
