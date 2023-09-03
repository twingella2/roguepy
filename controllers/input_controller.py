import pygame
import sys

class InputController:
    def handle_input(self, player_pos, player_speed, dungeon): # dungeonを追加
        x_move = 0
        y_move = 0

        keys = pygame.key.get_pressed()
        new_pos = player_pos.copy()

        if joystick:
            x_move += joystick.get_axis(0)
            y_move += joystick.get_axis(1)
        
        # キー入力で移動
        if keys[pygame.K_LEFT]:
            x_move -= 1
        if keys[pygame.K_RIGHT]:
            x_move += 1
        if keys[pygame.K_UP]:
            y_move -= 1
        if keys[pygame.K_DOWN]:
            y_move += 1
        
        # ジョイスティックの入力を処理
        x_move += joystick.get_axis(0)
        y_move += joystick.get_axis(1)

        new_x = int(player_pos[0] + x_move * player_speed)
        new_y = int(player_pos[1] + y_move * player_speed)

        # 壁との衝突判定
        if not dungeon.is_wall(new_x // 30, new_y // 30):
            player_pos[0], player_pos[1] = new_x, new_y

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        return new_x, new_y
