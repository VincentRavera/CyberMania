
from src.spritesheets.SpriteSheet import SpriteSheet
import numpy as np


class Character(object):
    """
    Typical NPC template
    """

    def __init__(self, file_name):
        """
        Constructor
        """
        self.nom = 'Abstract Character'
        self.position = np.array((50, 50))
        self.speed = np.array((0, 0))
        self.sprite = SpriteSheet(file_name)

    def move_right(self):
        """
        Move's character right
        """
        self.speed[0] += 5
        self.sprite_right()

    def move_left(self):
        """
        Move's character left
        """
        self.speed[0] -= 5
        self.sprite_left()

    def stop_moving(self):
        self.speed[0] = 0

    def draw(self, window):
        window.blit(self.sprite.image_at((0, 0, 24, 47)), self.position)

    def sprite_right(self):
        pass

    def sprite_left(self):
        pass


class Hero(Character):
    """
    Player character.
    """

    def __init__(self, file_name):
        """
        Constructor
        """
        Character.__init__(self, file_name)

    def jump(self):
        """
        Jumping method
        """
        self.speed[1] += 5

    def shoot(self):
        """
        Shoot method
        """
        self.speed[1] += 5
