
from pygame import mixer


class Sound(object):
    """
    Sound effect for Characters and Objects
    """
    def __init__(self, sound_file):
        """
        Constructor
        """
        self.path = sound_file
        self.mix = mixer.Sound

    def play(self):
        self.mix.Sound(self.path)
