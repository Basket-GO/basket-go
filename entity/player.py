import pygame
from element import Element

class Player():
    def __init__(self, game, name:str) -> None:
        # set player's game.
        self.__game = game
        # set our player's name.
        self.__name = name
        # init our score.
        self.__score = 0
        pass
    def setup(self) -> None:
        """
        Setup the player into the game.
        """
        # game's default font.
        font = pygame.font.Font('freesansbold.ttf', 32)
        text = font.render(str(self.__score), True, (255, 255, 255), None)
        # register the game element.
        self.__game.get_window().register_element("player_" + self.__name + "_score", Element(text, 512, 10))
    def get_name(self) -> str:
        """
        :return: str: player's name.
        """
        return self.__name
    def get_score(self) -> int:
        """
        :return: int: player's score.
        """
    def set_score(self, score:int) -> None:
        """
        Define player's score.
        :param: int score: the score to set.
        """
        self.__score = score