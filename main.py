import pygame
from scr.constant import MAX_FPS, SIZE


def game(disp, clock):
    while True:
        for event in pygame.event.get():
            if event == pygame.QUIT:
                exit()

        pygame.display.update()
        clock.tick(MAX_FPS)

def main() -> None:
    pygame.init()

    disp = pygame.display.set_mode(SIZE, pygame.RESIZABLE | pygame.SCALED)
    pygame.display.set_caption('Shooter')

    clock = pygame.time.Clock()

    while True:
        game(disp, clock)






if __name__ == '__main__':
    main()