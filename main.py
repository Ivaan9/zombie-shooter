from pygame import *
from random import *
import math
from settings import *
from sounds import *
#from menu import *
init()
mixer.init()
window = display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
clock = time.Clock()
game = True
shot_sound = mixer.Sound("assets/sounds/shot.mp3")
shot_sound.set_volume(0.3)



fon_image = image.load("assets/images/fon.png")
player_image = image.load("assets/images/player.png").convert_alpha()
zombies_image = image.load("assets/images/zombies.png").convert_alpha()
player_image = transform.scale(player_image, (100, 100))
zombies_image = transform.scale(zombies_image, (50, 50))
player_y = 400
player_x = 300
player_hp = 100

score = 0
zombies = []
bullets = []
def spawn_zombie():
    for i in range(10):
        zombies.append([randint(0, 1920), randint(0, 100)])
spawn_zombie()

font = font.Font(None, 36)

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    window.blit(fon_image, (0, 0))
    keys = key.get_pressed()
    if keys[K_w]:
        player_y -= 5
    if keys[K_s]:
        player_y += 5
    if keys[K_a]:
        player_x -= 5
    if keys[K_d]:
        player_x += 5
    window.blit(player_image, (player_x, player_y))

    for zombie in zombies:
        dx = player_x - zombie[0]
        dy = player_y - zombie[1]
        dist = math.hypot(dx, dy)
        if dist < 30:
            player_hp -= 10
            if player_hp <= 0:
                game = False
        if dist != 0:
            zombie[0] += dx / dist * 2
            zombie[1] += dy / dist * 2

    if e.type == MOUSEBUTTONDOWN:
        mx, my = mouse.get_pos()
        shot_sound.play()
        dx = mx - player_x
        dy = my - player_y
        dist = (dx ** 2 + dy ** 2) ** 0.5

        angle = math.degrees(math.atan2(-dy, dx))
        rotated_image = transform.rotate(player_image, angle)
        new_rect = rotated_image.get_rect(center=(player_x, player_y))
        window.blit(rotated_image, new_rect.topleft)
        if dist != 0:
            bullets.append([
                player_x,
                player_y,
                dx / dist * 10,
                dy / dist * 10
            ])


    for zombie in zombies[:]:
        zombie_rect = Rect(zombie[0] - 20, zombie[1] - 20, 40, 40)
        window.blit(zombies_image, (zombie[0], zombie[1]))

        for bullet in bullets[:]:
            bullet_rect = Rect(bullet[0] - 5, bullet[1] - 5, 10, 10)
            if bullet_rect.colliderect(zombie_rect):
                bullets.remove(bullet)
                zombies.remove(zombie)
                score += 1
                if len(zombies) < 5:
                    spawn_zombie()
                break
    hp_text = font.render(f"HP: {int(player_hp)}", True, ('white'))
    score_text = font.render(f"Score: {score}", True, ('white'))
    for bullet in bullets:
        draw.circle(window, (255, 255, 255), (int(bullet[0]), int(bullet[1])), 5)
        bullet[0] += bullet[2] * 2
        bullet[1] += bullet[3] * 2
    for bullet in bullets[:]:
        if bullet[0] < 0 or bullet[0] > 1920 or bullet[1] < 0 or bullet[1] > 1080:
            bullets.remove(bullet)
    window.blit(score_text, (10,50))
    window.blit(hp_text, (10, 10))
    display.update()
    clock.tick(60)