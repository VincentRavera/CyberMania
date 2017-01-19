import pygame
from threading import Thread

import sys
from src.contants.Constants import WHITE, FPS
import src.inputs.Input as InputModule
from src.facade import Facade
from src.maths import Maths
from src.facade.Facade import fpsClock


class Task(Thread):
    def __init__(self, job):
        Thread.__init__(self)
        self.job = job

    def run(self):
        self.job.do()


class OutputDrawer(object):
    def __init__(self, window, list_to_draw):
        # Set up the window
        pygame.display.set_caption('CyberMania')
        self.window = window
        self.listToDraw = list_to_draw

    def do(self):
        try:
            self.window.fill(WHITE)
            for toDraw in self.listToDraw:
                toDraw.draw(self.window)
            pygame.display.update()
        except pygame.error:
            print("pygame exited, stopping thread")
            Facade.isRunning = False


class InputsListener(object):
    def __init__(self, hero):
        self.hero = hero
        Facade.music.toogle()

    def do(self):
        InputModule.listen(self.hero)


class PositionUpdater(object):
    def __init__(self, list_of_object):
        self.listOfObject = list_of_object

    def do(self):
        for objects in self.listOfObject:
            Maths.update_position_of_object(objects)
