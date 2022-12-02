class Window():
    def __init__(self) -> None:
         # game elements (objects, background etc.)
        self.__elements = []
    def register_element(self, key:str, element):
        """
        Register a game element into the cache.
        :param str key: the key to pair to the given element.
        :param object element: the element to store.
        """
        self.__elements.append([key, element])
    def get_element(self, key:str):
        """
        If present returns the element paired with the given key
        else it raises RuntimeError.
        :param str key: the key paired to the game element.
        :return: the game element.
        """
        for element in self.__elements:
            if element[0] == key:
                return element[1]
        raise RuntimeError("element not found for key: ", key)
    def get_elements(self):
        """
        :return: the game elements.
        """
        return self.__elements