import pygame
from element import Element

class Player():
    def __init__(self, game, name:str) -> None:
        # game's default font.
        self.__font = pygame.font.Font('freesansbold.ttf', 32)
        # set player's game.
        self.__game = game
        # set our player's name.
        self.__name = name
        # init our score.
        self.__score = 0
        # init score text.
        self.__text = None
        pass
    def setup(self) -> None:
        """
        Setup the player into the game.
        """
        self.__text = self.__font.render(str(self.__score), True, (255, 255, 255), None)
        # register the game element.
        self.__game.get_window().register_element("player_" + self.__name + "_score", Element(self.__text, 512, 10, True, True))
    def get_name(self) -> str:
        """
        :return: str: player's name.
        """
        return self.__name
    def get_score(self) -> int:
        """
        :return: int: player's score.
        """
        return self.__score
    def set_score(self, score:int) -> None:
        """
        Define player's score.
        :param: int score: the score to set.
        """
        self.__score = score
        self.__update_score()
    def __update_score(self) -> None:
        """
        Updates player's score text. (UI)
        """
        self.__text = self.__font.render(str(self.__score), True, (255, 255, 255), None)
        self.__game.get_window().register_element("player_" + self.__name + "_score", Element(self.__text, 512, 10, True, True))