import pygame
import component.component as Component


class Interface():
    def __init__(self, button: dict, background: str, text: dict):

        self.button = button
        self.background = background
        self.text = text
        self.__elements = []
        pygame.init()
        icon = pygame.image.load("./img/Logo.png")
        pygame.display.set_icon(icon)
        pygame.display.set_caption("ʙᴀsᴋᴇᴛ ɢᴏ !")
        self.window = pygame.display.set_mode((1024, 640))
        self.fond = pygame.image.load(self.background)
        pygame.mouse.set_pos(
            (self.fond.get_width()/2, self.fond.get_height()/2))

    def register_component(self, Component):
        """
        Registers component from the interface to a list
        :param component: the component to register.
        """
        self.__elements.append(Component)

    def get_component(self, Component):
        """
        Gets the component from the interface.
        :param component: the component to get.
        :return: the component.
        """
        for element in self.__elements:
            if element == Component:
                return element
        raise RuntimeError("Component not found.")

    def remove_component(self, Component):
        """
        Removes the component from the interface.
        :param component: the component to remove.
        :return: whether the component has been removed or not.
        """
        for element in self.__elements:
            if element == Component:
                self.__elements.remove(element)
                return True
        return False

    def get_components(self):
        """
        :return: the components.
        """
        return self.__elements

    def setup(self):
        while True:
            self.register_component(self.button)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
            self.window.blit(self.fond, (0, 0))
            self.get_component(self.button).draw(self.window)

            pygame.display.flip()
