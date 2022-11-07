import pygame
import sys

class Game():
    def __init__(self, screen:pygame.Surface, players:list, img_location:str, sound_location:str) -> None:
        # get the actual display screen.
        self.__screen = screen
        # get the actuals players playing.
        self.__players = players
        # get the actual background.
        self.__background = pygame.image.load(img_location + "terrain_basket_sans_public.png")
        self.__background = pygame.transform.scale(self.__background, (1024, 390))
        self.__crow_arms_down = pygame.image.load(img_location + "terrain_basket_public_mains_baissees.png")
        self.__crow_arms_down = pygame.transform.scale(self.__crow_arms_down, (1024, 250))
        self.__ball = pygame.image.load(img_location + "basket-ball.png")
        self.__ball = pygame.transform.scale(self.__ball, (70, 70))
    
    def setup(self):
        """
        Setup the ressources (background image, audio, etc.)
        """
        x,y = 30, 400
        while True:
            self.__screen.blit(self.__background, (0, 250))
            self.__screen.blit(self.__crow_arms_down, (0, 0))
            self.__screen.blit(self.__ball, (x, y))
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                elif event.type == pygame.MOUSEMOTION and pygame.mouse.get_pressed()[0] == True:
                    x = pygame.mouse.get_pos()[0] - 30
                    y = pygame.mouse.get_pos()[1] - 30
                    self.__screen.blit(self.__ball, (x, y))
            pygame.display.update()
    def end(self):
        pass
    
