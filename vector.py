from math import sqrt

class Vector:
    def __init__(self, x:int, y:int) -> None:
        self.__x = x
        self.__y = y
        pass
    def get_x(self) -> int:
        """
        :return: the x coordinate of the vector.
        """
        return self.__x
    def get_y(self) -> int:
        """
        :return: the y coordinate of the vector.
        """
        return self.__y
    def set_x(self, x:int) -> None:
        """
        Define vector's x coordinate.
        :param: int x: the x coordinate to update.
        """
        self.__x = x
    def set_y(self, y:int) -> None:
        """
        Define vector's y coordinate.
        :param: int y: the y coordinate to update.
        """
        self.__y = y
    def normalize(self) -> int:
        """
        :return: the normalized vector.
        """
        return sqrt(self.__x**2 + self.__y**2)