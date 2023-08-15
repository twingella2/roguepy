import pygame
import sys

class InputController:
    def handle_input(self, player_pos, player_speed, dungeon): # dungeonを追加
        keys = pygame.key.get_pressed()

        # キー入力で移動
        new_x, new_y = player_pos
        # new_x = player_pos[0]
        # new_y = player_pos[1]

        new_pos = player_pos.copy()

        if keys[pygame.K_LEFT]:
            new_x -= player_speed
        if keys[pygame.K_RIGHT]:
            new_x += player_speed
        if keys[pygame.K_UP]:
            new_y -= player_speed
        if keys[pygame.K_DOWN]:
            new_y += player_speed

        # 壁との衝突判定
        if not dungeon.is_wall(new_x // 30, new_y // 30):
            player_pos[0], player_pos[1] = new_x, new_y

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
