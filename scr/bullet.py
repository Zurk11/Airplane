import pygame
from .entity import Entity

class Bullet(Entity):
    def __init__(self, image, coords, speed, vector):
        image = pygame.transform.rotate(image, -pygame.Vector2(0, -1).angle_to(vector))
        super().__init__(image, coords, speed)
        self.vector = vector.normalize()

    def update(self):
        self.move(*(self.vector * self.speed).xy)
        if self.rect.bottom <= 0:
            self.kill()

        