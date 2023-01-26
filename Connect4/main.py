import pygame
import numpy as np
import sys
from logic import *
import logic

COLUMNS = logic.COLUMNS
ROWS = logic.ROWS

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
            pygame.draw.rect(WINDOW, BLUE, (c*SQUARESIZE, r * SQUARESIZE, SQUARESIZE, SQUARESIZE))
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
                pygame.draw.circle(WINDOW, RED, (posx, int(SQUARESIZE/2)), RADIUS)
            else:
                pygame.draw.circle(WINDOW, YELLOW, (posx, int(SQUARESIZE/2)), RADIUS)
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
