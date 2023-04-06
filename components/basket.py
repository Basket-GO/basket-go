from element import Element

class Basket(Element):
    def __init__(self, decoration_hoop:Element, first_hoop:Element, second_hoop:Element) -> None:
        super().__init__(decoration_hoop.get_surface(), decoration_hoop.get_x(), decoration_hoop.get_y(), True, False)
        # register our hoops.
        self.__first_hoop = first_hoop
        self.__second_hoop = second_hoop
        # make the hoops invisible.
        self.__first_hoop.set_visible(False)
        self.__second_hoop.set_visible(False)
    def move(self, x:int, y:int) -> None:
        """
        Moves the decoration and the hoops. More convenient hehe :D
        :param x int: the x coordinate where the basket should move.
        :param y int: the y coordinate where the basket should move.
        """
        h1, h2 = self.hoops()
        h1.set_x(h1.get_x() + (x - self.get_x()))
        h1.set_y(h1.get_y() + (y - self.get_y()))
        h2.set_x(h2.get_x() + (x - self.get_x()))
        h2.set_y(h2.get_y() + (y - self.get_y()))
        self.set_x(x)
        self.set_y(y)
    def hoops(self):
        """
        :return: the two parts of the basket.
        """
        return self.__first_hoop, self.__second_hoop
    def is_within(self, x:float, y:float, vy:float) -> bool:
        """
        :param x float: the x coordinate to check for.
        :param y float: the y coordinate to check for.
        :param vy float: the y coordinate of the ball's vector.
        :return: whether the x & y coordinates are within the basket hoops.
        """
        # retrieve hoops.
        hoop_1, hoop_2 = self.hoops()
        return x > hoop_1.center_x() and x < hoop_2.center_x() and y > hoop_1.center_y() and vy > 0