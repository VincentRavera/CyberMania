'''
Created on 16 janv. 2017

@author: vince
'''
import sys
import pygame
from pygame.constants import QUIT, KEYDOWN, K_RIGHT, K_LEFT, K_SPACE, K_p, KEYUP
from src.facade.Facade import music


def exitGame():
    pygame.mixer.music.stop()
    pygame.quit()
    sys.exit()


def musicInputs(event):
    if event.type == KEYDOWN:
        if event.key == K_p:
            music.mute()


def listen(hero):
    for event in pygame.event.get():
        if event.type == QUIT:
            exitGame()
        if event.type == KEYDOWN:
            if event.key == K_RIGHT:
                print("d R")
                hero.moveRight()
            if event.key == K_LEFT:
                print("d L")
                hero.moveLeft()
            if event.key == K_SPACE:
                hero.jump()
        if event.type == KEYUP:
            if event.key == K_RIGHT:
                print("u R")
                hero.stopMoving()
            if event.key == K_LEFT:
                print("u L")
                hero.stopMoving()
        musicInputs(event)