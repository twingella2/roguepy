import pygame

class MenuView:
    def __init__(self, screen):
        self.screen = screen
        self.font = pygame.font.Font(None, 30)
        self.options = ["1. Start", "2. Option", "3. Exit"]
        self.selected_option = 0

    def draw(self):
        self.screen.fill((0, 0, 0))
        for index, option in enumerate(self.options):
            color = (255, 255, 255) if index == self.selected_option else (100, 100, 100)
            text = self.font.render(option, True, color)
            self.screen.blit(text, (400 - text.get_width() // 2, 200 + index * 40))
