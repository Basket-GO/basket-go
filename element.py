from pygame import Surface
from math import (sqrt)


class Element():
    def __init__(self, surface: Surface, x: int, y: int, visible: bool = True, allow_override: bool = False) -> None:
        """The base class for all the elements in the game.

        Args:
            surface (Surface): The surface where the element will be drawn.
            x (int): The x coordinate of the element.
            y (int): The y coordinate of the element.
            visible (bool, optional): If the element is visble or not . Defaults to True.
            allow_override (bool, optional): If the element can be override. Defaults to False.
        """
        self.__surface = surface
        # those are the inital x and y coordinates. (those coordinates are immutable)
        self.__ix, self.__iy = x, y
        # those are the mutable x and y coordinates.
        self.__x, self.__y = x, y
        self.__visible = visible
        self.__allow_override = allow_override
        pass
    def set_surface(self, surface:Surface):
        self.__surface = surface
    def get(self) -> tuple:
        """
        :return: the whole element.
        """
        return (self.__surface, (self.__x, self.__y))
    def get_position(self) -> tuple:
        """
        :return: the x & y coordinates.
        """
        return self.__x, self.__y
    def get_surface(self) -> Surface:
        """
        :return: the surface.
        """
        return self.__surface
    def get_initial_x(self, relative:bool):
        """
        :param relative bool: whether whe should get it from the center or not.
        :return: the initial immutable x coordinate of the element.
        """
        return self.__ix if not relative else (self.get_surface().get_size()[0] / 2) + self.__ix
    def get_initial_y(self, relative:bool):
        """
        :param relative bool: whether we should get it from the center or not.
        :return: the initial immutable x coordinate of the element.
        """
        return self.__iy if not relative else (self.get_surface().get_size()[0] / 2) + self.__iy
    def get_x(self):
        """
        :return: the live x position of the element.
        """
        return self.__x

    def get_y(self):
        """
        :return: the live y position of the element.
        """
        return self.__y
    def allow_override(self):
        """
        :return: whether the element can be overrident or not.
        (another element can erase this one.)
        """
        return self.__allow_override

    def is_visible(self):
        """
        :return: whether the element is visible or not. (Note it can still interact.)
        """
        return self.__visible

    def set_visible(self, visible: bool):
        """
        Set the visibility of the element.
        :param: bool visible: whether the element is visible or not.
        """
        self.__visible = visible

    def set_x(self, x: int):
        """
        Set the x position of the element.
        :param int x: the x position of the element.
        """
        self.__x = x

    def set_y(self, y: int):
        """
        Set the y position of the element.
        :param int y: the y position of the element.
        """
        self.__y = y
    def center_x(self):
        """
        :return: the x center of image.
        """
        return (self.get_surface().get_size()[0] / 2) + self.get_x()
    def center_y(self):
        """
        :return: the y center of image.
        """
        return (self.get_surface().get_size()[0] / 2) + self.get_y()
    def distance_two_points(self, x, y, x1, y1):
        """
        :return: the euclidian distance between 4 points in the space.
        :param int x: the x position to compare with.
        :param int y: the y position to compare with.
        :param int x1: the x' position to compare with.
        :param int y1: the y' position to compare with.
        """
        
        return sqrt(((x - x1) ** 2) + ((y - y1) ** 2))
    def distance(self, x, y, from_center:bool):
        """
        :return: the euclidian distance between this element and x, y coordinates
        :param int x: the x position to compare with.
        :param int y: the y position to compare with.
        :param bool from_center: whether we should calculate the euclidian distance
        from the center of the surface or not.
        """
        return sqrt(((self.center_x() - x) ** 2) + ((self.center_y() - y) ** 2)) if from_center else sqrt((self.get_x() - x) ** 2) + ((self.get_y() - y) ** 2)
    def distance_element(self, element, from_center:bool):
        """
        :return: the euclidian distance between this element and another one.
        :param Element element: the element to compare with.
        :param bool from_center: whether we should calculate the euclidian distance
        from the center of the surface or not.
        """
        return self.distance(element.get_x(), element.get_y()) if not from_center else self.distance(element.center_x(), element.center_y())