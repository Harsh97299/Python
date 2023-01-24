import random #for generating random num
import sys
from pip import main #we will use sys.exit to exit the game
import pygame # basic pygame imports
from pygame.locals import * 

#Global variables for the game
FPS = 32
SCREENWIDH = 289
SCREENHEIGHT = 511
SCREEN = pygame.display.set_mode((SCREENWIDH, SCREENHEIGHT))#to initialize the screen
GROUNDY = SCREENHEIGHT *0.8
GAME_SPRITES = {}
GAME_SOUNDS = {}
PLAYER = 'gallery/sprites/bird.png'
BACKGROUND = 'gallery/sprites/background.png'
PIPE = 'gallery/sprites/pipe.png'

def welcomeScreen():
    #Shows Welcome screen on the screen

    playerx = int(SCREENWIDH/5)
    playery = int((SCREENHEIGHT - GAME_SPRITES['player'].get_height())/2)
    messagex = int((SCREENWIDH - GAME_SPRITES['message'].get_width())/2)
    messagey = int((SCREENHEIGHT - GAME_SPRITES['message'].get_height())/2)
    basex = 0
    while True:
        for event in pygame.event.get():
            # if user clicks the cross button, close the game
            if event.type == QUIT or (event.type == KEYDOWN == K_ESCAPE):
                pygame.quit()
                sys.exit()
            # if user presses the space or up key, start the game for them
            elif event.type == KEYDOWN and (event.key == K_SPACE or event.key == K_UP):
                return
            else:
                SCREEN.blit(GAME_SPRITES['backgroung'],(0, 0))
                SCREEN.blit(GAME_SPRITES['player'],(playerx, playery))
                SCREEN.blit(GAME_SPRITES['message'],(messagex, messagey))
                SCREEN.blit(GAME_SPRITES['base'],(basex, GROUNDY))
                pygame.display.update()
                FPSCLOCK.tick(FPS)

    pass

if __name__ == "__main__":
    # This will be the main function from where our game will start
    pygame.init #initialize all pygame's module
    FPSCLOCK = pygame.time.Clock()
    pygame.display.set_caption('Flappy Bird')
    GAME_SPRITES['numbers'] = (
        pygame.image.load('gallery/sprites/0.png').convert_alpha(),
        pygame.image.load('gallery/sprites/1.png').convert_alpha(),
        pygame.image.load('gallery/sprites/2.png').convert_alpha(),
        pygame.image.load('gallery/sprites/3.png').convert_alpha(),
        pygame.image.load('gallery/sprites/4.png').convert_alpha(),
        pygame.image.load('gallery/sprites/5.png').convert_alpha(),
        pygame.image.load('gallery/sprites/6.png').convert_alpha(),
        pygame.image.load('gallery/sprites/7.png').convert_alpha(),
        pygame.image.load('gallery/sprites/8.png').convert_alpha(),
        pygame.image.load('gallery/sprites/9.png').convert_alpha(),
    )
    GAME_SPRITES['message'] = pygame.image.load('gallery/sprites/message.png').convert_alpha()
    GAME_SPRITES['base'] = pygame.image.load('gallery/sprites/base.png').convert_alpha()
    GAME_SPRITES['pipe'] =(
        pygame.transform.rotate(pygame.image.load(PIPE).convert_alpha(), 180),
        pygame.image.load(PIPE).convert_alpha()
    )

    #GAME SOUNDS
    pygame.mixer.init()
    GAME_SOUNDS['die'] = pygame.mixer.Sound('gallery/audio/die.wav')
    GAME_SOUNDS['hit'] = pygame.mixer.Sound('gallery/audio/hit.wav')
    GAME_SOUNDS['point'] = pygame.mixer.Sound('gallery/audio/point.wav')
    GAME_SOUNDS['swoosh'] = pygame.mixer.Sound('gallery/audio/swoosh.wav')
    GAME_SOUNDS['wing'] = pygame.mixer.Sound('gallery/audio/wing.wav')

    GAME_SPRITES['backgroung'] = pygame.image.load(BACKGROUND).convert()
    GAME_SPRITES['player'] = pygame.image.load(PLAYER).convert()
    while True:
        welcomeScreen() #Shows welcome screen to user until he presses a button
        maingame() # This is the main game function