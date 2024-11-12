import pygame
from constants import * #noqa
from player import Player,Shot
from asteroid import Asteroid
from asteriodfield import AsteroidField

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
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (updatable,drawable)
    Asteroid.containers = (asteroids,updatable,drawable)
    AsteroidField.containers = (updatable,)
    Shot.containers = (shots,updatable,drawable)
    # instantiate player object
    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
    player.timer = 0
    AsteroidField()

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
        
        for item in asteroids:
            if item.collision(player):
                print("Game Over")
                return
            for bullet in shots:
                if item.collision(bullet):
                    bullet.kill()
                    item.split()

        for item in shots:
            item.draw(screen)

        for item in drawable:
            item.draw(screen)

        pygame.display.flip()
        t_pass = clock.tick(60) #60 fps
        dt = t_pass/1000 # as delta time returned is in milliseconds    


if __name__ == "__main__":
    main()