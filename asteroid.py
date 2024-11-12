import random
import pygame
from circleshape import CircleShape
from constants import *

class Asteroid(CircleShape):
    def __init__(self,x,y,radius):
        super().__init__(x,y,radius)
        self.x = x
        self.y = y
        self.position = pygame.Vector2(x,y)

    def draw(self, screen):
        pygame.draw.circle(
            screen,
            (255,255,255),
            self.position,
            self.radius,
            2)

    def update(self, dt):
        self.position += self.velocity * dt
    
    def split(self):
        self.kill()
        
        if self.radius <= ASTEROID_MIN_RADIUS:
            return 
        
        rand_angle = random.uniform(20,50)
        vectr_astrd_one = self.velocity.rotate(rand_angle)
        vectr_astrd_two = self.velocity.rotate(-rand_angle)
        radius_astrd = self.radius - ASTEROID_MIN_RADIUS 
        astrd_one = Asteroid(self.x,self.y,radius_astrd)
        astrd_two = Asteroid(self.x,self.y,radius_astrd)
        astrd_one.velocity = vectr_astrd_one * 1.2
        astrd_two.velocity = vectr_astrd_two * 1.2
        