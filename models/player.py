import pygame

class Player():
    def __init__(self):
        self.level = 1
        self.hp = 100
        self.max_hp = 100
        self.mp = 100
        self.max_mp = 100
        self.sp = 100
        self.max_sp = 100

    def draw_status(self, screen):
        # HPゲージの描画
        pygame.draw.rect(screen, (255, 0, 0), (10, 10, self.hp / self.max_hp * 100, 10))
        # MPゲージの描画
        pygame.draw.rect(screen, (0, 0, 255), (10, 30, self.mp / self.max_mp * 100, 10))
        # SPゲージの描画
        pygame.draw.rect(screen, (0, 255, 0), (10, 50, self.sp / self.max_sp * 100, 10))
        
        # LV, HP, MP, SPの値の描画
        font = pygame.font.SysFont(None, 24)
        status_text = f"LV: {self.level}  HP: {self.hp}/{self.max_hp}  MP: {self.mp}/{self.max_mp}  SP: {self.sp}/{self.max_sp}"
        text = font.render(status_text, True, (255, 255, 255))
        screen.blit(text, (10, 70))
