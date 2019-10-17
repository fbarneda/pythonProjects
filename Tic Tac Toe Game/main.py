if __name__ == "__main__":

    import functions as game

    print("\nWelcome to the Tic Tac Toe Game!")

    while True:
        #Creating a board
        board = ['/',' ',' ',' ',' ',' ',' ',' ',' ',' ']
        #Randomly select what player goes first
        game.choose_first()
        #Asking the player if they want to be X or O
        marker = game.player_input()

        while True:
            #Display the board of the game
            game.display_board(board)
            #Ask to input a number 1-9
            move = game.player_select_move()
            #Check if space is empty, if it's not continue, else save the marker in board
            if not game.space_check(board, move):
                continue
            else:
                game.place_marker(board,marker,move)
            #Check if anyone has won the game and if so, break inner loop
            if game.win_check(board, marker):
                game.display_board(board)
                print("="*20 + marker + " has won." + "="*20)
                break
            #Check if the board is full, if not, change markers, if it is, it's a tie at this point
            if not game.full_board_check(board):
                if marker == "X":
                    marker = "O"
                else:
                    marker = "X"
                continue
            else:
                game.display_board(board)
                print("="*20 + " It's a TIE." + "="*20)
                break
        #Check if we replay, if yes, loop starts again, else it ends and program stops
        if not game.replay():
            break