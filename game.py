import pygame
pygame.init()
from player import Player
from monster import Monster
from comet_event import CometFallEvent


class Game:

    def __init__(self):
        self.is_playing = False
        self.player = Player(self)
        self.comet_event = CometFallEvent(self)
        self.allMonsters = pygame.sprite.Group()
        self.score = 0
        self.already = False

        self.allPlayer = pygame.sprite.Group()
        self.allPlayer.add(self.player)

        self.pressed = {}
        self.spawn_monster()
        self.spawn_monster()

    def update(self, screen):

        font = pygame.font.SysFont("monospace", 20)
        score_text = font.render(f"Score: {self.score}", 1, (0,0,0))
        screen.blit(score_text, (20, 20))

        # On affiche les images
        screen.blit(self.player.image, self.player.rect)
        
        self.player.allProjectiles.draw(screen)
        self.allMonsters.draw(screen)
        self.comet_event.allComets.draw(screen)
        
        for projectile in self.player.allProjectiles:
            projectile.move()
            projectile.rotate()

        for monster in self.allMonsters:
            monster.forward()
            monster.update_health(screen)

        for comet in self.comet_event.allComets:
            comet.fall()

        self.player.update_health(screen)

        self.comet_event.update_bar(screen)

        if self.pressed.get(pygame.K_RIGHT) and self.player.rect.x + self.player.image.get_width() + 25 <= 1080:
            self.player.move_right()
        elif self.pressed.get(pygame.K_LEFT) and self.player.rect.x >= 25:
            self.player.move_left()


    def check_collision(self, sprite, group):
        return pygame.sprite.spritecollide(sprite, group, False, pygame.sprite.collide_mask)
    
    def spawn_monster(self):
        self.allMonsters.add(Monster(self, self.player))