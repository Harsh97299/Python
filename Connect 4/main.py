import pygame
import numpy as np
import sys

ROWS, COLUMNS = 6, 7

board = np.zeros((ROWS, COLUMNS))
game_over = False
turn = 1

pygame.init()

BLUE, BLACK, RED, YELLOW = (0, 0, 255), (0, 0, 0), (255, 0, 0), (255, 255, 0)

SQUARESIZE = 100
WIDTH, HEIGHT = COLUMNS*SQUARESIZE, (ROWS+1)*SQUARESIZE
SIZE = (WIDTH, HEIGHT)
RADIUS = int(SQUARESIZE/2 - 5)
WINDOW = pygame.display.set_mode(SIZE)
myfont = pygame.font.SysFont('ariel', 75)


def draw_window(board):
    for r in range(1, ROWS+1):
        for c in range(COLUMNS):
            pygame.draw.rect(WINDOW, BLUE, (c*SQUARESIZE, r *
                             SQUARESIZE, SQUARESIZE, SQUARESIZE))
            if board[r-1][c] == 0:
                pygame.draw.circle(
                    WINDOW, BLACK, (c*SQUARESIZE + int(SQUARESIZE/2), r*SQUARESIZE + int(SQUARESIZE/2)), RADIUS)
            elif board[r-1][c] == 1:
                pygame.draw.circle(
                    WINDOW, RED, (c*SQUARESIZE + int(SQUARESIZE/2), r*SQUARESIZE + int(SQUARESIZE/2)), RADIUS)
            elif board[r-1][c] == 2:
                pygame.draw.circle(
                    WINDOW, YELLOW, (c*SQUARESIZE + int(SQUARESIZE/2), r*SQUARESIZE + int(SQUARESIZE/2)), RADIUS)
    pygame.display.update()


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
clock = pygame.time.Clock()
draw_window(board)
while not game_over:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        if event.type == pygame.MOUSEMOTION:
            pygame.draw.rect(WINDOW, BLACK, (0, 0, WIDTH, SQUARESIZE))
            posx = event.pos[0]
            if turn == 1:
                pygame.draw.circle(
                    WINDOW, RED, (posx, int(SQUARESIZE/2)), RADIUS)
            else:
                pygame.draw.circle(
                    WINDOW, YELLOW, (posx, int(SQUARESIZE/2)), RADIUS)
            pygame.display.update()

        if event.type == pygame.MOUSEBUTTONDOWN:
            col = int(event.pos[0]/SQUARESIZE)
            if turn == 1:
                if (check_col(board, col) == False):
                    print("Column filled try again!")
                    continue
                row = get_row(board, col)
                set_piece(board, col, row, 1)
                if didWin(board, col, row):
                    pygame.draw.rect(WINDOW, BLACK, (0, 0, WIDTH, SQUARESIZE))
                    lable = myfont.render("Player 1 WINS!!", 1, RED)
                    WINDOW.blit(lable, (40, 10))
                    print("Player 1 Win")
                    game_over = True
                turn += 1
            else:
                if (check_col(board, col) == False):
                    print("Column filled try again!")
                    continue
                row = get_row(board, col)
                set_piece(board, col, row, 2)
                if didWin(board, col, row):
                    pygame.draw.rect(WINDOW, BLACK, (0, 0, WIDTH, SQUARESIZE))
                    lable = myfont.render("Player 2 WINS!!", 1, YELLOW)
                    WINDOW.blit(lable, (40, 10))
                    print("Player 2 Win")
                    game_over = True
                turn -= 1
            draw_window(board)

            print(board)
        if game_over == True:
            pygame.time.wait(3000)
