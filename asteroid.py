import pygame
from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS
import random

class Asteroid(CircleShape):
    def __init__(self, x, y, radius, asteroid_group):
        super().__init__(x, y, radius)
        self.asteroid_group = asteroid_group
    
    def draw(self, screen):
        pygame.draw.circle(screen, (255,255,255), self.position, self.radius, 2)
    
    def update(self, dt):
        self.position += self.velocity * dt
    
    def split(self):
        self.kill() # Kill the current asteroid to make new ones
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            random_angle = random.uniform(20,50)
            new_velocity1 = self.velocity.rotate(random_angle)
            new_velocity2 = self.velocity.rotate(-random_angle)
            new_radius = self.radius - ASTEROID_MIN_RADIUS
            asteroid1 = Asteroid(self.position.x, self.position.y, new_radius, self.asteroid_group)
            asteroid1.velocity = new_velocity1 * 1.2
            asteroid2 = Asteroid(self.position.x, self.position.y, new_radius, self.asteroid_group)
            asteroid2.velocity = new_velocity2 * 1.2
