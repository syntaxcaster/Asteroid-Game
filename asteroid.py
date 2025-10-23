import pygame
import random
from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def split(self):
        self.kill()

        if self.radius <= ASTEROID_MIN_RADIUS:
            return
            
        rand_angle = random.uniform(20, 50)
        vect1 = self.velocity.rotate(rand_angle)
        vect2 = self.velocity.rotate(-rand_angle)
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        astro1 = Asteroid(self.position.x, self.position.y, new_radius)
        astro2 = Asteroid(self.position.x, self.position.y, new_radius)
        astro1.velocity = vect1 * 1.2
        astro2.velocity = vect2 * 1.2

    def update(self, dt):
        self.position += self.velocity * dt

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)