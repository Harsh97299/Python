import pygame
import os

WIDTH, HEIGHT = 900, 500
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Test!")

WHITE = (255,255,255)
BLACK = (0, 0, 0)

BORDER = pygame.Rect(WIDTH/2 - 5, 0, 10, HEIGHT)
FPS = 60
VELOCITY = 5
BULLET_VEL = 7
SPACESHIP_WIDTH, SPACESHIP_HEIGHT = 55, 40

YELLOW_SPACESHIP_IMAGE = pygame.image.load(os.path.join('Assets','spaceship_yellow.png'))
YELLOW_SPACESHIP_IMAGE = pygame.transform.rotate(pygame.transform.scale(YELLOW_SPACESHIP_IMAGE, (SPACESHIP_WIDTH,SPACESHIP_WIDTH)), 90)
RED_SPACESHIP_IMAGE = pygame.image.load(os.path.join('Assets','spaceship_red.png'))
RED_SPACESHIP_IMAGE = pygame.transform.rotate(pygame.transform.scale(RED_SPACESHIP_IMAGE, (SPACESHIP_WIDTH,SPACESHIP_WIDTH)), 270)

def handle_yellow_movement(keys_pressed, yellow):
    if keys_pressed[pygame.K_a] and yellow.x - VELOCITY > 0: #Left
        yellow.x -= VELOCITY
    if keys_pressed[pygame.K_d] and yellow.x + VELOCITY + yellow.width < WIDTH-BORDER.x: #Right
        yellow.x += VELOCITY   
    if keys_pressed[pygame.K_w] and yellow.y - VELOCITY > -5: #Up
        yellow.y -= VELOCITY     
    if keys_pressed[pygame.K_s] and yellow.y + VELOCITY + yellow.height < HEIGHT - 7: #Down
        yellow.y += VELOCITY
def handle_red_movement(keys_pressed, red):
    if keys_pressed[pygame.K_LEFT] and red.x - VELOCITY > WIDTH - BORDER.x - 5: #Left
        red.x -= VELOCITY
    if keys_pressed[pygame.K_RIGHT] and red.x + VELOCITY + red.width < WIDTH: #Right
        red.x += VELOCITY   
    if keys_pressed[pygame.K_UP] and red.y + VELOCITY > 5: #Up
        red.y -= VELOCITY     
    if keys_pressed[pygame.K_DOWN] and red.y + VELOCITY + red.height < HEIGHT-10: #Down
        red.y += VELOCITY

def draw_window(red, yellow):
    WIN.fill(WHITE)
    pygame.draw.rect(WIN, BLACK, BORDER)
    WIN.blit(YELLOW_SPACESHIP_IMAGE, (yellow.x,yellow.y))
    WIN.blit(RED_SPACESHIP_IMAGE, (red.x,red.y))
    pygame.display.update()


def main():
    red = pygame.Rect(600, 100, SPACESHIP_WIDTH, SPACESHIP_HEIGHT)
    yellow = pygame.Rect(300, 100, SPACESHIP_WIDTH, SPACESHIP_HEIGHT)

    red_bullets = []
    yellow_bullets = []

    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False 
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LCTRL:
                    bullet = pygame.Rect()
                    yellow_bullets.append()
                
                
        keys_pressed = pygame.key.get_pressed()
        handle_yellow_movement(keys_pressed, yellow)
        handle_red_movement(keys_pressed,red)
        draw_window(red, yellow)
    pygame.quit()

if __name__ == "__main__":
    main()