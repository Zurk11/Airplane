from .entity import Entity
import pygame
from .constant import SHOOT_EVENT, SIZE


class Player(Entity):
    def __init__(self, image, coords, speed, health):
        super().__init__(image, coords, speed)
        self.health = health

    def get_damage(self, value):
        self.health -= value

        if self.health <= 0:
            self.kill()
            self.health = 0
    
    def update(self):
        pressed_keys = pygame.key.get_pressed()
        left = pressed_keys[pygame.K_a] or pressed_keys[pygame.K_LEFT]
        right = pressed_keys[pygame.K_d] or pressed_keys[pygame.K_RIGHT]
        if left != right:
            if left:
                self.move(-self.speed, 0)
            else:
                self.move(self.speed, 0)

        just_pressed = pygame.key.get_just_pressed()
        if just_pressed[pygame.K_SPACE]:
            pygame.event.post(pygame.Event(SHOOT_EVENT))
        
    def move(self, x, y):
        super().move(x, y)

        if self.rect.left <= 0:
            self.rect.left = 0
        if self.rect.right >= SIZE[0]:
            self.rect.right = SIZE[0]
        