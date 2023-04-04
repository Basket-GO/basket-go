from element import Element
from pygame import Surface
import pygame
from math import (pi, atan)

class Ball(Element):
    def __init__(self, surface: Surface, x: int, y: int, visible: bool = True) -> None:
        super().__init__(surface, x, y, visible, False)
        # this states whether the ball is released or not.
        self.__is_released = False
        self.__has_rebounced = False
        self.__has_grnd_rebounced = False
    def is_released(self) -> bool:
        """
        :return: whether the ball is released or not.
        """
        return self.__is_released
    def set_released(self, released:bool) -> None:
        """
        Set the ball as released or not.
        :param bool released: the release state of the ball.
        """
        self.__is_released = released
    def respawn(self) -> None:
        """
        Reset the ball's position to it's initial location
        and set the ball as not released.
        """
        self.set_x(self.get_initial_x())
        self.set_y(self.get_initial_y())
        self.set_released(False)
    def __arctan(self, x, y):
        """
        :return: the arctan of an angle based on the x and y position of this element.
        :param float x: an x coordinate.
        :param float y: an y coordinate.
        """
        if y == 0:  # Sur l'axe des ordonnées
            if x >= 0:
                return 0
            else:
                return pi
        elif x > 0:  # Premier et quatrième quadrants
            return -atan(y/x)
        else:
            if y > 0:  # Troisième quadrant
                return atan(x/y) - pi/2
            else:  # Second quadrant
                return atan(x/y) + pi/2
    def rotate(self, angle):
        orig_rect = self.get_surface().get_rect()
        rot_image = pygame.transform.rotate(self.get_surface(), angle)
        rot_rect = orig_rect.copy()
        rot_rect.center = rot_image.get_rect().center
        rot_image = rot_image.subsurface(rot_rect).copy()
        rot_image.unlock()
        self.set_surface(rot_image)
    def rebounce(self, ox, oy, alpha):
        """
        Makes the ball rebounce.
        :param float ox: the x point of impact.
        :param float oy: the y point of impact.
        :param float alpha: the alpha angle.
        """
        cx = self.center_x()
        cy = self.center_y()
        if ox - cx == 0:
            teta = pi / 2 if ox > cx else -(pi / 2)
        elif ox - cx < 0:
            teta = pi + self.__arctan((ox - cx), (oy - cy))
        elif ox - cx > 0:
            teta = self.__arctan((ox - cx), (oy - cy))
        return pi + 2 * teta - alpha
    def has_rebounced(self):
        return self.__has_rebounced
    def set_rebounced(self, has_rebounced:bool):
        self.__has_rebounced = has_rebounced
    def has_grnd_rebounced(self):
        return self.__has_grnd_rebounced
    def set_grnd_rebounced(self, has_grnd_rebounced:bool):
        self.__has_grnd_rebounced = has_grnd_rebounced