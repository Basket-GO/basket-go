from event_listener import EventListener
from game import Game
import pygame

class DragEventListener(EventListener):
    def __init__(self) -> None:
        super().__init__()
        self.__white_dot = pygame.image.load("img/white_dot.png")
        self.__white_dot = pygame.transform.scale(self.__white_dot, (20, 20))
    
    def run(self, event, game:Game):
        if pygame.mouse.get_pressed()[0] == True:
            # retrieve the ball.
            ball = game.get_window().get_element("ball")
            # update x and y position.
            ball.set_x(pygame.mouse.get_pos()[0] - 30)
            ball.set_y(pygame.mouse.get_pos()[1] - 30)
            # get the initial x and y value.
            ix, iy = ball.get_initial_x(), ball.get_initial_y()
            for t in range(0, 150):
                t = t
                # get the inital vector values.
                vx, vy = ix - ball.get_x(), iy - ball.get_y()
                x = ball.get_x() + 30 + vx * t
                y = -(1/2) * -9.81 * t**2 + vy * t + ball.get_y() + 30
                game.get_screen().blit(self.__white_dot, (x, y))