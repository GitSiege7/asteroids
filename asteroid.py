from circleshape import CircleShape
from constants import *
import random
import pygame

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, width=2)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()

        if(self.radius <= ASTEROID_MIN_RADIUS):
            return
        
        num = random.uniform(20, 50)

        vector1 = self.velocity.rotate(num)
        vector2 = self.velocity.rotate(-1 * num)

        new_r = self.radius - ASTEROID_MIN_RADIUS

        ast1 = Asteroid(self.position.x, self.position.y, new_r)
        ast2 = Asteroid(self.position.x, self.position.y, new_r)

        ast1.velocity = vector1 * 1.2
        ast2.velocity = vector2 * 1.2