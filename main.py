import pygame

from game import Game
from drag_event_listener import DragEventListener
from ball_release_event_listener import BallReleaseEventListener

# init pygame.
pygame.init()
# load game icon.
icon = pygame.image.load("img/basket-ball.png")
# set game icon.
pygame.display.set_icon(icon)
# set game name.
pygame.display.set_caption("ʙᴀsᴋᴇᴛ ɢᴏ !")
# define window's size.
screen = pygame.display.set_mode((1024,640))
# create a new instance of the Game.
game = Game(screen, "img/", None)
# listen to events.
game.listen(pygame.MOUSEMOTION, DragEventListener())
game.listen(pygame.MOUSEBUTTONUP, BallReleaseEventListener())
# register dummy player.
game.register_player("Yanis")
# setup the game.
game.setup()