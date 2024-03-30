import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up the screen dimensions
SCREEN_WIDTH = 64*23
SCREEN_HEIGHT = 64*12
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Football Game")

# Load the tile images for the grass
dark_grass_tile = pygame.image.load("assets\\DG.png").convert()
light_grass_tile = pygame.image.load("assets\\LG.png").convert()


TILE_WIDTH = 64
TILE_HEIGHT = 64


NUM_TILES_X = SCREEN_WIDTH // TILE_WIDTH
NUM_TILES_Y = SCREEN_HEIGHT // TILE_HEIGHT


running = True
for y in range(NUM_TILES_Y):
    for x in range(NUM_TILES_X):

        if (x // 2) % 2 == 0:
            screen.blit(dark_grass_tile, (x * TILE_WIDTH, y * TILE_HEIGHT))
        else:
            screen.blit(light_grass_tile, (x * TILE_WIDTH, y * TILE_HEIGHT))

pygame.draw.rect(screen, (255, 255, 255), (50, 50, SCREEN_WIDTH - 100, SCREEN_HEIGHT - 100), 2)

#keeper line
pygame.draw.rect(screen, (255, 255, 255), (50, (SCREEN_HEIGHT/2)-110, 120, 250), 2)
pygame.draw.rect(screen, (255, 255, 255), (SCREEN_WIDTH - 170, (SCREEN_HEIGHT/2)-110, 120, 250), 2)


#center circle
center_x = SCREEN_WIDTH // 2
center_y = SCREEN_HEIGHT // 2

pygame.draw.circle(screen, (255, 255, 255), (center_x, center_y), 60, 2)

#center line
pygame.draw.line(screen, (255, 255, 255), (SCREEN_WIDTH // 2, 50), (SCREEN_WIDTH // 2, SCREEN_HEIGHT-50), 2)

#goal post
pygame.draw.rect(screen, (255, 255, 255), (0, (SCREEN_HEIGHT/2)-60, 50, 150))
pygame.draw.rect(screen, (255, 255, 255), (SCREEN_WIDTH - 50, (SCREEN_HEIGHT/2)-60, 50, 150))


pygame.display.flip()


while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


pygame.quit()
sys.exit()
