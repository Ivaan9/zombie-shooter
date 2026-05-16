from pygame import *
from settings import *
init()

window = display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
clock = time.Clock()
menu = True
volume_on = True
text = font.Font(None, 36)
play_text = text.render("Play", True, (0, 0, 0))
volume_on_image = transform.scale(volume_on_image, (100, 100))
volume_off_image = transform.scale(volume_off_image, (100, 100))
mixer.music.play(-1)
def menu_loop():
    global menu
    global volume_on
    while menu:
        for e in event.get():
            if e.type == QUIT:
                menu = False

            if e.type == MOUSEBUTTONDOWN:
                if play.collidepoint(mouse.get_pos()):
                    menu = False
                if rect_volume_menu.collidepoint(mouse.get_pos()):
                    volume_on = not volume_on
        rect_volume_menu = Rect(1650, 100, 80, 80)
        window.blit(fon_image_menu, (0, 0))
        play = Rect(820, 440, 250, 50)
        window.blit(play_text, (920, 450))
        if volume_on:

            window.blit(volume_on_image, (1650, 80))
            mixer.music.set_volume(1)

        else:
            window.blit(volume_off_image, (1645, 95))
            mixer.music.set_volume(0)
        clock.tick(60)
        display.update()
