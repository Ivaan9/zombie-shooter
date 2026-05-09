from pygame import *
from settings import *
init()

window = display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
clock = time.Clock()
menu = True

text = font.Font(None, 36)
play_text = text.render("Play", True, (0, 0, 0))
fon_image = image.load("assets/images/fon.jpeg")
mixer.music.load("assets/sounds/menu.mp3")
mixer.music.set_volume(0.3)
mixer.music.play(-1)
def menu_loop():
    global menu
    while menu:
        for e in event.get():
            if e.type == QUIT:
                menu = False
        window.blit(fon_image, (0, 0))
        draw.rect(window, (255,255,255), (820, 440, 250, 50))
        window.blit(play_text, (920, 450))
        clock.tick(60)
        display.update()
menu_loop()