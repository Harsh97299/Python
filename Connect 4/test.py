import numpy

board = numpy.zeros((6,7))

for r in range(6):
    for c in range(7):
        print(r, c, " ", end=" "),
    
    print("\n")
player = 0
for r in range(3,6):
    for c in range(3,7):

        if board[r][c] == player and board[r-1][c-1] == player and board[r-2][c-2] == player and board[r-3][c-3] == player:
            print("Match found 1 ["+str(r)+"] ["+str(c)+"]")

for r in range(3,5):
    for c in range(0,3):
        if board[r][c] == player and board[r-1][c+1] == player and board[r-2][c+2] == player and board[r-3][c+3] == player:
            print("Match found 2 ["+str(r)+"] ["+str(c)+"]")