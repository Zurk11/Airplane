import pygame
from scr.constant import MAX_FPS, SIZE, SHOOT_EVENT
from scr.player import Player

def game(disp, clock):
    coords = SIZE[0]/2, SIZE[1]/50
    image = pygame.Surface([50,50])
    image.fill( ( 255, 0, 0) )
    player = Player(image, coords, 4, 100)

    while True:
        for event in pygame.event.get():
            if event == pygame.QUIT:
                exit()
            elif event.type == SHOOT_EVENT:
                print(1)

        player.update()

        disp.fill((0,0,0))

        player.render(disp)

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