'''
Created on 15 janv. 2017

@author: vince
'''
import pygame
import sys
from pygame.locals import *
from src.music.Music import Music
from src.characters.Character import Hero

if __name__ == '__main__':
    pass


pygame.init()

# Clock
FPS = 60
fpsClock = pygame.time.Clock()

# Set up the window
window = pygame.display.set_mode((800, 600), 0, 32)
pygame.display.set_caption('CyberMania')

# exit the Game function
def exitGame():
    pygame.mixer.music.stop()
    pygame.quit()
    sys.exit()

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# pygame.mixer.music.load('music/test.mp3')
fontObj = pygame.font.Font('freesansbold.ttf', 32)
textSurf = fontObj.render('Yolo world !', True, GREEN, BLUE)
textRect = textSurf.get_rect()
textRect.center = (700, 400)
music = Music('music/test.mp3')
# pygame.mixer.music.play(-1, 0.0)
hero = Hero('img/ssamus.png')

while True:
    window.fill(WHITE)
    hero.draw(window)
    window.blit(textSurf, textRect)
    
    for event in pygame.event.get():
        if event.type == QUIT:
            exitGame()
        if event.type == KEYUP:
            if event.key == K_DOWN:
                music.toogle()
        if event.type == KEYUP:
            if event.key == K_UP:
                music.stop()
    pygame.display.update()
    fpsClock.tick(FPS)
