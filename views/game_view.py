import pygame
import random

class GameView:
    def __init__(self, screen):
        self.screen = screen
        self.tile_size = 30

    def draw_dungeon(self, dungeon, camera_x, camera_y):
        for y, row in enumerate(dungeon.map):
            for x, tile in enumerate(row):
                if tile == '#':
                    pygame.draw.rect(self.screen, (100, 100, 100), (x * self.tile_size - camera_x, y * self.tile_size - camera_y, self.tile_size, self.tile_size))
                elif tile == '.':
                    random_offset = random.randint(-5, 5)
                    pygame.draw.rect(self.screen, (135 + random_offset, 206 + random_offset, 250 + random_offset), (x * self.tile_size - camera_x, y * self.tile_size - camera_y, self.tile_size, self.tile_size))
                elif tile == '>':
                    pygame.draw.rect(self.screen, (255, 0, 0), (x * self.tile_size - camera_x, y * self.tile_size - camera_y, self.tile_size, self.tile_size))

def draw(self, player_pos, camera_x, camera_y):
    pygame.draw.rect(self.screen, (255, 255, 255), (player_pos[0] - camera_x, player_pos[1] - camera_y, 10, 10))

