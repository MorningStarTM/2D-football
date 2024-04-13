import pygame
import sys
import math


class FootballGround:
    def __init__(self, screen_width, screen_height):
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))
        pygame.display.set_caption("Football Game")
        # Load the tile images for the grass
        self.dark_grass_tile = pygame.image.load("assets\\DG.png").convert()
        self.light_grass_tile = pygame.image.load("assets\\LG.png").convert()


    def draw_grass_tiles(self):
        TILE_WIDTH = 64
        TILE_HEIGHT = 64
        NUM_TILES_X = self.screen_width // TILE_WIDTH
        NUM_TILES_Y = self.screen_height // TILE_HEIGHT

        for y in range(NUM_TILES_Y):
            for x in range(NUM_TILES_X):

                if (x // 2) % 2 == 0:
                    self.screen.blit(self.dark_grass_tile, (x * TILE_WIDTH, y * TILE_HEIGHT))
                else:
                    self.screen.blit(self.light_grass_tile, (x * TILE_WIDTH, y * TILE_HEIGHT))


    def draw_goal_post(self):
        pygame.draw.rect(self.screen, (255, 255, 255), (50, 50, self.screen_width - 100, self.screen_height - 100), 2)
        #keeper line
        pygame.draw.rect(self.screen, (255, 255, 255), (50, (self.screen_height/2)-110, 120, 250), 2)
        pygame.draw.rect(self.screen, (255, 255, 255), (self.screen_width - 170, (self.screen_height/2)-110, 120, 250), 2)

    def draw_center_circle(self):
        #center circle
        center_x = self.screen_width // 2
        center_y = self.screen_height // 2
        pygame.draw.circle(self.screen, (255, 255, 255), (center_x, center_y), 60, 2)

    def draw_center_line(self):
        #center line
        pygame.draw.line(self.screen, (255, 255, 255), (self.screen_width // 2, 50), (self.screen_width // 2, self.screen_height-50), 2)

    def goal_area(self):
        #goal post
        pygame.draw.rect(self.screen, (255, 255, 255), (0, (self.screen_height/2)-60, 50, 150))
        pygame.draw.rect(self.screen, (255, 255, 255), (self.screen_width - 50, (self.screen_height/2)-60, 50, 150))

    def draw_center_arc(self):
        center = (self.screen_width // 2, self.screen_height // 2)  # Center of the arc
        radius = 100  # Radius of the arc
        start_angle_degrees = -29  # Start angle of the arc in degrees
        start_angle_radians = math.radians(start_angle_degrees)  # Convert start angle to radians
        end_angle_radians = start_angle_radians + math.pi / 3  # End angle of the arc (add 45 degrees)
        thickness = 2  # Thickness of the arc 
        pygame.draw.arc(self.screen, (255, 255, 255), (-12, center[1] - 80, radius * 2, radius * 2),
                    start_angle_radians, end_angle_radians, 2) 


        radius = 100  # Radius of the arc
        start_angle_degrees2 = 150  # Start angle of the arc in degrees
        start_angle_radians2 = math.radians(start_angle_degrees2)  # Convert start angle to radians
        end_angle_radians2 = start_angle_radians2 + math.pi / 3  # End angle of the arc (add 45 degrees)



        pygame.draw.arc(self.screen, (255, 255, 255), (self.screen_width-185, center[1] - 80, radius * 2, radius * 2),
                            start_angle_radians2, end_angle_radians2, thickness)

    def draw(self):
        self.draw_grass_tiles()
        self.draw_goal_post()
        self.draw_center_arc()
        self.draw_center_circle()
        self.draw_center_line()
        self.goal_area()