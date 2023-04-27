from element import Element
from pygame import Surface

class Hoop(Element):
    def __init__(self, surface: Surface, x: int, y: int, visible: bool = True, allow_override: bool = False) -> None:
        super().__init__(surface, x, y, visible, allow_override)
        self.__has_been_touched = False
    def has_been_touched(self) -> bool:
        return self.__has_been_touched
    def set_touched(self, touched:bool) -> None:
        self.__has_been_touched = touched