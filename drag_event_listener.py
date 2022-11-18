from event_listener import EventListener
from game import Game
import pygame

class DragEventListener(EventListener):
    def __init__(self) -> None:
        super().__init__()
    
    def run(self, event, game:Game):
        if pygame.mouse.get_pressed()[0] == True:
            # retrieve the ball.
            ball = game.get_element("ball")
            # update x and y position.
            ball.set_x(pygame.mouse.get_pos()[0] - 30)
            ball.set_y(pygame.mouse.get_pos()[1] - 30)