import pygame

# Base class for game objects
class CircleShape(pygame.sprite.Sprite):
    def __init__(self, x, y, radius):
        # we will be using this later
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()

        self.x = x
        self.y = y
        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 0)
        self.radius = radius

    def draw(self, screen):
        # sub-classes must override
        pass
    
    def update(self, dt):
        # sub-classes must override
        pass
    
    def colision(self, object):
        r1 = self.radius # actual object radius
        r2 = object.radius # collided object radius
        radius_sum = r1 + r2    
        distance = object.position.distance_to(self.position) # distance between two objects centers
                                                              
        if distance < radius_sum: # if distance is less than sum of radiuses, objects are colliding
            return True
                
        return False