# ----- Global Variables -----

# game board
board = ["-", "-", "-",
         "-", "-", "-",
         "-", "-", "-",]

# If game is still going
game_still_going = True

# Who won? or Tie?
winner = None

# Who's turn is it
current_player = "X"

# ----- -----

# display board
def display_board():
    print(board[0] +  " | " + board[1] + " | " + board[2])
    print(board[3] +  " | " + board[4] + " | " + board[5])
    print(board[6] +  " | " + board[7] + " | " + board[8])


# play a game of tic tac toe
def play_game():
    # Displays initial board
    display_board()

    # while the game is still going
    while game_still_going:
        # handle a single turn of an arbitrary player
        handle_turn(current_player)
        
        # check if the game has ended
        check_if_game_over()

        # Flip to the other player
        flip_player()


# the game has ended
if winner == "X" or winner =="O":
    print = winner + " won."

elif winner == None:
    print("Tie.")


# handle a single turn of an arbitrary player
def handle_turn(current_player):
    position = input("Choose a position from 1-9: ")
    position = int(position) - 1

    board[position] = "X"
    display_board()

# check if the game is over
def check_if_game_over():
    check_for_winner()
    check_if_tie()


# check if there is a win
def check_for_winner():
    #check rows

    # check columns

    # check diagonals

    return


# check tie
def check_if_tie():
    return


# flip player
def flip_player():
    return


play_game()