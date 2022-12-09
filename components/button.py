import pygame

#button class
class Button():
    def __init__(self, x, y, image, image2, scale):
        width = image.get_width()
        height = image.get_height()
        self.image = pygame.transform.scale(image, (int(width * scale), int(height * scale)))
        self.image2 = pygame.transform.scale(image2, (int(width * scale), int(height * scale)))
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.clicked = False

    def draw_and_clicked(self, surface):
        """ write button and return action"""
        press_up_or_down = True
        action = False
        #get mouse position
        pos = pygame.mouse.get_pos()
        image = self.image
        #check mouseover and clicked conditions
        if self.rect.collidepoint(pos) : 
            image = self.image2
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                self.clicked = True
                action = True

        if pygame.mouse.get_pressed()[0] == 0:
            self.clicked = False

        #draw button on screen
        surface.blit(image, (self.rect.x, self.rect.y))

        return action