import pygame


class OptionView:
    def __init__(self, screen):
        self.screen = screen
        self.font = pygame.font.Font(None, 30)
        self.options = ["Resolution: 800x600", "Resolution: 1024 x 768", "Resolution: 1280 x 1024", "Back to Menu"]
        self.selected_option = 0
    
    def draw(self):
        self.screen.fill((0, 0, 0))
        for index, option in enumerate(self.options):
            color = (255, 255, 255) if index == self.selected_option else (100, 100, 100)
            text = self.font.render(option, True, color)
            self.screen.blit(text, (400 - text.get_width() // 2, 200 + index * 40))