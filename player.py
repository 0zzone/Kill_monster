import pygame
pygame.init()
from projectile import Projectile

class Player(pygame.sprite.Sprite):

    def __init__(self, game):
        super().__init__()
        self.health = 100
        self.game = game
        self.max_health = 100
        self.attack = 15
        self.velocity = 10
        self.allProjectiles = pygame.sprite.Group()
        self.image = pygame.image.load('assets/monster.png')
        self.image = pygame.transform.scale(self.image, (100, 100)) 
        self.rect = self.image.get_rect()
        self.rect.x = 440
        self.rect.y = 470
    
    def dammage(self, ammount):
        self.health -= ammount
        if self.health <= 0:
            self.game.allMonsters = pygame.sprite.Group()
            self.game.comet_event.allComets = pygame.sprite.Group()
            self.game.spawn_monster()
            self.game.spawn_monster()
            self.rect.x = 440
            self.health = self.max_health
            self.game.is_playing = False
            self.game.already = True

    def update_health(self, surface):
        pygame.draw.rect(surface, (36, 36, 36), [self.rect.x, self.rect.y-10, self.max_health, 5])
        pygame.draw.rect(surface, (111, 210, 46), [self.rect.x, self.rect.y-10, self.health, 5])

    def launch_projectile(self, player):
        self.allProjectiles.add(Projectile(player))

    def move_right(self):
        if not self.game.check_collision(self, self.game.allMonsters):
            self.rect.x += self.velocity
    
    def move_left(self):
        self.rect.x -= self.velocity