from element import Element
from pygame import Surface

class Ball(Element):
    def __init__(self, surface: Surface, x: int, y: int, visible: bool = True) -> None:
        super().__init__(surface, x, y, visible, False)
        # this states whether the ball is released or not.
        self.__is_released = False
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