'''
Created on 16 janv. 2017

@author: vince
'''
from pygame import mixer

class Sound(object):
    '''
    classdocs
    '''


    def __init__(self, soundFile):
        '''
        Constructor
        '''
        self.path = soundFile
        self.mix = mixer.Sound


    def play(self):
        self.mix.Sound(self.path)