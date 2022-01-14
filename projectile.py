import pygame
pygame.init()

class Projectile(pygame.sprite.Sprite):

    def __init__(self, player):
        super().__init__()
        self.player = player
        self.velocity = 15
        self.image = pygame.image.load('assets/projectile.png')
        self.image = pygame.transform.scale(self.image, (50, 50))
        self.rect = self.image.get_rect()
        self.rect.x = self.player.rect.x + 80
        self.rect.y = self.player.rect.y + 20
        self.origin_image = self.image
        self.angle = 0
    
    def rotate(self):
        self.angle += 12
        self.image = pygame.transform.rotozoom(self.origin_image, self.angle, 1)
        self.rect = self.image.get_rect(center=self.rect.center)

    def remove(self):
        self.player.allProjectiles.remove(self)

    def move(self):
        for monster in self.player.game.check_collision(self, self.player.game.allMonsters):
            self.remove()
            monster.dammage(self.player.attack)

        self.rect.x += self.velocity
        if self.rect.x > 1080:
            self.remove()
