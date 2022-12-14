from events.event_listener import EventListener
from element import Element
import pygame


class DragEventListener(EventListener):
    def __init__(self, game) -> None:
        super().__init__()
        self.__white_dot = pygame.image.load("img/basket-ball/white_dot.png")
        # pre-register the dots.
        for i in range(20):
            game.get_window().register_element(("dot_",str(i)), Element(self.__white_dot, 0, 0, False, False))
    
    def run(self, event, game):
        # retrieve the ball.
        ball = game.get_window().get_element("ball")
        # get the with and the height of the ball.
        bw, bh = ball.get_surface().get_size()
         # get the width and the height of the window.
        h = pygame.display.get_surface().get_size()[1]
        # retrieve mouse position.
        mouse_x, mouse_y = pygame.mouse.get_pos()
        # check if the ball is out of limits on the x axis.
        if pygame.mouse.get_pos()[0] - (bw / 2) < 0:
            # still update the y axis.
            mouse_x = bw / 2
        # check if the ball is out of limits on the y axis.
        if pygame.mouse.get_pos()[1] + (bh / 2) > h:
            # still update the x axis.
            mouse_y = h - bh / 2
        if pygame.mouse.get_pressed()[0] == True and not ball.is_released():
            # update x and y position.
            ball.set_x(mouse_x - 30)
            ball.set_y(mouse_y - 30)
            # get the initial x and y value.
            ix, iy = ball.get_initial_x(), ball.get_initial_y()
            vx, vy = 1.1 * (ix - ball.get_x()), 1.1 * (iy - ball.get_y())
            for t in range(20):
                # get the inital vector values.
                x = (ball.get_x() + 30 + vx * t)
                y = (9.81 * t**2 + vy * t + ball.get_y() + 30)
                if t != 0:
                    # retrieve the dot.
                    dot = game.get_window().get_element(("dot_", str(t)))
                    # update x and y coordinates.
                    dot.set_x(x)
                    dot.set_y(y)
                    # set the dot visible.
                    dot.set_visible(True)