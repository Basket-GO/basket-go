import pygame
from element import Element


class Player():
    def __init__(self, game: str, name: str) -> None:
        """Player class.

        Args:
            game (str): The game where the player is playing.
            name (str): The name of the player.
        """

        # set player's game.
        self.__game = game
        # set our player's name.
        self.__name = name
        # init our score.
        self.__score = 0
        pass

    def setup(self) -> None:
        """Setup the player's score.
        """
        # game's default font.
        font = pygame.font.Font('freesansbold.ttf', 32)
        text = font.render(str(self.__score), True, (255, 255, 255), None)
        # register the game element.
        self.__game.get_window().register_element(
            "player_" + self.__name + "_score", Element(text, 512, 10))

    def get_name(self) -> str:
        """Get the player's name.

        Returns:
            str: the player's name.
        """
        return self.__name

    def get_score(self) -> int:
        """Get the player's score.

        Returns:
            int: the player's score.
        """

    def set_score(self, score: int) -> None:
        """Set the player's score.

        Args:
            score (int): the player's score.
        """
        self.__score = score
