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

        self.hovered = False
        self.hover_sound = pygame.mixer.Sound("./sound/blipshort1.wav")

    def draw_and_clicked(self, surface):
        """ write button and return action"""
        action = False
        #get mouse position
        image = self.image
        pos = pygame.mouse.get_pos()
        #check mouseover and clicked conditions
        if self.rect.collidepoint(pos):
            if not self.hovered:
                self.hovered = True
                if self.hovered:
                    self.hover_sound.play()
            image = self.image2
            if pygame.mouse.get_pressed()[0] == 1 :
                action = True
        else:
            self.hovered = False
            
        #draw button on screen
        surface.blit(image, (self.rect.x, self.rect.y))

        return action
