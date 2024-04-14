import pygame
import math
import random
from utils.ground import FootballGround
from utils.keeper import GoalKeeper
import sys

# Set up the screen dimensions
SCREEN_WIDTH = 64*23
SCREEN_HEIGHT = 64*12

def main():
    # Initialize Pygame
    pygame.init()

    ground = FootballGround(SCREEN_WIDTH, SCREEN_HEIGHT)
    keeper = GoalKeeper()

    screen = ground.screen

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        keys = pygame.key.get_pressed()

        # Check if the right arrow key is held down
        if keys[pygame.K_RIGHT]:
            current_direction = "right"
            keeper.update_position(current_direction)
            keeper.update_image_index()
        if keys[pygame.K_LEFT]:
            current_direction = "left"
            keeper.update_position(current_direction)
            keeper.update_image_index()
        if keys[pygame.K_DOWN]:
            current_direction = "down"
            keeper.update_position(current_direction)
            keeper.update_image_index()
        if keys[pygame.K_UP]:
            current_direction = "up"
            keeper.update_position(current_direction)
            keeper.update_image_index()
        # Clear the screen
        screen.fill((0, 0, 0))

        # Draw the football ground
        ground.draw()
        keeper.draw(screen)
                
                #keeper.update_image_index()
                #keeper.update_position(keeper.current_direction)
        

        # Update the display
        pygame.display.flip()

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()