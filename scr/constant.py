import pygame

# пременные для окна

MAX_FPS = 60
SIZE = [800,600]


# события

SHOOT_EVENT = pygame.event.custom_type()
SPAWN_EVENT = pygame.event.custom_type()


# переменные игрока 
HEALTH_BAR_WIDTH = 150
PLAYER_HEALTH = 100
PLAYER_SPEED = 7.5

ENEMY_DAMAGE = 10
ENEMY_SPEED= 5


#переменные пули 
BULET_SPEED = 10

