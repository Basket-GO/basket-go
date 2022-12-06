import pygame
import random
from game import Game

# init pygame.
pygame.init()
# load game icon.
icon = pygame.image.load("img/Logo.png")
# set game icon.
pygame.display.set_icon(icon)
# set game name.
pygame.display.set_caption("ʙᴀsᴋᴇᴛ ɢᴏ !")
# define window's size.
screen = pygame.display.set_mode((1024,640))
image = ["flame","mountains","pink","basket-ball","smile","military"]
i = random.randint(0,5)
# create a new instance of the Game.
game = Game(screen, "img/",image[i], None)
# register dummy player.
game.register_player("Yanis")
# setup the game.
game.setup()