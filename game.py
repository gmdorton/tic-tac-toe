# ----- Global Variables (sets a starting point) -----

# game board
board = ["-", "-", "-",
         "-", "-", "-",
         "-", "-", "-"]

# If game is still going
game_still_going = True

# Who won? or Tie?
winner = None

# Who's turn is it
current_player = "X"

# ----- End Global Variables-----

# display board
def display_board():
    print(board[0] +  " | " + board[1] + " | " + board[2] + "    " + " 1 | 2 | 3 ")
    print(board[3] +  " | " + board[4] + " | " + board[5] + "    " + " 4 | 5 | 6 ")
    print(board[6] +  " | " + board[7] + " | " + board[8] + "    " + " 7 | 8 | 9 ")


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
            print(winner + " won.")

    elif winner == None:
            print("Tie.")


# handle a single turn of an arbitrary player
def handle_turn(player):
    # tells who's turn it is
    print(player + "'s turn")
    # instructs player what to do
    position = input("Choose a position from 1-9: ")
    valid = False
    while not valid:
        # Prevents player from putting an invalid number (position)
        while position not in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
            position = input("Choose a position from 1-9: ")

        position = int(position) - 1

        # Prevents the player from over writing another player position
        if board[position] == "-":
            valid = True
        else:
            print("You can't go there. Pick again.")

    board[position] = player

    display_board()


# check if the game is over
def check_if_game_over():
    check_for_winner()
    check_if_tie()


# check if there is a win
def check_for_winner():
    # set global variables
    global winner
    # check rows
    row_winner = check_rows()
    # check columns
    column_winner = check_columns()
    # check diagonals
    diagonal_winner = check_diagonals()

    if row_winner:
        winner = row_winner
    elif column_winner:
       winner = column_winner
    elif diagonal_winner:
        winner = diagonal_winner
    else:
        winner = None

    return


def check_rows():
    # set up global variables
    global game_still_going
    # check rows for 3 of the same mark and is not empty
    row_1 = board[0] == board[1] == board[2] != "-" 
    row_2 = board[3] == board[4] == board[5] != "-"
    row_3 = board[6] == board[7] == board[8] != "-"
    # if any rows match, flag that there is a win
    if row_1 or row_2 or row_3:
        game_still_going = False
    
    #returns the Winner (X or O)
    if row_1:
            return board[0]
    elif row_2:
            return board[3]
    elif row_3:
            return board[6]
    return


def check_columns():
    # set up global variables
    global game_still_going
    # check columns for 3 of the same mark and is not empty
    column_1 = board[0] == board[3] == board[6] != "-" 
    column_2 = board[1] == board[4] == board[7] != "-"
    column_3 = board[2] == board[5] == board[8] != "-"
    # if any columns match, flag that there is a win
    if column_1 or column_2 or column_3:
        game_still_going = False
    
    #returns the Winner (X or O)
    if column_1:
            return board[0]
    elif column_2:
            return board[1]
    elif column_3:
            return board[2]
    return


def check_diagonals():
   # set up global variables
    global game_still_going
    # check diagonals for 3 of the same mark and is not empty
    diagonal_1 = board[0] == board[4] == board[8] != "-" 
    diagonal_2 = board[2] == board[4] == board[6] != "-"
    # if any diagonals match, flag that there is a win
    if diagonal_1 or diagonal_2:
        game_still_going = False
    
    #returns the Winner (X or O)
    if diagonal_1:
            return board[0]
    elif diagonal_2:
            return board[2]
    return


# check tie
def check_if_tie():
    # defining the global varriant
    global game_still_going

    if "-" not in board:
        game_still_going = False
    return


# flip player
def flip_player():
    # defining global variable
    global current_player
    # if the current player is X, then it changes to O
    if current_player == "X":
        current_player = "O"
    # if the Current player is O, then it changes to X
    elif current_player == "O":
        current_player = "X"
    return


play_game()