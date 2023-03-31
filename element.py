from pygame import Surface


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
