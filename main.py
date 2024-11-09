import pygame
from constants import * #noqa
from player import Player

def main():
    pygame.init()
    # setting screen resolution
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    # setting delta time clock
    dt = 0
    clock = pygame.time.Clock()

    # creating groups
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()

    Player.containers = (updatable,drawable)

    # instantiate player object
    Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)

    print("Starting asteroids!")
    print("Screen width:",1280)
    print("Screen height:",720)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill(pygame.Color(0,0,0))

        for item in updatable:
            item.update(dt)
        
        for item in drawable:
            item.draw(screen)

        pygame.display.flip()
        t_pass = clock.tick(60) #60 fps
        dt = t_pass/1000 # as delta time returned is in milliseconds    


if __name__ == "__main__":
    main()