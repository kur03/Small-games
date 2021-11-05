# player1 => cross
# player2 => circle
# user click on case
# if case empty print symbole on case
# check for 3 align identical symboles
# if 3 align tell winner

# Variables
# borad[3][3]
# x and y are the position
# user = 1 or user = 2 for player1 and player2

from tkinter.constants import FALSE, TRUE


def isfilled(board) :
    filled = 0
    for i in range(len(board)) :
        for j in range(len(board)) :
            if board[i][j] != 0 :
                # 0 for filled
                filled += 1
    if filled == 9 :
        return True
    # 1 for not filled
    return False

def print_symbole (board, x, y, player) :
    # board[x][y] == 0 means the case is empty
    if (board[x][y] == 0):
        # return who is the player n° which tell which symbol to print
        board[x][y] = player
        return player
    
    # the case is not empty, the player canot put its symbol here, will print an error msg
    else :
        return 0


def check (board, player) :

    # check all lines
    for i in range(len(board)) :
        if(board[i][0] == board[i][1] == board[i][2] == player) :
            return player

    # check all columns
    for i in range(len(board)) :
        if(board[0][i] == board[1][i] == board[2][i] == player) :
            return player
    
    # check diagonal top left to bottom right
    if(board[0][0] == board[1][1] == board[2][2] == player) :
        return player
    
    # check diagonal bottom left to top right
    if(board[2][0] == board[1][1] == board[0][2] == player) :
        return player
    
    return 0
