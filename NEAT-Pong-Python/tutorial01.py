import pygame
from pong import Game

width, height = 700, 500

window = pygame.display.set_mode((width, height))
game = Game(window, width, height)

clock = pygame.time.Clock()
run = True
while run:
    clock.tick(60)  # this is to limit the speed
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            break

    keys = pygame.key.get_pressed()
    if (keys[pygame.K_UP]):
        game.move_paddle(left=True, up=True)
    if (keys[pygame.K_DOWN]):
        game.move_paddle(left=True, up=False)

    game_info = game.loop()
    print(game_info.left_score, game_info.right_score)
    game.draw(False, False)
    pygame.display.update()

pygame.quit()
