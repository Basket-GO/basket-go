from element import Element
from pygame import Surface


class Ball(Element):
    def __init__(self, surface: Surface, x: int, y: int, visible: bool = True) -> None:
        """Class for the ball.

        Args:
            surface (Surface): The window where the ball will be drawn.
            x (int): the x coordinate of the ball.
            y (int): the y coordinate of the ball.
            visible (bool, optional): If the ball is visible . Defaults to True.
        """
        super().__init__(surface, x, y, visible, False)
        # this states whether the ball is released or not.
        self.__is_released = False

    def is_released(self) -> bool:
        """Check if the ball is released or not.

        Returns:
            bool: whether the ball is released or not.
        """
        return self.__is_released

    def set_released(self, released: bool) -> None:
        """Set the ball as released or not.

        Args:
            released (bool): the release state of the ball.
        """
        self.__is_released = released

    def respawn(self) -> None:
        """Reset the ball's position to it's initial location
        and set the ball as not released.
        """
        self.set_x(self.get_initial_x())
        self.set_y(self.get_initial_y())
        self.set_released(False)
