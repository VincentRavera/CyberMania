'''
Created on 16 janv. 2017

@author: vince
'''
import pygame
from src.spritesheets.SpriteSheet import SpriteSheet


class Character(object):
    '''
    classdocs
    '''

    def __init__(self, fileName):
        '''
        Constructor
        '''
        self.nom = 'Abstract Character'
        self.pos = (10, 10)
        self.speed = (0, 0)
        self.sprite = SpriteSheet(fileName)
        
        
    def moveRight(self):
        '''
        Move's character right
        '''
        
        
    def moveLeft(self):
        '''
        Move's character left
        '''
        
        
    def draw(self, window):
        window.blit(self.sprite.imageAt((0, 0, 24, 47)), self.pos)
        
        
        
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