"""
TIC TAC TOE 2020
"""


def clear_output():
    print('\n' * 100)


def print_the_board(board):
    print(f"\n               |                 |             ")
    print(f"      {board[6]}        |        {board[7]}        |        {board[8]}    ")
    print(f"               |                 |             ")
    print(f"-" * 49)
    print(f"               |                 |             ")
    print(f"      {board[3]}        |        {board[4]}        |        {board[5]}    ")
    print(f"               |                 |             ")
    print(f"-" * 49)
    print(f"               |                 |             ")
    print(f"      {board[0]}        |        {board[1]}        |        {board[2]}    ")
    print(f"               |                 |             ")


def select_marker():
    x = ''
    while x != "X" and x != "O":
        x = input("\nPlease pick a marker 'X' or 'O': ").upper()
    return x


def save_player_input_into_board(board, mark, position):
    board[position - 1] = mark


def check_for_winner(marker):
    return board_values[0] == marker and board_values[1] == marker and board_values[2] == marker or \
           board_values[3] == marker and board_values[4] == marker and board_values[5] == marker or \
           board_values[6] == marker and board_values[7] == marker and board_values[8] == marker or \
           board_values[0] == marker and board_values[3] == marker and board_values[6] == marker or \
           board_values[1] == marker and board_values[4] == marker and board_values[7] == marker or \
           board_values[2] == marker and board_values[5] == marker and board_values[8] == marker or \
           board_values[0] == marker and board_values[4] == marker and board_values[8] == marker or \
           board_values[2] == marker and board_values[4] == marker and board_values[6] == marker


def check_if_board_full():
    for i in range(0, 9):
        if board_values[i].isspace():
            # Not full, we return False
            return False
    else:
        return True


def check_position_free(position):
    return board_values[position - 1].isspace()


def player_choose_next_position():
    while True:

        position = input(f"\n'{current_marker}', please enter a position [1-9]: ")

        if position.isnumeric() and (0 < int(position) < 10):
            position = int(position)

            if check_position_free(position):
                save_player_input_into_board(board_values, current_marker, position)
                break
            else:
                print(f"'{current_marker}', please enter a position that is free.")
                continue


def next_player_marker():
    if current_marker.upper() == "X":
        return "O"
    elif current_marker.upper() == "O":
        return "X"


def play_again():
    i = ''
    while i != "y" and i != "n":
        i = input("Do you want to play again (y/n)? ")
        i.lower()
    return i == "y"


print("\nWelcome to the Tic Toc Game 2020")

while True:

    board_values = [" ", " ", " ", " ", " ", " ", " ", " ", " "]
    current_marker = select_marker()

    while True:

        print_the_board(board_values)

        player_choose_next_position()

        if check_for_winner(current_marker):
            print_the_board(board_values)
            print("\n" + '*' * 15 + f" Player '{current_marker}' won. " + '*' * 15 + "\n")
            break
        elif check_if_board_full():
            print_the_board(board_values)
            print(f"\n" + '*' * 15 + " It is a tie. " + '*' * 15 + "\n")
            break
        else:
            current_marker = next_player_marker()

    if play_again():
        continue
    else:
        print(f"\nThanks for playing. Bye now!")
        break
