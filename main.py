from turtle import heading, width
import sys, pygame
from game import Game

pygame.init()
pygame.display.set_caption("Basket Go !")
screen = pygame.display.set_mode((1024,640))
game = Game(screen, None, "img/", None)
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