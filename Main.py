import pygame
from src.characters.Character import Hero
from src.contants.Constants import DISPLAY_SURF, FPS
from src.runtime.Runtime import Task, OutputDrawer, PositionUpdater, InputsListener
from src.facade.Facade import isRunning, fpsClock

if __name__ == '__main__':
    pass


pygame.init()
window = pygame.display.set_mode(DISPLAY_SURF)

hero = Hero('img/keney_p1_animation/Player.png', 'img/keney_p1_animation/Player.json')
listToDraw = list()
listToDraw.append(hero)

drawer = Task(OutputDrawer(window, listToDraw))

positionUpdater = Task(PositionUpdater(listToDraw))

inputsListener = Task(InputsListener(hero))

drawer.start()
positionUpdater.start()
inputsListener.start()

while isRunning:
    drawer.join()
    positionUpdater.join()
    inputsListener.join()

    fpsClock.tick(FPS)

    drawer.run()
    positionUpdater.run()
    inputsListener.run()
