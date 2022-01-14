import pygame
from comet import Comet

class CometFallEvent:

    def __init__(self, game):
        self.percent = 0
        self.speed = 100
        self.allComets = pygame.sprite.Group()
        self.game = game
        self.fall_mode = False
    
    def add_percent(self):
        self.percent += self.speed / 100

    def reset(self):
        self.percent = 0
    
    def fall_meteor(self):
        self.allComets.add(Comet(self))

    def attempt_fall(self):
        for i in range(15):
            self.fall_meteor()

    
    def update_bar(self, surface):
        self.add_percent()
        pygame.draw.rect(surface, (0,0,0), [20, surface.get_height() - 50, surface.get_width()-40, 10])
        if (self.percent/100) * surface.get_width()-40 < surface.get_width()-40:
            pygame.draw.rect(surface, (200,100,80), [20, surface.get_height() - 50, (self.percent/100) * surface.get_width()-40, 10])
        else:
            if len(self.game.allMonsters) == 0:
                self.fall_mode = True