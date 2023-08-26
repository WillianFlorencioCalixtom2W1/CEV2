import pygame
import helicopter
import enemy_heli
import boat
import sprites
import random

pygame.mixer.pre_init(44100, -16, 1,512)
pygame.init() 

pygame.display.set_icon(sprites.icon)
display_width = 800
display_height = 600
game.display = pygame.display.set_mode((display_width, display_height))

font = "sound_alert.wav"
def message_to_screen(massage, textfont, size, color):
    my_font = pygame.font.Font(textfont, size)
    my_message = my_font.render(message, 0, color)
    return my_message
white = (255, 255, 255)
black = (0, 0, 0)
gray = (50, 50, 50)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
yellow = (255, 255, 0)

for convert_sprite in  sprites.all_sprites:
    convert_sprite.convert_apha()

    clock = paygame.time.Clock()
FPS = 30

player = heilicopter.Helicopter(100, display_heigth/2-40)
moving = True
godmode = false

score = 0
heighscore_file = open('highscore.dat', "r")
highscore_int = int(highscore_file.read)

cloud_x
