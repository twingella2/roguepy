import pygame

class TitleView:
    def __init__(self, screen):
        self.screen = screen
        self.font = pygame.font.Font(None, 30)
        self.options = ["Start", "Continue", "Quit"]
        self.selected_option = 0

    def draw(self):
        title_image = pygame.image.load('resources/title.png')  # タイトル画像をロード
        self.screen.blit(title_image, (0, 0))
        for index, option in enumerate(self.options):
            color = (255, 255, 255) if index == self.selected_option else (100, 100, 100)
            text_surface = self.font.render(option, True, color)
            self.screen.blit(text_surface, (350, 300 + index * 30))
