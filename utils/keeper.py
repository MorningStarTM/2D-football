import pygame
import random
import math

SCREEN_WIDTH = 64*23
SCREEN_HEIGHT = 64*12

class GoalKeeper(pygame.sprite.Sprite):
    def __init__(self):
        # Load images
        self.images = {
            "right": [pygame.image.load("assets\\player_idle_right.png"),
                      pygame.image.load("assets\\player_right_1.png"),
                      pygame.image.load("assets\\player_right_2.png")],
            "down": [pygame.image.load("assets\\player_idle_down.png"),
                     pygame.image.load("assets\\player_down_1.png"),
                     pygame.image.load("assets\\player_down_2.png")],
            "left": [pygame.image.load("assets\\player_idle_left.png"),
                     pygame.image.load("assets\\player_left_1.png"),
                     pygame.image.load("assets\\player_left_2.png")],
            "up": [pygame.image.load("assets\\player_idle_up.png"),
                   pygame.image.load("assets\\player_up_1.png"),
                   pygame.image.load("assets\\player_up_2.png")]
        }
        self.current_direction = "right"
        self.current_image_index = 0
        self.position = [50, SCREEN_HEIGHT//2]  # x, y coordinates

    def update_position(self, direction):
        if direction == "right":
            self.current_direction = "right"
            self.position[0] += 1
        elif direction == "left":
            self.current_direction = "left"
            self.position[0] -= 1
        elif direction == "down":
            self.current_direction = "down"
            self.position[1] += 1
        elif direction == "up":
            self.current_direction = "up"
            self.position[1] -= 1

    def update_image_index(self):
        print(self.current_image_index)
        self.current_image_index = (self.current_image_index + 1) % len(self.images[self.current_direction])

    def draw(self, screen):
        screen.blit(self.images[self.current_direction][self.current_image_index], self.position)

    def current_dir(self):
        return self.current_direction
    
    def player_pos(self):
        return self.position
    
    def shoot(self):
        #space bar to shoot ball to long range
        return 6

    def sprite_group():
        keeper_group = pygame.sprite.Group()
        return keeper_group
    