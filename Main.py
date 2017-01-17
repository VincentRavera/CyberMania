'''
Created on 15 janv. 2017

@author: vince
'''
import pygame
from pygame.locals import *
from src.characters.Character import Hero
from src.contants.Constants import DISPLAY_SURF
from src.runtime.Runtime import Task, OutputDrawer, PositionUpdater, InputsListener

if __name__ == '__main__':
    pass




pygame.init()
window = pygame.display.set_mode(DISPLAY_SURF)

hero = Hero('img/ssamus.png')
listToDraw = []
listToDraw.append(hero)

runtime = Task(OutputDrawer(window, listToDraw))

positionUpdater = Task(PositionUpdater(listToDraw))

inputsListener = Task(InputsListener(hero))

runtime.start()
positionUpdater.start()
inputsListener.start()
