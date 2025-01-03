import pygame

from constants import *

def main():
    print("Starting asteroids!")
    
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        screen.fill(color=(0, 0, 0), rect=None, special_flags=0)
        pygame.display.flip()
    
    pygame.quit()
    
if __name__ == "__main__":
    main()


