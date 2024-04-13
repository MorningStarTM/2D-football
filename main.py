import pygame
import math
import random
from utils.ground import FootballGround
import sys

# Set up the screen dimensions
SCREEN_WIDTH = 64*23
SCREEN_HEIGHT = 64*12

def main():
    # Initialize Pygame
    pygame.init()


    ground = FootballGround(SCREEN_WIDTH, SCREEN_HEIGHT)
    ground.draw()

    pygame.display.flip()

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    main()
