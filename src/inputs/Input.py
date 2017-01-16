'''
Created on 16 janv. 2017

@author: vince
'''
import sys
import pygame
from pygame.constants import QUIT, KEYDOWN, K_RIGHT, K_LEFT, K_SPACE, K_p


def exitGame():
    pygame.mixer.music.stop()
    pygame.quit()
    sys.exit()


def musicInputs(event, music):
    if event.type == KEYDOWN:
        if event.key == K_p:
            music.mute()


def listen(hero, music):
    for event in pygame.event.get():
        if event.type == QUIT:
            exitGame()
        if event.type == KEYDOWN:
            if event.key == K_RIGHT:
                hero.moveRight()
            if event.key == K_LEFT:
                hero.moveLeft()
            if event.key == K_SPACE:
                hero.jump()
        musicInputs(event, music)