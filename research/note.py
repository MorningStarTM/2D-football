import pygame
import sys

# Initialize Pygame
pygame.init()

# Set screen dimensions
SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Running Animation")

# Load images
image1 = pygame.image.load("assets\\player_idle_right.png")
image2 = pygame.image.load("assets\\player_right_1.png")
image3 = pygame.image.load("assets\\player_right_2.png")
image4 = pygame.image.load("assets\\player_idle_down.png")
image5 = pygame.image.load("assets\\player_down_1.png")
image6 = pygame.image.load("assets\\player_down_2.png")

# Create a list of images
images_right = [image1, image2, image3]
images_down = [image4, image5, image6]

# Set initial image index for running right and running down
current_image_index_right = 0
current_image_index_down = 0

# Set initial position for the images
image_x, image_y = 0, SCREEN_HEIGHT // 2

# Set animation speed
animation_speed = 5
clock = pygame.time.Clock()

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                # Move to the next image in the list for running right
                current_image_index_right = (current_image_index_right + 1) % len(images_right)
            elif event.key == pygame.K_DOWN:
                # Move to the next image in the list for running down
                current_image_index_down = (current_image_index_down + 1) % len(images_down)

    # Clear the screen
    screen.fill((255, 255, 255))

    # Draw the current image for running right
    screen.blit(images_right[current_image_index_right], (image_x, image_y))

    # Draw the current image for running down
    screen.blit(images_down[current_image_index_down], (image_x + 100, image_y + 100))

    # Update the display
    pygame.display.flip()

    # Cap the frame rate
    clock.tick(animation_speed)

# Quit Pygame
pygame.quit()
sys.exit()