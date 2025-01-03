import sys

import pygame

from asteroid import Asteroid
from asteroidfield import AsteroidField
from bullets import Shot
from constants import *
from player import Player


def main():
    print("Starting asteroids!")
    
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0
    
    # groups
    updatable = pygame.sprite.Group() # all objects that can be updated
    drawable = pygame.sprite.Group() # all objects that can be drawn
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    
    # containers
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable,)
    Shot.containers = (shots, updatable, drawable)
    
    # instances
    player_instance = Player(x=SCREEN_WIDTH / 2, y=SCREEN_HEIGHT / 2)
    asteroid_field_instance = AsteroidField()
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        for object in updatable:
            object.update(dt)
        
        for asteroid in asteroids:
            if player_instance.colision(asteroid):
                print("Game over!")
                pygame.quit()
                sys.exit()
        
            for shot in shots:
                if shot.colision(asteroid):
                    asteroid.kill()
                    asteroid.split()
        
        screen.fill("black")
        
        for object in drawable:
            object.draw(screen)
        
        pygame.display.flip()
        
        # limit the framerate to 60 FPS
        dt = clock.tick(60) / 1000
    
if __name__ == "__main__":
    main()


