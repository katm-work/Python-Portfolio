#imported libraries used in the game
import pygame
import time
import random
# Defining dimensions of the window and character
WIDTH, HEIGHT = 1000, 800
CHAR_WIDTH, CHAR_HEIGHT = 40, 60
CHAR_VEL = 5
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
#displays window title and BG sets background
pygame.display.set_caption('Fun Little Dodging Game')
BG = pygame.transform.scale(pygame.image.load("assets/img/bocc.gif"), (WIDTH, HEIGHT))
# definition for what draw function does
def draw(character):
    WIN.blit(BG, (0,0))
    pygame.draw.rect(WIN, 'red', character)
   # pygame.draw.rect(WIN, 'blue', enemy)
    pygame.display.flip()
# definition for main file
def main():
    run = True
    character = pygame.Rect(200,  HEIGHT - CHAR_HEIGHT, CHAR_WIDTH, CHAR_HEIGHT)
   # enemy = pygame.Rect()
    while run == True:
        clock = pygame.time.Clock()
        clock.tick(60)
        keys = pygame.key.get_pressed()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                    run = False

        if keys[pygame.K_LEFT] and character.x > 0:
             character.x -= CHAR_VEL
        elif keys[pygame.K_RIGHT] and character.x < WIDTH - CHAR_WIDTH:
             character.x += CHAR_VEL
        draw(character)
    pygame.quit()            
if __name__ == '__main__':
    main()
