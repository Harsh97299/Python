ROWS, COLUMNS = 6, 7

def didWin(board, col, row):
    player = board[row][col]

    # Horizontal Check
    count = 0
    for r in range(COLUMNS):
        if player == board[row][r]:
            count += 1
        else:
            count = 0
        if count >= 4:
            return True

    # Vertical Check
    count = 0
    for r in range(ROWS):
        if player == board[r][col]:
            count += 1
        else:
            count = 0
        if count >= 4:
            return True

    # Diagonal Check
    for r in range(3, 6):
        for c in range(3, 7):
            if board[r][c] == player and board[r-1][c-1] == player and board[r-2][c-2] == player and board[r-3][c-3] == player:
                return True

    for r in range(3, 6):
        for c in range(0, 4):
            if board[r][c] == player and board[r-1][c+1] == player and board[r-2][c+2] == player and board[r-3][c+3] == player:
                return True


def set_piece(board, col, row, num):
    board[row][col] = num


def check_col(board, col):
    if (board[0][col] == 0):
        return True
    else:
        return False


def get_row(board, col):
    r = ROWS-1
    while r >= 0:
        if board[r][col] == 0:
            return r
        r -= 1