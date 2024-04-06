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
image7 = pygame.image.load("assets\\player_idle_left.png")
image8 = pygame.image.load("assets\\player_left_1.png")
image9 = pygame.image.load("assets\\player_left_2.png")
image10 = pygame.image.load("assets\\player_idle_up.png")
image11 = pygame.image.load("assets\\player_up_1.png")
image12 = pygame.image.load("assets\\player_up_2.png")

# Create a list of images
images_right = [image1, image2, image3]
images_down = [image4, image5, image6]
images_left = [image7, image8, image9]
images_up = [image10, image11, image12]

# Set initial image index and direction
current_image_index = 0
current_direction = "right"

# Set initial position for the player
player_x, player_y = 0, SCREEN_HEIGHT // 2

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
                current_direction = "right"
                current_image_index = (current_image_index + 1) % len(images_right)
                player_x += 6
            elif event.key == pygame.K_LEFT:
                current_direction = "left"
                current_image_index = (current_image_index + 1) % len(images_left)
                player_x -= 6
            elif event.key == pygame.K_DOWN:
                current_direction = "down"
                current_image_index = (current_image_index + 1) % len(images_down)
                player_y += 6
            elif event.key == pygame.K_UP:
                current_direction = "up"
                current_image_index = (current_image_index + 1) % len(images_up)
                player_y -= 6

    # Clear the screen
    screen.fill((255, 255, 255))

    # Draw the current image for the player
    if current_direction == "right":
        screen.blit(images_right[current_image_index], (player_x, player_y))
    elif current_direction == "left":
        screen.blit(images_left[current_image_index], (player_x, player_y))
    elif current_direction == "down":
        screen.blit(images_down[current_image_index], (player_x, player_y))
    elif current_direction == "up":
        screen.blit(images_up[current_image_index], (player_x, player_y))

    # Update the display
    pygame.display.flip()

    # Cap the frame rate
    clock.tick(animation_speed)

# Quit Pygame
pygame.quit()
sys.exit()