import pygame
import numpy as np
import sys
from logic import *
import logic
from UI import *

COLUMNS = logic.COLUMNS
ROWS = logic.ROWS

board = np.zeros((ROWS, COLUMNS))
game_over = False
turn = 1

pygame.init()

clock = pygame.time.Clock()
draw_window(board)

while not game_over:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        if event.type == pygame.MOUSEMOTION:
            Motion(event.pos[0], turn)

        if event.type == pygame.MOUSEBUTTONDOWN:
            
            if turn == 1:
                col = int(event.pos[0]/SQUARESIZE)
                
                if (check_col(board, col) == False):
                    print("Column filled try again!")
                    continue
                row = get_row(board, col)
                set_piece(board, col, row, 1)
                if didWin(board, col, row):
                    Player1Won()
                    game_over = True
                turn += 1
            else:
                col = int(event.pos[0]/SQUARESIZE)
                if (check_col(board, col) == False):
                    print("Column filled try again!")
                    continue
                row = get_row(board, col)
                set_piece(board, col, row, 2)
                if didWin(board, col, row):
                    Player2Won()
                    game_over = True
                turn -= 1
            draw_window(board)
            print(board)
        
        if game_over == True:
            pygame.time.wait(3000)
