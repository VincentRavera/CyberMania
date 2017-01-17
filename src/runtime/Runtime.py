'''
Created on 17 janv. 2017

@author: vince
'''
import time
import pygame
from threading import Thread
from src.contants.Constants import WHITE, FPS
import src.inputs.Input as inputs
from src.facade.Facade import music
from src.maths import Maths
from src.contants.Constants import ONE_SEC_2_MILI
from src.facade.Facade import fpsClock


class Task(Thread):

    def __init__(self, job):
        Thread.__init__(self)
        self.job = job


    def run(self):
        self.job.do()


class OutputDrawer(object):
    def __init__(self, window, listToDraw):
        # Set up the window
        pygame.display.set_caption('CyberMania')
        self.window = window
        self.listToDraw = listToDraw


    def do(self):
        while True:
            try :
                self.window.fill(WHITE)
                for toDraw in self.listToDraw:
                    toDraw.draw(self.window)
                pygame.display.update()
                fpsClock.tick(FPS)
            except pygame.error:
                print("pygame exited, stopping thread")
                break


class InputsListener(object):
    def __init__(self, hero):
        print("Task::InputsListener created")
        self.hero = hero


    def do(self):
        print("Task::InputsListener call")
        music.toogle()
        while True:
            inputs.listen(self.hero)

class PositionUpdater(object):
    def __init__(self, listOfObject):
        self.listOfObject = listOfObject


    def do(self):
        while True :
            t0 = time.time()*1000
            for objects in self.listOfObject:
                Maths.updatePositionOfObject(objects)
            dt = time.time()*1000 - t0
            if dt < ONE_SEC_2_MILI/FPS:
                time.sleep((ONE_SEC_2_MILI/FPS-dt)/ONE_SEC_2_MILI)
