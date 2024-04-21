import pygame
import os  
import time
import random 
pygame.font.init()

#image
RED_SPACE_SHIP = pygame.image.load(os.path.join("pixel_ship_red_small.png"))
GREEN_SPACE_SHIP = pygame.image.load(os.path.join("pixel_ship_green_small.png"))
BLUE_SPACE_SHIP = pygame.image.load(os.path.join("pixel_ship_blue_small.png"))

#PlayerShip
YELLOW_SPACE_SHIP = pygame.image.load(os.path.join("pixel_ship_yellow.png"))

# lasers
RED_LASER = pygame.image.load(os.path.join( "pixel_laser_red.png"))
GREEN_LASER = pygame.image.load(os.path.join( "pixel_laser_green.png"))
BLUE_LASER = pygame.image.load(os.path.join( "pixel_laser_blue.png"))
YELLOW_LASER = pygame.image.load(os.path.join("pixel_laser_yellow.png"))

#Background
BG = pygame.image.load(os.path.join("background-black.png"))

def main():
    run = True
    FPS = 60
    clock = pygame.time.Clock()

    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
main()    