import functions as game
print("\nWelcome to the Tic Tac Toe Game!\n")

while True:
    board = ['/',' ',' ',' ',' ',' ',' ',' ',' ',' ']
    marker = game.player_input()

    if marker == "X":
        player1 = "X"
        player2 = "O"
    else:
        player1 = "O"
        player2 = "X"

    while True:

        game.display_board(board)

        move = game.player_select_move()

        if not game.space_check(board, move):
            continue
        else:
            game.place_marker(board,marker,move)

        if game.win_check(board, marker):
            game.display_board(board)
            print("="*20 + marker + " has won." + "="*20)
            break

        if not game.full_board_check(board):
            if marker == "X":
                marker = "O"
            else:
                marker = "X"
            continue
        else:
            break

    res = input("Wanna play again?\n").upper()

    if res == "Y":
        continue
    else:
        break