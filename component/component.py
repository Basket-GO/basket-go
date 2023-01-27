class Component:
    def __init__(self, x: int = 0, y: int = 0) -> None:
        self.__x = x
        self.__y = y
        self.__action_listeners = []

    def get_x(self) -> int:
        return self.__x

    def get_y(self) -> int:
        return self.__y

    def set_x(self, x: int) -> None:
        self.__x = x

    def set_y(self, y: int) -> None:
        self.__y = y

    def draw(self, surface):
        pass

    def addActionListener(self, action_listener):
        self.__action_listeners.append(action_listener)
