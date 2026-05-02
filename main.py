from pygame import *
from random import *
import math
init()
window = display.set_mode((800, 600))
clock = time.Clock()
game = True

player_y = 400
player_x = 300
player_hp = 100

score = 0
zombies = []
bullets = []
def spawn_zombie():
    for i in range(10):
        zombies.append([randint(0, 800), randint(0, 100)])
spawn_zombie()

font = font.Font(None, 36)

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    window.fill('green')
    keys = key.get_pressed()
    if keys[K_w]:
        player_y -= 5
    if keys[K_s]:
        player_y += 5
    if keys[K_a]:
        player_x -= 5
    if keys[K_d]:
        player_x += 5


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
    draw.circle(window, 'red', (player_x, player_y), 20)
    if e.type == MOUSEBUTTONDOWN:
        mx, my = mouse.get_pos()

        dx = mx - player_x
        dy = my - player_y
        dist = (dx ** 2 + dy ** 2) ** 0.5

        if dist != 0:
            bullets.append([
                player_x,
                player_y,
                dx / dist * 10,
                dy / dist * 10
            ])
    for zombie in zombies[:]:
        # Створюємо прямокутник для зомбі (x, y, ширина, висота)
        # Якщо радіус 20, то ширина і висота будуть 40
        zombie_rect = Rect(zombie[0] - 20, zombie[1] - 20, 40, 40)

        # Малюємо зомбі
        draw.circle(window, (0, 0, 255), (int(zombie[0]), int(zombie[1])), 20)

        for bullet in bullets[:]:
            # Створюємо прямокутник для кулі (наприклад, розміром 10x10)
            bullet_rect = Rect(bullet[0] - 5, bullet[1] - 5, 10, 10)

            # Перевіряємо зіткнення прямокутників
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
        if bullet[0] < 0 or bullet[0] > 800 or bullet[1] < 0 or bullet[1] > 600:
            bullets.remove(bullet)
    window.blit(score_text, (10,50))
    window.blit(hp_text, (10, 10))
    display.update()
    clock.tick(60)