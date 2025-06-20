import pygame
from constants import *
from player import Player


def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("PyGame - Asteroids")
    fps = pygame.time.Clock()
    dt = 0
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    updateable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()

    updateable.add(player)
    drawable.add(player)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        screen.fill(pygame.Color(0, 0, 0))
        dt = fps.tick(60) / 1000

        for item in updateable:
            item.update(dt)

        for item in drawable:
            item.draw(screen)

        pygame.display.flip()


if __name__ == "__main__":
    main()
