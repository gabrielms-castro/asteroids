import pygame
import random

from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        
    def draw(self, screen):
        pygame.draw.circle(
            surface=screen,
            color="white",
            center = self.position,
            radius=self.radius,
            width=2,
        )
    
    def update(self, dt):
        self.position += self.velocity * dt
    
    def split(self):
        self.kill()
        
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
    
        random_angle = random.uniform(20, 50)
        
        vector1 = self.velocity.rotate(random_angle)
        vector2 = self.velocity.rotate(-random_angle)
        
        old_radius = self.radius
        smaller_asteroids_new_radius = old_radius - ASTEROID_MIN_RADIUS
        
        new_asteroid1 = Asteroid(self.position.x, self.position.y, smaller_asteroids_new_radius)
        new_asteroid2 = Asteroid(self.position.x, self.position.y, smaller_asteroids_new_radius)
        
        new_asteroid1.velocity = vector1 * 1.2
        new_asteroid2.velocity = vector2 * 1.2
        
