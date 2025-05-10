import pygame
from random import *
from scr.constant import *
from scr.player import Player
from scr.bullet import Bullet
from scr.enemy import Enemy
from scr.utils import load_image
from scr.entity import Entity
from scr.utils import get_path


def game(disp, clock):
    astr_iamge = load_image('govno', 'images', 'asteroid.png', size=[164, 164])
    player_iamge = load_image('govno', 'images', 'player.png', size=[96, 96])
    shoot_iamge = load_image('govno', 'images', 'shot.png', size=[64,64])
    back_iamge = load_image('govno', 'images', 'background.png', size=SIZE)

    shoot_sound = pygame.Sound(get_path('govno', 'sounds', 'ekh.wav'))
    death_sound = pygame.Sound(get_path('govno', 'sounds', 'death.wav'))
    expl_sound = pygame.Sound(get_path('govno', 'sounds', 'explosion.wav'))

    shoot_sound.set_volume(0.5)
    death_sound.set_volume(0.5)
    expl_sound.set_volume(0.5)

    coords = SIZE[0]/2, SIZE[1]-50 

    player = Player(player_iamge, coords, PLAYER_SPEED, PLAYER_HEALTH)

    bullets = list()
    
    enemys = list()

    difficulty = 0
    score = 0
    font = pygame.Font(get_path("govno", "fonts", "pixel.ttf"), 24)

    pygame.time.set_timer(SPAWN_EVENT, 2000, 1)

    while player.health > 0:
        difficulty += clock.get_time()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
            elif event.type == SHOOT_EVENT:
                if score < 10: 
                    b = Bullet(shoot_iamge, player.rect.midtop, 10, pygame.Vector2(0, -1))
                    bullets.append(b)
                elif score < 20:
                    b1 = Bullet(shoot_iamge, player.rect.midtop, 10, pygame.Vector2(0.5, -1))
                    b2 = Bullet(shoot_iamge, player.rect.midtop, 10, pygame.Vector2(-0.5, -1))
                    bullets.extend([b1, b2])
                elif score < 3:
                    ...
                shoot_sound.play()
            elif event.type == SPAWN_EVENT:
                milis = max(750, round(2000 - difficulty/ 70))
                print(milis)
                pygame.time.set_timer(SPAWN_EVENT, milis, 1)

                new_im = pygame.transform.rotozoom(astr_iamge, randint(0, 360), 1 + randint(-10, 500) / 100)

                e = Enemy(round(10 + difficulty/7000), new_im,[ randint(50, SIZE[0] - 50), -new_im.height], 5 + difficulty/35000)
                enemys.append(e)


        player.update()

        for i in bullets.copy():
            i.update()
            if not i.alive:
                bullets.remove(i)

        for i in enemys.copy():
            i.update()
            if not i.alive: 
                enemys.remove(i)
                score += 1 

        for b in bullets:
            for e in enemys:
                if b.collide_entity(e):
                    expl_sound.play()
                    b.kill()
                    e.kill()
                    score += 1
        
        for e in enemys:
            if e.collide_entity(player):
                death_sound.play()
                player.get_damage(ENEMY_DAMAGE)
                e.kill()
                score -= 1

        disp.fill("black")
        disp.blit(back_iamge, (0,0))

        player.render(disp)
        for u in bullets:
            u.render(disp)
        for u in enemys:
            u.render(disp)

        pygame.draw.rect(disp, (100, 0, 0), [10,10, HEALTH_BAR_WIDTH, 30])
        width = int(player.health / PLAYER_HEALTH * HEALTH_BAR_WIDTH)
        pygame.draw.rect(disp, (255, 0, 0), [10,10, width, 30])

        image_score = font.render(str(score), True, (50, 200, 50))
        rect_score = image_score.get_rect(midtop = [SIZE[0]/2, 10])
        disp.blit(image_score, rect_score)

        pygame.display.update()
        clock.tick(MAX_FPS)

def show_lose(disp, clock):
    running = True

    font = pygame.Font(get_path("govno", "fonts", "pixel.ttf"), 64)
    text = font.render('YOU LOSE!', True, (255, 50, 50))
    disp.blit(text, text.get_rect(center=[SIZE[0] / 2, SIZE[1]/ 2]))
    pygame.display.update()

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
            elif event.type == pygame.KEYDOWN:
                running = False
        clock.tick(MAX_FPS)



def main() -> None:
    pygame.init()

    disp = pygame.display.set_mode(SIZE, pygame.RESIZABLE | pygame.SCALED)
    pygame.display.set_caption('Shooter')

    clock = pygame.time.Clock()

    pygame.mixer.music.load(get_path('govno', 'music', 'background-1.mp3'))
    pygame.mixer.music.set_volume(0.2)
    pygame.mixer.music.play(-1)

    while True:
        game(disp, clock)
        show_lose(disp, clock)


if __name__ == '__main__':
    main() 