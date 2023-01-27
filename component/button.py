import pygame
import component as Component
# button class


class Button(Component):
    def __init__(self, x, y, image, hoover):
        super().__init__(x, y)
        self.__image = image
        self.__hoover = hoover
        self.__clicked = False

    def draw(self, surface):
        # get mouse position
        pos = pygame.mouse.get_pos()
        image = self.__image

        # check mouseover and clicked conditions
        if image.get_rect().collidepoint(pos):
            image = self.__hoover
            if pygame.mouse.get_pressed()[0] == 1 and self.__clicked == False:
                self.__clicked = True
        elif pygame.mouse.get_pressed()[0] == 0:
            self.__clicked = False
        # draw button on screen
        surface.blit(image, (self.rect.x, self.rect.y))
