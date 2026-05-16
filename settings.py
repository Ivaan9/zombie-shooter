from pygame import *

mixer.init()

WINDOW_WIDTH = 1920
WINDOW_HEIGHT = 1080
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)


fon_image_menu = image.load("assets/images/fon_menu.jpeg")
fon_image = image.load("assets/images/fon_game.png")
player_image = image.load("assets/images/player.png")
zombies_image = image.load("assets/images/zombies.png")
volume_on_image = image.load("assets/images/volume.on.png")
volume_off_image = image.load("assets/images/volume.off.png")
shot_sound = mixer.Sound("assets/sounds/shot.mp3")
mixer.music.load("assets/sounds/menu.mp3")
