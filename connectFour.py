from browser import timer
import random

# Creates a game board and adds it to the canvas
canvas_board = Rectangle(400, 300)
canvas_board.set_position(0, get_height() / 5)
canvas_board.set_color(Color.blue)
player_buffer = 5
player_radius = ((canvas_board.height - (player_buffer * 7)) / 6) / 2
# Global Variable
board = []
player = "red"


# Creates a circle that is placed on the canvas at the specified x, y coordinate
def make_player(x, y, color):
    player = Circle(player_radius)
    player.set_position(x, y)
    player.set_color(color)
    add(player)


# Adds numbers to the top of each column
def add_col_nums():
    starting_x = player_radius * 2
    for num in range(7):
        number = Text(num)
        number.set_position(starting_x - player_buffer, get_height() / 5 - player_buffer)
        add(number)
        starting_x += player_radius * 2 + player_buffer


# creates the initial game board for connect four
def make_board():
    for i in range(6):
        board.append(["-", "-", "-", "-", "-", "-", "-"])


# Iterates through game board and places circles on canvas based on the current board
def add_curr_players():
    starting_x = player_radius * 2 + player_buffer
    starting_y = get_height() / 5 + player_buffer + player_radius
    for row in range(len(board)):
        for col in range(len(board[0])):
            if board[row][col] == "-":
                make_player(starting_x, starting_y, Color.white)
            elif board[row][col] == "red":
                make_player(starting_x, starting_y, Color.red)
            else:
                make_player(starting_x, starting_y, Color.black)
            starting_x += (player_radius * 2) + player_buffer
        starting_x = player_radius * 2 + player_buffer
        starting_y += (player_radius * 2) + player_buffer


# returns true if a row,col move is a valid move on the current board
def is_valid_move(col):
    if (col >= len(board[0])) or col < 0:
        return False
    return check_column_depth(col) != - 1


# checks to see which row a player should be placed at
# players should be placed at the lowest possible row
def check_column_depth(col):
    for i in range(6):
        if (board[i][col]) != "-":
            return i - 1
    return 5


# places a player at the specified row and col
def place_player(player, row, col):
    board[row][col] = player


# Gets move from player and places that move on the board. If player is red, ask for their move
# if player is black, call minimax
def take_turn(player):
    print(player, "'s Turn")
    if player == "red":
        # try statement makes sure input is only numerical values.
        try:
            col = int(input("Enter a col "))
        except:
            col = -1
        while (not is_valid_move(col)):
            print("Please enter a valid move")
            try:
                # try statement makes sure input is only numerical values.
                col = int(input("Enter a col "))
            except:
                col = -1
            if col == "":
                return
        row = check_column_depth(col)
    else:
        # returns the optimal row, col for a given move
        score, row, col = minimax("black", 4, -100000, 100000)
    place_player(player, row, col)
    add_curr_players()


# returns true if player has won horizontally
def check_row_winner(player):
    streak = 0
    for row in range(len(board)):
        for col in range(len(board[row]) - 1):
            if board[row][col] == player and board[row][col] == board[row][col + 1]:
                streak += 1
            else:
                streak = 0
            if streak == 3:
                return True
        streak = 0
    return False


# returns true if player has won vertically
def check_col_winner(player):
    streak = 0
    for row in range(7):
        for col in range(5):
            if board[col][row] == player and board[col][row] == board[col + 1][row]:
                streak += 1
            else:
                streak = 0
            if streak == 3:
                return True
        streak = 0
    return False


# returns true if player has won diagonally
# iterates through all values on board - the try/except statements catch errors
def check_diag_winner(player):
    for row in range(len(board)):
        for col in range(len(board[0])):
            try:
                if board[row][col] == player and board[row + 1][col + 1] == player and board[row + 2][
                    col + 2] == player and board[row + 3][col + 3] == player:
                    return True
                if board[row][col] == player and board[row + 1][col - 1] == player and board[row + 2][
                    col - 2] == player and board[row + 3][col - 3] == player and col - 3 >= 0:
                    return True
            except IndexError:
                try:
                    if board[row][col] == player and board[row + 1][col - 1] == player and board[row + 2][
                        col - 2] == player and board[row + 3][col - 3] == player and col - 3 >= 0:
                        return True
                except IndexError:
                    next
                next
    return False


# returns true if player has won in any way
def check_win(player):
    return check_diag_winner(player) or check_col_winner(player) or check_row_winner(player)


