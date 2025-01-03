import pygame

from bullets import Shot
from circleshape import CircleShape
from constants import (PLAYER_RADIUS, PLAYER_SHOOT_COOLDOWN, PLAYER_SHOOT_SPEED, PLAYER_SPEED,
                       PLAYER_TURN_SPEED)


class Player(CircleShape):
    def __init__ (self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0
        self.shoot_timer = 0
        
    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]   
         
    def draw(self, screen):
        pygame.draw.polygon(
            surface=screen,
            color="white",
            points=self.triangle(),
            width=2
        )
    
    def update(self, dt):
        self.shoot_timer -= dt
        keys = pygame.key.get_pressed()
        
        # rotate left
        if keys[pygame.K_a]:
            self.rotate(-dt) # need to invert dt to rotate left
        
        # rotate right    
        if keys[pygame.K_d]:
            self.rotate(dt)
        
        # move forward    
        if keys[pygame.K_w]:
            self.move(dt)
    
        # move backward
        if keys[pygame.K_s]:
            self.move(-dt)
        
        # shoot
        if keys[pygame.K_SPACE]:
            self.shoot()
    
    def rotate(self, dt):
        self.rotation += PLAYER_TURN_SPEED * dt
        
    def move(self, dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward *PLAYER_SPEED * dt
    
    def shoot(self):
        if self.shoot_timer > 0:
            return  
        self.shoot_timer = PLAYER_SHOOT_COOLDOWN
        shot = Shot(self.position.x, self.position.y)
        shot.velocity = pygame.Vector2(0, 1).rotate(self.rotation)
        shot.velocity *= PLAYER_SHOOT_SPEED
        
