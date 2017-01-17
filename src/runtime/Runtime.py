import pygame
from threading import Thread
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
        while True:
            try:
                self.window.fill(WHITE)
                for toDraw in self.listToDraw:
                    toDraw.draw(self.window)
                pygame.display.update()
                fpsClock.tick(FPS)
            except pygame.error:
                print("pygame exited, stopping thread")
                Facade.isRunning = False
                break


class InputsListener(object):
    def __init__(self, hero):
        print("Task::InputsListener created")
        self.hero = hero

    def do(self):
        print("Task::InputsListener call")
        Facade.music.toogle()
        while True:
            InputModule.listen(self.hero)


class PositionUpdater(object):
    def __init__(self, list_of_object):
        self.listOfObject = list_of_object

    def do(self):
        while True:
            for objects in self.listOfObject:
                Maths.update_position_of_object(objects)
            fpsClock.tick(FPS)
