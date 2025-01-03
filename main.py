import pygame
import sys

from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField

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
    
    # containers
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable,)
    
    # instances
    player_instance = Player(
        x=SCREEN_WIDTH / 2,
        y=SCREEN_HEIGHT / 2 
    )
    
    asteroid_field_instance = AsteroidField()
    
    
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        for player in updatable:
            player.update(dt)
        
        for asteroid in asteroids:
            if player_instance.colision(asteroid):
                print("Game over!")
                pygame.quit()
                sys.exit()
        
        screen.fill("black")
        
        for player in drawable:
            player.draw(screen)
        
        pygame.display.flip()
        dt = clock.tick(60) / 1000
    
if __name__ == "__main__":
    main()


