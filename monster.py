import pygame
from random import randint

class Monster(pygame.sprite.Sprite):

    def __init__(self, game, player):
        super().__init__()
        self.game = game
        self.allPlayer = pygame.sprite.Group()
        self.allPlayer.add(player)
        self.health = 100
        self.max_health = 100
        self.attack = 0.5
        self.image = pygame.image.load('assets/enemy.png')
        self.image = pygame.transform.scale(self.image, (100, 100)) 
        self.rect = self.image.get_rect()
        self.rect.x = randint(1000, 1200)
        self.rect.y = 470
        self.velocity = randint(6, 8)
    

    def dammage(self, ammount):
        self.health -= ammount
        if self.health <= 0 and self.game.comet_event.percent < 100:
            self.rect.x = randint(1000, 1200)
            self.velocity = randint(6, 8)
            self.health = self.max_health
            self.game.score += 10
        elif self.health <= 0 and self.game.comet_event.percent >= 100:
            self.game.score += 10
            self.game.allMonsters.remove(self)
            if len(self.game.allMonsters) == 0:
                self.game.comet_event.attempt_fall()
            self.game.comet_event.reset()

    def update_health(self, surface):
        pygame.draw.rect(surface, (36, 36, 36), [self.rect.x, self.rect.y-10, self.max_health, 5])
        pygame.draw.rect(surface, (111, 210, 46), [self.rect.x, self.rect.y-10, self.health, 5])

    def forward(self):
        if not self.game.check_collision(self, self.allPlayer):
            self.rect.x -= self.velocity
        else:
            self.game.player.dammage(self.attack)