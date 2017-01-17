import sys
import pygame
from pygame.constants import QUIT, KEYDOWN, K_RIGHT, K_LEFT, K_SPACE, K_p, KEYUP
from src.facade.Facade import music


def exit_game():
    pygame.mixer.music.stop()
    pygame.quit()
    sys.exit()


def music_inputs(event):
    if event.type == KEYDOWN:
        if event.key == K_p:
            music.mute()


def listen(hero):
    for event in pygame.event.get():
        if event.type == QUIT:
            exit_game()
        if event.type == KEYDOWN:
            if event.key == K_RIGHT:
                hero.move_right()
            if event.key == K_LEFT:
                hero.move_left()
            if event.key == K_SPACE:
                hero.jump()
        if event.type == KEYUP:
            if event.key == K_RIGHT:
                hero.stop_moving()
            if event.key == K_LEFT:
                hero.stop_moving()
        music_inputs(event)
