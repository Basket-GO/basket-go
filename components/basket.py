from element import Element

class Basket(Element):
    def __init__(self, decoration_hoop:Element, first_hoop:Element, second_hoop:Element) -> None:
        super().__init__(decoration_hoop.get_surface(), decoration_hoop.get_x(), decoration_hoop.get_y(), True, False)
        # register our hoops.
        self.__decoration_hoop = decoration_hoop
        self.__first_hoop = first_hoop
        self.__second_hoop = second_hoop
        # make the hoops invisible.
        self.__first_hoop.set_visible(False)
        self.__second_hoop.set_visible(False)
    def hoops(self):
        """
        :return: the two parts of the basket.
        """
        return self.__first_hoop, self.__second_hoop
    def get_decoration_hoop(self) -> Element:
        """
        :return: the decoration hoop that is not interactive.
        """
        return self.__decoration_hoop