# returns true if there are moves left in the game
def check_moves_left():
    for list in board:
        if "-" in list:
            return True
    return False


# prints result after the game is over
def check_results():
    if check_win("black"):

        print("Black Wins!")
    elif check_win("red"):

        print("Red Wins!")
    else:
        print("It's a Tie!")


#########The following functions are used to help compute the current score of the game.###############
# You do NOT need to know how these functions work. Each function is checking to see if
# a player has three in a row, two in a row, and one in a row. Each of those states is valuable
# for a player, and goes into the optimal move."""

def check_three_row(player):
    streak = 0
    total_threes = 0
    for row in range(len(board)):
        for col in range(len(board[row]) - 1):
            if board[row][col] == player and board[row][col] == board[row][col + 1]:
                streak += 1
            else:
                streak = 0
            try:
                if (streak == 2 and board[row][col + 1] == "-") or (
                        streak == 2 and board[row][col - streak - 1] == "-"):
                    total_threes += 1
            except:
                next
    return total_threes


def check_three_col(player):
    streak = 0
    total_threes = 0

    for row in range(7):
        for col in range(5):
            if board[col][row] == player and board[col][row] == board[col + 1][row]:
                streak += 1
            else:
                streak = 0
            try:
                if (streak == 2 and board[col + 1][row] == "-") or (
                        streak == 2 and board[col - streak - 1][row] == "-"):
                    total_threes += 1
            except:
                next
    return total_threes


def check_three_diag(player):
    total_threes = 0
    for row in range(len(board)):
        for col in range(len(board[0])):
            try:
                if board[row][col] == player and board[row + 1][col + 1] == player and board[row + 2][
                    col + 2] == player and board[row + 3][col + 3] == "-":
                    total_threes += 1
                if board[row][col] == player and board[row + 1][col - 1] == player and board[row + 2][
                    col - 2] == player and board[row + 3][col - 3] == "-":
                    total_threes += 1
                if board[row][col] == player and board[row + 1][col - 1] == player and board[row + 2][
                    col - 2] == player and board[row - 1][col + 1] == "-":
                    total_threes += 1
                if board[row][col] == player and board[row + 1][col + 1] == player and board[row + 2][
                    col + 2] == player and board[row - 1][col - 1] == "-":
                    total_threes += 1
            except IndexError:
                try:
                    if board[row][col] == player and board[row + 1][col - 1] == player and board[row + 2][
                        col - 2] == player and board[row + 3][col - 3] == "-":
                        total_threes += 1
                except:
                    try:
                        if board[row][col] == player and board[row + 1][col - 1] == player and board[row + 2][
                            col - 2] == player and board[row - 1][col + 1] == "-":
                            total_threes += 1
                    except:
                        try:
                            if board[row][col] == player and board[row + 1][col + 1] == player and board[row + 2][
                                col + 2] == player and board[row - 1][col - 1] == "-":
                                total_threes += 1
                        except:
                            next
                next
    return total_threes


def check_two_row(player):
    streak = 0
    total_twos = 0
    for row in range(len(board)):
        for col in range(len(board[row]) - 1):
            if board[row][col] == player and board[row][col] == board[row][col + 1]:
                streak += 1
            else:
                streak = 0
            try:
                if (streak == 1 and board[row][col + 1] == "-") or (
                        streak == 1 and board[row][col - streak - 1] == "-"):
                    total_twos += 1
            except:
                next
    return total_twos


def check_two_col(player):
    streak = 0
    total_two = 0

    for row in range(7):
        for col in range(5):
            if board[col][row] == player and board[col][row] == board[col + 1][row]:
                streak += 1
            else:
                streak = 0
            try:
                if (streak == 1 and board[col + 1][row] == "-") or (
                        streak == 1 and board[col - streak - 1][row] == "-"):
                    total_two += 1
            except:
                next
    return total_two


def check_two_diag(player):
    total_two = 0
    for row in range(len(board)):
        for col in range(len(board[0])):
            try:
                if board[row][col] == player and board[row + 1][col + 1] == player and board[row + 2][col + 2] == "-":
                    total_two += 1
                if board[row][col] == player and board[row + 1][col - 1] == player and board[row + 2][col - 2] == "-":
                    total_two += 1
                if board[row][col] == player and board[row + 1][col - 1] == player and board[row + 2][col - 2] == "-":
                    total_two += 1
                if board[row][col] == player and board[row + 1][col + 1] == player and board[row + 2][col + 2] == "-":
                    total_two += 1
            except IndexError:
                try:
                    if board[row][col] == player and board[row + 1][col - 1] == player and board[row + 2][
                        col - 2] == "-":
                        total_two += 1
                except:
                    try:
                        if board[row][col] == player and board[row + 1][col - 1] == player and board[row + 2][
                            col - 2] == "-":
                            total_two += 1
                    except:
                        try:
                            if board[row][col] == player and board[row + 1][col + 1] == player and board[row + 2][
                                col + 2] == "-":
                                total_two += 1
                        except:
                            next
                next
    return total_two


