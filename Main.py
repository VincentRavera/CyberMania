'''
Created on 15 janv. 2017

@author: vince
'''
import pygame
from pygame.locals import *
from src.characters.Character import Hero
import src.inputs.Input as inputs
from threading import Thread
from src.music.Music import Music
import sys

if __name__ == '__main__':
    pass
# Clock
FPS = 60

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

displaySurf = (1024, 668)# Display Size



class Task(Thread):

    def __init__(self, job):
        Thread.__init__(self)
        self.job = job


    def run(self):
        self.job.do()

class Runtime(object):
    def __init__(self, window, hero):
        self.fpsClock = pygame.time.Clock()
        # Set up the window
        pygame.display.set_caption('CyberMania')
        self.window = window
        self.hero = hero


    def do(self):
        while True:
            try :
                self.window.fill(WHITE)
                self.hero.draw(window)
                # inputs.listen(hero)
                pygame.display.update()
                self.fpsClock.tick(FPS)
            except pygame.error:
                print("pygame exited, stopping thread")
                break


class PositionUpdater(object):
    def __init__(self, hero):
        self.muse = Music('music/test.mp3')
        self.hero = hero


    def do(self):
        self.muse.toogle()
        while True:
            inputs.listen(self.hero, self.muse)

pygame.init()
window = pygame.display.set_mode(displaySurf)

hero = Hero('img/ssamus.png')

runtime = Task(Runtime(window, hero))

positionUpdater = Task(PositionUpdater(hero))

runtime.start()
positionUpdater.start()
