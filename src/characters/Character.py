from src.spritesheets.JsonReader import MovementManager
from src.spritesheets.SpriteSheet import SpriteSheet
import numpy as np


class Character(object):
    """
    Typical NPC template
    """

    def __init__(self, path_img, path_json):
        """
        Constructor
        """
        self.nom = 'Abstract Character'
        self.position = np.array((50, 50))
        self.speed = np.array((0, 0))
        self.movement_manager = MovementManager(path_img=path_img, path_json=path_json)

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
        if self.speed[0] == 0:
            window.blit(self.movement_manager.get_resting_image(), self.position)
        else:
            window.blit(self.movement_manager.get_next_image(), self.position)


    def sprite_right(self):
        pass

    def sprite_left(self):
        pass


class Hero(Character):
    """
    Player character.
    """

    def __init__(self, path_img, path_json):
        """
        Constructor
        """
        Character.__init__(self, path_img, path_json)

    def jump(self):
        """
        Jumping method
        """
        self.speed[1] -= 5

    def shoot(self):
        """
        Shoot method
        """
        self.speed[1] += 5
