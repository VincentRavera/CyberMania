from pygame import mixer, time
from src.contants.Constants import MUSIC_FADEOUT, ONE_SEC_2_MILI


class Music(object):
    """
    classdocs
    """
    def __init__(self, sound_file):
        """
        Constructor
        """
        mixer.init()
        self.current = sound_file
        self.mix = mixer.music
        self.mix.load(self.current)
        self.isPaused = False
        self.isStopped = True
        self.isMute = self.mix.get_volume()

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
        mixer.music.fadeout(MUSIC_FADEOUT)
        self.isPaused = False
        self.isStopped = True

    def mute(self):
        a = self.mix.get_volume()
        if a == 0:
            self.mix.set_volume(self.isMute)
        else:
            self.isMute = self.mix.get_volume()
            self.mix.set_volume(0)
    
    def load_this(self, string):
        if self.current != string:
            mixer.music.fadeout(MUSIC_FADEOUT)
            time.wait(MUSIC_FADEOUT)
