
import pygame
import logic
import sys

pygame.init()
COLUMNS = logic.COLUMNS
ROWS = logic.ROWS

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

def Player1Won():
    pygame.draw.rect(WINDOW, BLACK, (0, 0, WIDTH, SQUARESIZE))
    lable = myfont.render("Player 1 WINS!!", 1, RED)
    WINDOW.blit(lable, (40, 10))
    print("Player 1 Win")

def Player2Won():
    pygame.draw.rect(WINDOW, BLACK, (0, 0, WIDTH, SQUARESIZE))
    lable = myfont.render("Player 2 WINS!!", 1, YELLOW)
    WINDOW.blit(lable, (40, 10))
    print("Player 2 Win")

def Motion(posx, turn):
    pygame.draw.rect(WINDOW, BLACK, (0, 0, WIDTH, SQUARESIZE))
    if turn == 1:
        pygame.draw.circle(WINDOW, RED, (posx, int(SQUARESIZE/2)), RADIUS)
    else:
        pygame.draw.circle(WINDOW, YELLOW, (posx, int(SQUARESIZE/2)), RADIUS)
    pygame.display.update()