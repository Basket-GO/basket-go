from element import Element

class Basket():
    def __init__(self, first_hoop:Element, second_hoop:Element) -> None:
        # register our hoops.
        self.__first_hoop = first_hoop
        self.__second_hoop = second_hoop
    def hoops(self):
        """
        :return: the two parts of the basket.
        """
        return self.__first_hoop, self.__second_hoop