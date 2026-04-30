from game import *
from ai import easy_move, medium_move, hard_move

board = [
[" "," "," "],
[" "," "," "],
[" "," "," "]
]

wins=0
losses=0
draws=0

print("=== AI Tic-Tac-Toe Game ===")
print("You = X | AI = O")

level=input("Choose difficulty Easy/Medium/Hard:").lower()

while True:

    print_board(board)

    row=int(input("Row (0-2): "))
    col=int(input("Col (0-2): "))

    if row not in [0,1,2] or col not in [0,1,2]:
        print("Enter only 0,1,2")
        continue

    if board[row][col]!=" ":
        print("Invalid move")
        continue


    board[row][col]="X"

    if check_winner(board,"X"):
        print_board(board)
        wins+=1
        print("You Win")
        print("Wins:",wins,"Losses:",losses,"Draws:",draws)
        break

    if is_draw(board):
        draws+=1
        print("Draw")
        print("Wins:",wins,"Losses:",losses,"Draws:",draws)
        break


    if level=="easy":
        r,c=easy_move(board)

    elif level=="medium":
        r,c=medium_move(board)

    else:
        r,c=hard_move(board)


    board[r][c]="O"

    print("AI chose:",r,c)


    if check_winner(board,"O"):
        print_board(board)
        losses+=1
        print("AI Wins")
        print("Wins:",wins,"Losses:",losses,"Draws:",draws)
        break


    
    if is_draw(board):
        draws+=1
        print("Draw")
        print("Wins:",wins,"Losses:",losses,"Draws:",draws)
        break