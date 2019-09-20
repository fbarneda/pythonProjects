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
        player = input("Please pick your marker 'X' or 'O':\n").upper()
    return player


def place_marker(board, marker, position):
    board[position] = marker


def win_check(board, mark):
    return (board[1] == mark and board[2] == mark and board[3] == mark) or (
            board[4] == mark and board[5] == mark and board[6] == mark) or (
                   board[7] == mark and board[8] == mark and board[9] == mark) or (
                   board[1] == mark and board[5] == mark and board[9] == mark) or (
                   board[3] == mark and board[5] == mark and board[7] == mark) or (
                   board[1] == mark and board[4] == mark and board[7] == mark) or (
                   board[2] == mark and board[5] == mark and board[8] == mark) or (
                   board[3] == mark and board[6] == mark and board[9] == mark)


def choose_first():
    import random
    res = random.randint(1, 11)
    if res % 2 == 0:
        res = "Player 1"
    else:
        res = "Player 2"

    print("\n" + res + " goes first!\n")


def space_check(board, pos):
    if str(board[pos]) == " ":
        return True
    else:
        return False


def full_board_check(board):
    if ' ' in board:
        return False
    else:
        return True


def player_select_move():
    while True:
        pos = input("Please enter a number: [1-9]\n")
        if pos in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
            return int(pos)


def replay():

    while True:
        res = input("\nWanna play again? [Y/N]\n").upper()
        if res[0] == 'N':
            return False
        elif res[0] == 'Y':
            return True