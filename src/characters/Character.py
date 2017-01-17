'''
Created on 16 janv. 2017

@author: vince
'''
from src.spritesheets.SpriteSheet import SpriteSheet
import numpy as np


class Character(object):
    '''
    classdocs
    '''

    def __init__(self, fileName):
        '''
        Constructor
        '''
        self.nom = 'Abstract Character'
        self.position = np.array((50, 50))
        self.speed = np.array((0,0))
        self.sprite = SpriteSheet(fileName)


    def moveRight(self):
        '''
        Move's character right
        '''
        self.speed[0] = self.speed[0] + 1
        self.SriteRight()


    def moveLeft(self):
        '''
        Move's character left
        '''
        self.speed[0] = self.speed[0] - 1
        self.SpritLeft()


    def stopMoving(self):
        self.speed[0] = 0


    def draw(self, window):
        window.blit(self.sprite.imageAt((0, 0, 24, 47)), self.position)


    def SpritLeft(self):
        pass


    def SriteRight(self):
        pass


class Hero(Character):
    '''
    classdocs
    '''

    def __init__(self, fileName):
        '''
        Constructor
        '''
        Character.__init__(self, fileName)


    def jump(self):
        '''
        Jumping method
        '''
        
        
    def shoot(self):
        '''
        Shoot method
        '''