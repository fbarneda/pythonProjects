import functions as game
print("\nWelcome to the Tic Tac Toe Game!\n")

while True:

    board = ['*',' ',' ',' ',' ',' ',' ',' ',' ',' ']

    marker = game.player_input()

    if marker == "X":
        player1 = "X"
        player2 = "O"
    else:
        player1 = "O"
        player2 = "X"

    while True:

        if game.full_board_check(board) == False:

            game.display_board(board)

            position = game.player_choice(board)

            if game.space_check(board, position):
                game.place_marker(board,marker,position)

            if marker == "X":
                marker = "O"

        else:
            print("Full")
            break

        # position = game.player_choice(board)
        # if position == '#':
        #     print("Already in use, choose another one.")
        # else:
        #     game.place_marker(board, player, position)
        #     game.display_board(board)

# position = int(input("Please enter a number"))
# print("\n"*100)