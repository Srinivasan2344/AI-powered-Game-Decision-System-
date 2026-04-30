import random
from game import check_winner,is_draw,available_moves


# HARD - Minimax
def minimax(board,is_max):
    if check_winner(board,"O"):
        return 10
    if check_winner(board,"X"):
        return -10
    if is_draw(board):
        return 0

    if is_max:
        best=-1000
        for i,j in available_moves(board):
            board[i][j]="O"
            score=minimax(board,False)
            board[i][j]=" "
            best=max(best,score)
        return best
    else:
        best=1000
        for i,j in available_moves(board):
            board[i][j]="X"
            score=minimax(board,True)
            board[i][j]=" "
            best=min(best,score)
        return best


def hard_move(board):
    best_score=-1000
    best_move=None

    for i,j in available_moves(board):
        board[i][j]="O"
        score=minimax(board,False)
        board[i][j]=" "

        if score>best_score:
            best_score=score
            best_move=(i,j)

    return best_move


# EASY - random
def easy_move(board):
    return random.choice(available_moves(board))


# MEDIUM - simple heuristic
def medium_move(board):

    # try winning move
    for i,j in available_moves(board):
        board[i][j]="O"
        if check_winner(board,"O"):
            board[i][j]=" "
            return (i,j)
        board[i][j]=" "

    # block player
    for i,j in available_moves(board):
        board[i][j]="X"
        if check_winner(board,"X"):
            board[i][j]=" "
            return (i,j)
        board[i][j]=" "

    
    return random.choice(available_moves(board))