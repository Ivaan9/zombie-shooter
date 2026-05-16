from pygame import *
from random import *
from menu import menu_loop
from settings import *
from sounds import *
import math

init()
mixer.init()
window = display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
clock = time.Clock()
game = True
game_over = False
volume_on = True
player_image = transform.scale(player_image, (100, 100))
zombies_image = transform.scale(zombies_image, (50, 50))
volume_on_image = transform.scale(volume_on_image, (100, 100))
volume_off_image = transform.scale(volume_off_image, (100, 100))
menu_loop()


def reset_game():
    global player_x, player_y, player_hp, score_kills, zombies, zombie_sp, bullets, game_over
    player_y = 850
    player_x = 950
    player_hp = 100
    score_kills = 0
    zombie_sp = 20
    zombies = []
    bullets = []
    spawn_zombie(zombie_sp)
    game_over = False


def spawn_zombie(count):
    for i in range(count):
        zombies.append([
            randint(0, 1920),
            randint(0, 100)
            ])
font = font.Font(None, 36)
reset_game()
while game:
    rect_volume_game = Rect(1650, 100, 80, 80)
    for e in event.get():

        if e.type == QUIT:
            game = False
        if e.type == MOUSEBUTTONDOWN and not game_over:
            if rect_volume_game.collidepoint(mouse.get_pos()):
                volume_on = not volume_on
            else:
                mx, my = mouse.get_pos()
                dx = mx - player_x
                dy = my - player_y
                dist = (dx ** 2 + dy ** 2) ** 0.5
                shot_sound.play()
                if dist != 0:
                    bullets.append([
                        player_x,
                        player_y,
                        dx / dist * 10,
                        dy / dist * 10
                    ])
    if not game_over:
        window.blit(fon_image, (70, 70))
        if volume_on:
            window.blit(volume_on_image, (1650, 80))
            mixer_music.set_volume(0.3)
            shot_sound.set_volume(0.1)

        else:
            window.blit(volume_off_image, (1645, 95))
            mixer_music.set_volume(0)
            shot_sound.set_volume(0)
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
                player_hp -= 1
                if player_hp <= 0:
                    game_over = True
                    zombies.clear()
            if dist != 0:
                zombie[0] += dx / dist * 2
                zombie[1] += dy / dist * 2
        for zombie in zombies[:]:
            zombie_rect = Rect(zombie[0] - 20, zombie[1] - 20, 40, 40)
            window.blit(zombies_image, (zombie[0], zombie[1]))

            for bullet in bullets[:]:
                bullet_rect = Rect(bullet[0] - 5, bullet[1] - 5, 10, 10)
                if bullet_rect.colliderect(zombie_rect):
                    bullets.remove(bullet)
                    zombies.remove(zombie)
                    score_kills += 1
            if len(zombies) < 10:
                spawn_zombie(zombie_sp)
                break
        for bullet in bullets:
            draw.circle(window, (255, 255, 255), (int(bullet[0]), int(bullet[1])), 5)
            bullet[0] += bullet[2] * 2
            bullet[1] += bullet[3] * 2
        for bullet in bullets[:]:
            if bullet[0] < 0 or bullet[0] > 1920 or bullet[1] < 0 or bullet[1] > 1080:
                bullets.remove(bullet)
        score_text = font.render(f"Kills: {score_kills}", True, (WHITE))
        hp_text = font.render(f"HP: {int(player_hp)}", True, (WHITE))
        window.blit(score_text, (205,155))
        window.blit(hp_text, (205, 120))
    else:
        game_over_text = font.render("Game Over", True, (RED))
        restart_text = font.render("Натисніть R для перезапуску", True, (WHITE))
        window.blit(game_over_text, (840, 500))
        window.blit(restart_text, (750, 700))
        keys = key.get_pressed()
        if keys[K_r]:
            reset_game()
    display.update()
    clock.tick(60)