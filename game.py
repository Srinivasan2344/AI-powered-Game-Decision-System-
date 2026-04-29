def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-"*9)


def check_winner(board,player):

    for row in board:
        if all(cell==player for cell in row):
            return True

    for col in range(3):
        if all(board[row][col]==player for row in range(3)):
            return True

    if all(board[i][i]==player for i in range(3)):
        return True

    if all(board[i][2-i]==player for i in range(3)):
        return True

    return False


def is_draw(board):
    return all(cell!=" " for row in board for cell in row)


def available_moves(board):
    moves=[]

    for i in range(3):
        for j in range(3):
            if board[i][j]==" ":
                moves.append((i,j))

    return moves