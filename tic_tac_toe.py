import time
# the computer (i.e., your program) should play the game using 'X's;
# the user (e.g., you) should play the game using 'O's;
# the first move belongs to the computer − it always puts its first 'X' in the middle of the board;
# all the squares are numbered row by row starting with 1 (see the example session below for reference)
# the user inputs their move by entering the number of the square they choose −
# the number must be val1id, i.e., it must be an integer, it must be greater than 0 and less than 10, and it cannot point to a field which is already occupied;
# the program checks if the game is over − there are four possible verdicts: the game should continue, the game ends with a tie, you win, or the computer wins;
# the computer responds with its move and the check is repeated;
# don't implement any form of artificial intelligence − a random field choice made by the computer is good enough for the game.
# Requirements:
# the board should be stored as a three-element list, while each element is another three-element list (the inner lists represent rows)
# so that all of the squares may be accessed using the following syntax:
# board[row][column]
def display_board(board):
    print(f"""
+-------+-------+-------+
|       |       |       |
|   {board[0][0]}   |   {board[0][1]}   |   {board[0][2]}   |
|       |       |       |
+-------+-------+-------+
|       |       |       |
|   {board[1][0]}   |   {board[1][1]}   |   {board[1][2]}   |
|       |       |       |
+-------+-------+-------+
|       |       |       |
|   {board[2][0]}   |   {board[2][1]}   |   {board[2][2]}   |
|       |       |       |
+-------+-------+-------+
    """)


#     I wanna own this bruh.
def enter_move(board):
    # The function accepts the board's current status, asks the user about their move,
    # checks the input, and updates the board according to the user's decision.
    user_move = int(input("Your move: "))
    if user_move == 1:
        board[0][0] = 'O'
    elif user_move == 2:
        board[0][1] = 'O'
    elif user_move == 3:
        board[0][2] = 'O'
    elif user_move == 4:
        board[1][0] = 'O'
    elif user_move == 5:
        board[1][1] = 'O'
    elif user_move == 6:
        board[1][2] = 'O'
    elif user_move == 7:
        board[2][0] = 'O'
    elif user_move == 8:
        board[2][1] = 'O'
    elif user_move == 9:
        board[2][2] = 'O'
    return board

def make_list_of_free_fields(board):
    # The function browses the board and builds a list of all the free squares;
    # the list consists of tuples, while each tuple is a pair of row and column numbers.
    pass
def victory_for(board):
    # The function analyzes the board's status in order to check if
    # the player using 'O's or 'X's has won the game
    # Verify Horizontal O's
    if all([z=='O' for z in board[0]]) or all([z=='O' for z in board[1]]) or all([z=='O' for z in board[2]]):
        return True
    # Verify Vertical O's
    elif all([z[0] == 'O' for z in board]) or all([z[1] == 'O' for z in board]) or all([z[2] == 'O' for z in board]):
        return True
    # Verify Diagonal O's
    elif (board[0][0] == 'O' and board[1][1] == 'O' and board[2][2] == 'O'):
        return True
    elif (board[0][2] == 'O' and board[1][1] == 'O' and board[2][0] == 'O'):
        return True
    # Verify Horizontal X's
    elif all([z == 'X' for z in board[0]]) or all([z == 'X' for z in board[1]]) or all([z == 'X' for z in board[2]]):
        return True
    # Verify Vertical X's
    elif all([z[0] == 'X' for z in board]) or all([z[1] == 'X' for z in board]) or all([z[2] == 'X' for z in board]):
        return True
    # Verify Diagonal X's
    elif (board[0][0] == 'X' and board[1][1] == 'X' and board[2][2] == 'X'):
        return True
    elif (board[0][2] == 'X' and board[1][1] == 'X' and board[2][0] == 'X'):
        return True
    return False

def draw_move(board):
    # The function draws the computer's move and updates the board.
    user_move = int(input("Computer's move: "))
    if user_move == 1:
        board[0][0] = 'X'
    elif user_move == 2:
        board[0][1] = 'X'
    elif user_move == 3:
        board[0][2] = 'X'
    elif user_move == 4:
        board[1][0] = 'X'
    elif user_move == 5:
        board[1][1] = 'X'
    elif user_move == 6:
        board[1][2] = 'X'
    elif user_move == 7:
        board[2][0] = 'X'
    elif user_move == 8:
        board[2][1] = 'X'
    elif user_move == 9:
        board[2][2] = 'X'
    return board

board = [[1, 2, 3],
         [4, 'X', 6],
         [7, 8, 9]]

display_board(board)

while True:
    board = enter_move(board)
    display_board(board)
    win = victory_for(board)
    if win == True:
        break
    board = draw_move(board)
    display_board(board)
    win = victory_for(board)
    if win == True:
        break

# Verify input is valid
    # 1 - 9
    # A number that has not been clicked
#

