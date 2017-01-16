'''
Created on 16 janv. 2017

@author: vince
'''
from pygame import mixer

class Music(object):
    '''
    classdocs
    '''


    def __init__(self, soundFile):
        '''
        Constructor
        '''
        mixer.init()
        self.current = soundFile
        self.mix = mixer.music
        self.mix.load(self.current)
        self.isPaused = False
        self.isStopped = True
    
    def toogle(self):
        if self.isStopped:
            mixer.music.play(-1, 0.0)
            self.isStopped = False
        else:
            if self.isPaused:
                mixer.music.unpause()
                self.isPaused = False
            else:
                mixer.music.pause()
                self.isPaused = True
    def stop(self):
        mixer.music.fadeout(3000)
        self.isPaused = False
        self.isStopped = True