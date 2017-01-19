import pygame
from src.characters.Character import Hero
from src.contants.Constants import DISPLAY_SURF, FPS
from src.runtime.Runtime import Task, OutputDrawer, PositionUpdater, InputsListener
from src.facade.Facade import isRunning, fpsClock

if __name__ == '__main__':
    pass


pygame.init()
window = pygame.display.set_mode(DISPLAY_SURF)

hero = Hero('img/keney_p1_animation/Player.png')
listToDraw = list()
listToDraw.append(hero)

runtime = Task(OutputDrawer(window, listToDraw))

positionUpdater = Task(PositionUpdater(listToDraw))

inputsListener = Task(InputsListener(hero))

runtime.start()
positionUpdater.start()
inputsListener.start()

while isRunning:
    runtime.join()
    positionUpdater.join()
    inputsListener.join()

    fpsClock.tick(FPS)

    runtime.run()
    positionUpdater.run()
    inputsListener.run()