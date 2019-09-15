import functions as game
print("Welcome to the Tic Tac Toe Game!")

while True:

    board = ['#',' ',' ',' ',' ',' ',' ',' ',' ',' ']

    player = game.player_input()

    #game.choose_first()

    while True:

        game.display_board(board)

        position = game.player_choice(board)

        if game.space_check(board, position):
            game.place_marker(board,player,position)



    # position = int(input("Please enter a number"))
    # print("\n"*100)