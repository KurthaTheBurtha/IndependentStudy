#Copy your code from Complete the Game or Tic Tac Toe with Random NPC
#Then copy your completed minimax from Getting the Row Col Values
board = []


##Copy your check_tie and check_win functions from the previous lesson
# and any other function needed for those functions to work.
def is_valid_move(row, col):
    if row > 2 or col > 2 or board[row][col] != '-':
        print("Please enter a valid move")
        return False
    return True


def check_col_win(player):
    for i in range(3):
        if board[0][i] == player and board[1][i] == player and board[2][i] == player:
            return True
    return False


def check_row_win(player):
    for i in range(3):
        if board[i][0] == player and board[i][1] == player and board[i][2] == player:
            return True
    return False


def check_diag_win(player):
    if board[0][0] == player and board[1][1] == player and board[2][2] == player:
        return True
    if board[2][0] == player and board[1][1] == player and board[0][2] == player:
        return True
    return False


def check_win(player):
    if check_row_win(player) or check_diag_win(player) or check_col_win(player):
        return True
    return False


def check_tie():
    filled = True
    for i in range(3):
        for j in range(3):
            if (board[i][j] == "-"):
                filled = False
    if check_win("X") or check_win("O"):
        return False
    if filled:
        return True
    return False


##Copy over your place_player function
def place_player(player, row, col):
    if is_valid_move(row, col):
        board[row][col] = player


def hard_place_player(player, row, col):
    board[row][col] = player


def minimax(player):
    global optimalRow
    global optimalCol
    optimalRow = -1
    optimalCol = -1
    # copy your basecase here:
    if check_win("O"):
        return (10, None, None)
    elif check_win("X"):
        return (-10, None, None)
    elif check_tie():
        return (0, None, None)

    # implement recursive case
    if player == "O":
        best = -1000
        for row in range(3):
            for col in range(3):
                if board[row][col] == "-":
                    place_player("O", row, col)
                    best = max(best, minimax("X")[0])
                    optimalRow = row
                    optimalCol = col
                    hard_place_player("-", row, col)
        return (best, optimalRow, optimalCol)
    if player == "X":
        worst = 1000
        for row in range(3):
            for col in range(3):
                if board[row][col] == "-":
                    place_player("X", row, col)
                    worst = min(worst, minimax("O")[0])
                    optimalRow = row
                    optimalCol = col
                    hard_place_player("-", row, col)
        return (worst, optimalRow, optimalCol)


##Don't edit this code
# It check to see if your minimax function is working correctly
# When the code is executed, the console should print 10, 0, -10
def print_board():
    print("\n")
    print("\t0\t\t1\t\t2")
    count = 0
    for item in board:
        row = ""
        for space in item:
            row += "\t" + space + "\t"
        print(count, row + "\n")
        count += 1


##Copy your check_tie and check_win functions from the previous lesson
# and any other function needed for those functions to work.
def is_valid_move(row, col):
    if int(row) > 2 or int(col) > 2 or board[row][col] != '-':
        print("Please enter a valid move")
        return False
    return True


def check_col_win(player):
    for i in range(3):
        if board[0][i] == player and board[1][i] == player and board[2][i] == player:
            return True
    return False


def check_row_win(player):
    for i in range(3):
        if board[i][0] == player and board[i][1] == player and board[i][2] == player:
            return True
    return False


def check_diag_win(player):
    if board[0][0] == player and board[1][1] == player and board[2][2] == player:
        return True
    if board[2][0] == player and board[1][1] == player and board[0][2] == player:
        return True
    return False


def check_win(player):
    if check_row_win(player) or check_diag_win(player) or check_col_win(player):
        return True
    return False


def check_tie():
    filled = True
    for i in range(3):
        for j in range(3):
            if (board[i][j] == "-"):
                filled = False
    if check_win("X") or check_win("O"):
        return False
    if filled:
        return True
    return False


##Copy over your place_player function
def place_player(player, row, col):
    if is_valid_move(row, col):
        board[row][col] = player


def hard_place_player(player, row, col):
    board[row][col] = player

global optimalRow
global optimalCol
optimalRow = -1
optimalCol = -1
def minimax(player,depth,alpha,beta):
    # copy your basecase here:
    if check_win("O"):
        return (10, None, None)
    elif check_win("X"):
        return (-10, None, None)
    elif check_tie() or depth ==0:
        return (0, None, None)

    # implement recursive case
    if player == "O":
        best = -1000
        for row in range(3):
            for col in range(3):
                if board[row][col] == "-":
                    place_player("O", row, col)
                    prevbest = best
                    best = max(best, minimax("X",depth-1,alpha,beta)[0])
                    alpha = max(alpha,best)
                    if alpha>=beta:
                        break
                    if not prevbest == best:
                        optimalRow = row
                        optimalCol = col
                    hard_place_player("-", row, col)
        return best, optimalRow, optimalCol
    if player == "X":
        worst = 1000
        for row in range(3):
            for col in range(3):
                if board[row][col] == "-":
                    place_player("X", row, col)
                    prevworst = worst
                    worst = min(worst, minimax("O",depth-1,alpha,beta)[0])
                    beta = min(alpha,worst)
                    if beta<=alpha:
                        break
                    if not prevworst == worst:
                        optimalRow = row
                        optimalCol = col
                    hard_place_player("-", row, col)
        return worst, optimalRow, optimalCol


def take_turn(player):
    print(player + " \'s Turn")
    row = input("Enter a row ")
    col = input("Enter a col ")
    while is_valid_move(int(row), int(col)) == False:
        row = input("Enter a row ")
        col = input("Enter a col ")
    place_player(player, int(row), int(col))


def print_board():
    print("\n")
    print("\t0\t\t1\t\t2")
    count = 0
    for item in board:
        row = ""
        for space in item:
            row += "\t" + space + "\t"
        print(count, row + "\n")
        count += 1


for i in range(3):
    board.append(['-', '-', '-'])
print("Welcome to Tic Tac Toe!")
print()
print_board()
turns = 0
while not check_tie() and not check_win("O") and not check_win("X"):
    take_turn("X")
    if check_tie() or check_win("X") or check_win("O"):
        break
    score, orow, ocol = minimax("O",4,-1000,1000)
    place_player("O", orow, ocol)
    print_board()

winner = ""
if check_tie():
    print("It's a tie!")
else:
    if check_win("X"):
        winner = "X"
    elif check_win("O"):
        winner = "O"
    print(winner + " wins!")
print_board()