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

def isfilled(board) :
    for i in range(len(board)-1) :
        for j in range(len(board)-1) :
            if board[i][j] != 0 :
                # 0 for filled
                return 0
    # 1 for not filled
    return 1

def print_symbole (board, x, y, player) :
    # board[x][y] == 0 means the case is empty
    if (board[x][y] == 0):
        # return who is the player n° which tell which symbol to print
        board[x][y] = player
        return player
    
    # the case is not empty, the player canot put its symbol here, will print an error msg
    else :
        return 0


def check (board, x, y, player) :
    # check the column
    win = 0

    # cases aboves for column
    i = x
    j = y
    while i < 3 :
        if board[i][j] == player :
            win += 1
        i += 1

    # cases below for column
    i = x
    j = y
    while i >=0 :
        if board[i][j] == player :
            win += 1
        i -= 1

    if win >= 3 :
        # 1 means the player won
        return 1

    # check the line
    win = 0
    # cases right for line
    i = x
    j = y
    while j < 3 :
        if board[i][j] == player :
            win += 1
        j += 1

    # cases left for line
    i = x
    j = y
    while j >= 0 :
        if board[i][j] == player :
            win += 1
        j -= 1

    if win >= 3 :
        # 1 means the player won
        return 1

    # check the diagonal
    win = 0
    # diagonal top left to bottom right
    for i in board :
        if board[i][i] == player :
            win += 1

    # diagonal bottom left to top right
    for i in reversed(board) :
        for j in board :
            if board[i][j] == player :
                win += 1

    if win >= 3 :
        # 1 means the player won
        return 1