def check_one_row(player):
    total_ones = 0
    for row in range(len(board)):
        for col in range(len(board[row]) - 1):
            try:
                if (board[row][col] == player and board[row][col + 1] == "-" and board[row][col - 1] == "-"):
                    total_ones += 1
            except:
                next
    return total_ones


def check_one_col(player):
    total_ones = 0
    for row in range(7):
        for col in range(5):
            try:
                if (board[col][row] == player and board[col + 1][row] == "-" and board[col - 1][row] == "-"):
                    total_ones += 1
            except:
                next
    return total_ones


def check_one_diag(player):
    total_one = 0
    for row in range(len(board)):
        for col in range(len(board[0])):
            try:
                if board[row][col] == player and board[row + 1][col + 1] == "-" and board[row - 1][col - 1] == "-":
                    total_one += 1

                if board[row][col] == player and board[row + 1][col - 1] == player and board[row - 1][col + 1] == "-":
                    total_one += 1
            except IndexError:
                # try:
                #   if board[row][col] == player and board[row - 1][col-1] == player and board[row - 2][col-2] == player and board[row - 3][col-3] == player:
                #     return True
                # except IndexError:
                #     pass
                next
    return total_one


def check_three_total(player):
    return (check_three_col(player) + check_three_row(player) + check_three_diag(player)) * 50


def check_two_total(player):
    return (check_two_col(player) + check_two_row(player) + check_two_diag(player)) * 20


def check_one_total(player):
    return (check_one_col(player) + check_one_row(player) + check_one_diag(player)) * 7


###############End of functions used to compute the current score.######################

# returns the current score of the game board. Compares the number of open black winning move
# to the number of red winning moves. This function should be used in minimax!
def check_curr_score():
    return check_three_total("black") + check_two_total("black") + check_one_total("black") - check_two_total(
        "red") - check_three_total("red") - check_one_total("red")


# Implement minimax with depth and alpha beta pruning.
# returns a score, row and col value.
global optimalRow
global optimalCol
optimalRow = -1
optimalCol = -1
def minimax(player, depth, alpha, beta):
    #base case
    if check_win("black"):
        return (10,None,None)
    elif check_win("red"):
        return (-10,None,None)
    elif depth==0 or check_moves_left()==0:
        return(check_curr_score(),None,None)

    #recursive case
    if player == "black":
        best = -1000
        for col in range(7):
            if board[check_column_depth()][col] == "-":
                place_player("black",check_column_depth(),col)
                prevbest = best
                best = max(best, minimax("red",depth-1,alpha,beta))
                alpha = max(alpha,best)
                if alpha>=beta:
                    break
                if not prevbest == best:
                    optimalRow = check_column_depth(col)-1
                    optimalCol = col
                place_player("-",check_row_winner(col)-1,col)
        return best, optimalRow,optimalCol
        if player == "red":
            worst = 1000
            for col in range(7):
                if board[check_column_depth()][col] == "-":
                    place_player("red", check_column_depth(), col)
                    prevworst = worst
                    worst = min(worst, minimax("red", depth - 1, alpha, beta))
                    beta = min(beta, worst)
                    if beta <= alpha:
                        break
                    if not prevworst == worst:
                        optimalRow = check_column_depth(col) - 1
                        optimalCol = col
                    place_player("-", check_row_winner(col) - 1, col)
            return worst, optimalRow, optimalCol


# starts the game!
def play_game():
    global player
    add_curr_players()
    take_turn(player)
    if player == "red":
        player = "black"
    else:
        player = "red"
    if not check_win("black") and not check_win("red") and check_moves_left():
        print("Next Move...")
        # timer is used to delay the start of the next move. This is necessary for
        # the graphics to work.
        timer.set_timeout(play_game, 100)
    else:
        check_results()
        add_curr_players()


add(canvas_board)
make_board()
add_col_nums()
add_curr_players()
# timer is used to delay the start of the next move. This is necessary for
# the graphics to work.
timer.set_timeout(play_game, 100)
