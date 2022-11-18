from pygame import Surface

class Element():
    def __init__(self, surface:Surface, x:int, y:int) -> None:
        self.__surface = surface
        self.__x = x
        self.__y = y
        pass
    def get(self) -> tuple:
        """
        :return: the whole element.
        """
        return (self.__surface, (self.__x, self.__y))
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
    def set_x(self, x:int):
        """
        Set the x position of the moveable element.
        :param int x: the x position of the element.
        """
        self.__x = x
    def set_y(self, y:int):
        """
        Set the y position of the moveable element.
        :param int y: the y position of the element.
        """
        self.__y = y