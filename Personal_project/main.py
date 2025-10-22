import pygame
from util_background import *
from util_params import *

# pygame setup
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
running = True



# make background by calling the make background function
background = make_background()

########### TESTING ZONE #################

# blit our world's image to the screen
world_background = pygame.image.load('background.png').convert()

# get the total size of our world
world_width = world_background.get_width()
world_height = world_background.get_height()

# lets set what we see on the screen at a time
screen_x = 0 
screen_y = 0


##########################################

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    
    
    # draw my background
    screen.blit(world_background,(0,0),(screen_x,screen_y,WIDTH,HEIGHT))
    # screen.blit(background,(0,0))

    # RENDER YOUR GAME HERE

    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()