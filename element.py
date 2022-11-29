from pygame import Surface

class Element():
    def __init__(self, surface:Surface, x:int, y:int, visible:bool=True) -> None:
        self.__surface = surface
        # those are the inital x and y coordinates. (those coordinates are immutable)
        self.__ix, self.__iy = x, y
        # those are the mutable x and y coordinates.
        self.__x, self.__y = x, y
        self.__visible = visible
        pass
    def get(self) -> tuple:
        """
        :return: the whole element.
        """
        return (self.__surface, (self.__x, self.__y))
    def get_surface(self) -> Surface:
        """
        :return: the surface.
        """
        return self.__surface
    def get_initial_x(self):
        """
        :return: the initial immutable x coordinate of the element.
        """
        return self.__ix
    def get_initial_y(self):
        """
        :return: the initial immutable x coordinate of the element.
        """
        return self.__iy
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
    def get_surface(self):
        """
        :return: the element surface.
        """
        return self.__surface
    def is_visible(self):
        """
        :return: whether the element is visible or not. (Note it can still interact.)
        """
        return self.__visible
    def set_visible(self, visible:bool):
        """
        Set the visibility of the element.
        :param: bool visible: whether the element is visible or not.
        """
        self.__visible = visible
    def set_x(self, x:int):
        """
        Set the x position of the element.
        :param int x: the x position of the element.
        """
        self.__x = x
    def set_y(self, y:int):
        """
        Set the y position of the element.
        :param int y: the y position of the element.
        """
        self.__y = y