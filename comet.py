import pygame
from random import randint

class Comet(pygame.sprite.Sprite):

    def __init__(self, comet_event):
        super().__init__()
        self.comet_event = comet_event
        self.image = pygame.image.load('assets/comet.png')
        self.image = pygame.transform.rotozoom(self.image, 45, 1)
        self.image = pygame.transform.scale(self.image, (70, 70))
        self.rect = self.image.get_rect()
        self.rect.x = randint(0, 1080)
        self.rect.y = - randint(30, 800)
        self.velocity = randint(8, 15)
        self.attack = 30
    
    def remove(self):
        self.comet_event.allComets.remove(self)

    def fall(self):
        self.rect.y += self.velocity
        if self.rect.y >= 550:
            self.remove()
            if len(self.comet_event.allComets) == 0:
                self.comet_event.fall_mode = False
                self.comet_event.reset()
                if len(self.comet_event.game.allMonsters) == 0:
                    self.comet_event.game.spawn_monster()
                    self.comet_event.game.spawn_monster()
        
        if self.comet_event.game.check_collision(self, self.comet_event.game.allPlayer):
            self.comet_event.game.player.dammage(self.attack)
            self.remove()