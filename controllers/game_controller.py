import pygame

from models.levels import Dungeon
from controllers.input_controller import InputController
from views.game_view import GameView
from views.menu_view import MenuView
from views.option_view import OptionView
from views.title_view import TitleView
from models.player import Player


class GameController:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((800, 600))
        self.clock = pygame.time.Clock()
        self.input_controller = InputController()
        self.game_view = GameView(self.screen)
        self.menu_view = MenuView(self.screen)
        self.option_view = OptionView(self.screen)
        self.show_menu = False
        self.show_option = False
        self.title_view = TitleView(self.screen)
        self.show_title = True
        self.dungeon = Dungeon()
        self.player = Player()
        self.player_pos = [self.dungeon.start_pos[0] * 30, self.dungeon.start_pos[1] * 30]
        self.camera_x, self.camera_y = 0, 0

        class GameController:
        # 既存のコード
            pygame.joystick.init()
            self.joystick = None
            if pygame.joystick.get_count() > 0:
                self.joystick = pygame.joystick.Joystick(0)
                self.joystick.init()


    def run(self):
        player_speed = 10
        while True:
            keys = pygame.key.get_pressed()
            if keys[pygame.K_ESCAPE]:
                self.show_menu = True

            if self.show_title:
                self.title_screen()
            elif self.show_menu:
                self.menu_screen()
            elif self.show_option:
                self.option_screen()
            else:
                self.game_logic(player_speed)

            pygame.display.flip()
            self.clock.tick(60)
    
    def title_screen(self):
        self.title_view.draw()
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_DOWN:
                    self.title_view.selected_option = (self.title_view.selected_option + 1) % 3
                elif event.key == pygame.K_UP:
                    self.title_view.selected_option = (self.title_view.selected_option - 1) % 3
                elif event.key == pygame.K_RETURN:
                    if self.title_view.selected_option == 0:  # Start
                        self.show_title = False
                    elif self.title_view.selected_option == 1:  # Continue
                        pass  # ゲームの続行ロジックをここに追加
                    elif self.title_view.selected_option == 2:  # Quit
                        pygame.quit()
                        exit()

    def game_logic(self, player_speed):
        self.input_controller.handle_input(self.player_pos, player_speed, self.dungeon)

        # プレイヤーのステータスの描画
        self.player.draw_status(self.screen)
        
        # 階層の描画
        font = pygame.font.SysFont(None, 24)
        level_text = f"階層: {self.dungeon.level}"
        text = font.render(level_text, True, (255, 255, 255))
        self.screen.blit(text, (self.screen.get_width() - 100, 10))

        # カメラの追跡を更新
        self.camera_x = self.player_pos[0] - 400
        self.camera_y = self.player_pos[1] - 300

        x_index = self.player_pos[0] // 30
        y_index = self.player_pos[1] // 30

        # 階段にふれる前に範囲外アクセスをチェックする
        if 0 <= x_index < len(self.dungeon.map[0]) and 0 <= y_index < len(self.dungeon.map):
            if self.dungeon.is_stairs(x_index, y_index):
                self.dungeon.next_level()
                # プレイヤーの位置がダンジョンマップの範囲内にあることを確認
                self.player_pos = [self.dungeon.start_pos[0] * 30, self.dungeon.start_pos[1] * 30]

        # 描画
        self.game_view.draw_dungeon(self.dungeon, self.camera_x, self.camera_y)
        pygame.draw.rect(self.screen, (255, 255, 255), (self.player_pos[0] - self.camera_x, self.player_pos[1] - self.camera_y, 30, 30))
        pygame.display.flip()

        # ジョイスティックの入力を取得
        if self.joystick:
            x_move = self.joystick.get_axis(0)  # 左ジョイスティックの水平方向
            y_move = self.joystick.get_axis(1)  # 左ジョイスティックの垂直方向

        # プレイヤーの位置を更新
            self.player_pos[0] += x_move * player_speed
            self.player_pos[1] += y_move * player_speed

        # フォントの設定
        font = pygame.font.Font(None, 36)

        # LV, HP, MP, SPの表示
        lv_text = font.render(f"LV: {self.player.level}", True, (255, 255, 255))
        hp_text = font.render(f"HP: {self.player.hp}/{self.player.max_hp}", True, (255, 0, 0))
        mp_text = font.render(f"MP: {self.player.mp}/{self.player.max_mp}", True, (0, 0, 255))
        sp_text = font.render(f"SP: {self.player.sp}/{self.player.max_sp}", True, (0, 255, 0))
        self.screen.blit(lv_text, (10, 10))
        self.screen.blit(hp_text, (10, 40))
        self.screen.blit(mp_text, (10, 70))
        self.screen.blit(sp_text, (10, 100))

        # HP, MP, SPのゲージ
        pygame.draw.rect(self.screen, (255, 0, 0), (100, 40, 200 * self.player.hp / self.player.max_hp, 20))
        pygame.draw.rect(self.screen, (0, 0, 255), (100, 70, 200 * self.player.mp / self.player.max_mp, 20))
        pygame.draw.rect(self.screen, (0, 255, 0), (100, 100, 200 * self.player.sp / self.player.max_sp, 20))

        # ダンジョン階層の表示
        floor_text = font.render(f"Floor: {self.dungeon.current_floor}", True, (255, 255, 255))
        self.screen.blit(floor_text, (self.screen.get_width() - 100, 10))


    def menu_screen(self):
        self.menu_view.draw()
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_DOWN:
                    self.menu_view.selected_option = (self.menu_view.selected_option + 1) % 3
                elif event.key == pygame.K_UP:
                    self.menu_view.selected_option = (self.menu_view.selected_option - 1) % 3
                elif event.key == pygame.K_RETURN:
                    if self.menu_view.selected_option == 0:
                        self.show_menu = False
                    elif self.menu_view.selected_option == 1:
                        self.show_option = True
                        self.show_menu = False
                    elif self.menu_view.selected_option == 2:
                        pygame.quit()
                        exit()

    def option_screen(self):
        self.option_view.draw()
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_DOWN:
                    self.option_view.selected_option = (self.option_view.selected_option + 1) % 3
                elif event.key == pygame.K_UP:
                    self.option_view.selected_option = (self.option_view.selected_option - 1) % 3
                elif event.key == pygame.K_RETURN:
                    if self.option_view.selected_option == 0:  # Start
                        self.show_option = False
                    elif self.option_view.selected_option == 1:  # Option
                        self.show_option = False
                        self.show_menu = True
                    elif self.option_view.selected_option == 2:  # Exit
                        pygame.quit()
                        exit()
                elif event.key == pygame.K_ESCAPE:  # Go back to menu
                    self.show_option = False
                    self.show_menu = True
