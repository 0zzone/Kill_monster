# Imports
import pygame
pygame.init()
from player import Player
from game import Game

# Création de la fenêtre
pygame.display.set_caption('Jeu Python')
screen = pygame.display.set_mode((1080, 650))



# On créé le jeu
game = Game()

running = True
while running:

    # On installe le background
    background = pygame.image.load('assets/background.png')
    screen.blit(background, (0,0))

    banner = pygame.image.load('assets/banner.png')
    banner = pygame.transform.scale(banner, (400, 250))

    button = pygame.image.load('assets/play-button.png')
    button_rect = button.get_rect()
    button_rect.x = 500
    button_rect.y = 400

    if game.is_playing:
        game.update(screen)
    else:
        screen.blit(banner, (300, 100))
        screen.blit(button, button_rect)
        if game.already:
            font = pygame.font.SysFont("monospace", 20)
            score_text = font.render(f"Score: {game.score}", 1, (0,0,0))
            screen.blit(score_text, (20, 20))


    # On met à jour le jeu
    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
        elif event.type == pygame.KEYDOWN:
            game.pressed[event.key] = True

            if event.key == pygame.K_SPACE:
                game.player.launch_projectile(game.player)

        elif event.type == pygame.KEYUP:
            game.pressed[event.key] = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if button_rect.collidepoint(event.pos):
                game.is_playing = True
                game.score = 0