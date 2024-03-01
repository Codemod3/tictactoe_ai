import math
import copy 

X = "X"
O = "O"
EMPTY = None

def initial_state():
  
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]

def player(board):
    countx = 0
    counto = 0
    for row in range(len(board)):
        for col in range(len(board[row])):
            if board[row][col] == X:
                countx += 1
            if board[row][col] == O:
                counto += 1
    if countx > counto:
        return O
    else:
        return X

def actions(board):
    outcomes = set()
    for row in range(len(board)):
        for col in range(len(board[0])):
            if board[row][col] == EMPTY:
                outcomes.add((row,col))
    return outcomes

def result(board, action):
    if action not in actions(board):
        raise Exception("Invalid action")
    row, col = action
    board_copy = copy.deepcopy(board)
    board_copy[row][col] = player(board)
    return board_copy

def checkrow(board,player):
    for row in range(len(board)):
        if board[row][0] == player and board[row][1] == player and board[row][2] == player:
            return True
    return False

def checkcol(board,player):
    for col in range(len(board)):
        if board[0][col] == player and board[1][col] == player and board[2][col] == player:
            return True
    return False

def checkdiag1(board,player):
    if board[0][0] == player and board[1][1] == player and board[2][2] == player:
        return True
    return False

def checkdiag2(board,player):
    if board[0][2] == player and board[1][1] == player and board[2][0] == player:
        return True
    return False

def winner(board):
    for player in [X, O]:
        if (checkrow(board, player) or checkcol(board, player) or checkdiag1(board, player) or checkdiag2(board, player)):
            return player
    return None

def checkfull(board):
    for row in range(len(board)):
        for col in range(len(board[row])):
            if board[row][col] == EMPTY:
                return False
    return True

def terminal(board):
    if winner(board) != None or checkfull(board)==True:
        return True
    return False

def utility(board):
    if winner(board) == X:
        return 1
    elif winner(board) == O:
        return -1
    else:
        return 0

def max_val(board):
    if terminal(board):
        return utility(board)
    v = -math.inf
    for action in actions(board):
        v = max(v, min_val(result(board, action)))
    return v

def min_val(board):
    if terminal(board):
        return utility(board)
    v = math.inf
    for action in actions(board):
        v = min(v, max_val(result(board, action)))
    return v

def minimax(board):
    if terminal(board):
        return None
    best_action = None
    if player(board) == X:
        v = -math.inf
        for action in actions(board):
            min_value = min_val(result(board, action))
            if min_value > v:
                v = min_value
                best_action = action
    else:
        v = math.inf
        for action in actions(board):
            max_value = max_val(result(board, action))
            if max_value < v:
                v = max_value
                best_action = action
    return best_action
