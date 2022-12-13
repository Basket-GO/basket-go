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
        # try to get the previous element bind with this key.
        previous_element = self.get_element(key)
        # check if this element can be overriden.
        if previous_element != None and previous_element.allow_override():
            self.remove_element(key)
        self.__elements.append([key, element])
    def get_element(self, key:str):
        """
        If present returns the element paired with the given key
        else it raises RuntimeError.
        :param str key: the key paired to the game element.
        :return: the game element or None if not found.
        """
        for element in self.__elements:
            if element[0] == key:
                return element[1]
        return None
    def remove_element(self, key:str) -> bool:
        """
        Removes the element paired to the given key.
        :param str key: the key bind with the element to remove.
        :return: whether the element has been removed or not.
        """
        for element in self.__elements:
            if element[0] == key:
                self.__elements.remove(element)
                return True
        return False
    def get_elements(self):
        """
        :return: the game elements.
        """
        return self.__elements