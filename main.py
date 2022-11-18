from turtle import heading, width
import pygame
from game import Game
from drag_event_listener import DragEventListener

pygame.init()
pygame.display.set_caption("Basket Go !")
screen = pygame.display.set_mode((1024,640))
game = Game(screen, None, "img/", None)
game.listen(pygame.MOUSEMOTION, DragEventListener())
game.setup()

"""size = width, height = 320, 240
speed = [2, 2]
black = 0, 0, 0

screen = pygame.display.set_mode(size)

ball = pygame.image.load("terrain_basket_-_sans_public.png")
ballrect = ball.get_rect()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
        print(event.type)"""