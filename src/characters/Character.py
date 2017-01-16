'''
Created on 16 janv. 2017

@author: vince
'''
import pygame


class Character(object):
    '''
    classdocs
    '''
    nom = 'Abstract Character'
    pos = (10, 10)
    speed = (0, 0)
    sprite = pygame.image.load('img/error.png')


    def __init__(self, params):
        '''
        Constructor
        '''
        self.nom = 'Abstract Character'
        self.pos = (10, 10)
        self.speed = (0, 0)
        
        
    def moveRight(self):
        '''
        Move's character right
        '''
        
        
    def moveLeft(self):
        '''
        Move's character left
        '''
        
        
    def draw(self, window):
        window.blit(self.sprite, self.pos)