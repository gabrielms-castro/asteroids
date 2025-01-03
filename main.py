import pygame

from constants import *
from player import Player

def main():
    print("Starting asteroids!")
    
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0
    player_instance = Player(
        x=SCREEN_WIDTH / 2,
        y=SCREEN_HEIGHT / 2 
    )
    
    # groups
    updatable = pygame.sprite.Group(player_instance) # all objects that can be updated
    drawable = pygame.sprite.Group(player_instance) # all objects that can be drawn
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        for player in updatable:
            player.update(dt)
        
        screen.fill("black")
        
        for player in drawable:
            player.draw(screen)
        
        pygame.display.flip()
        dt = clock.tick(60) / 1000
    
if __name__ == "__main__":
    main()


