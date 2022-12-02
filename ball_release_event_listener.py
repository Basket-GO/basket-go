from event_listener import EventListener
from game import Game
from stoppable_thread import StoppableThread
from vector import Vector
from math import (ceil, atan, pi, cos, sin)
from time import wait
import pygame

class BallReleaseEventListener(EventListener):
    def __init__(self) -> None:
        super().__init__()
    
    def run(self, event, game:Game):
        # retrieve the ball.
        ball = game.get_element("ball")
        # retrieve the placeholder ball.
        placeholder_ball = game.get_element("placeholder_ball")
        # check if the ball is at the same position
        if abs(ball.get_x() - ball.get_initial_x()) < 15 and abs(ball.get_y() - ball.get_initial_y()) < 15:
            return
        # disable ball.
        placeholder_ball.set_visible(False)
        # launch new thread.
        self.__t = StoppableThread(target=self.__move_ball, args=(game,))
        # register the thread in order to be able to kill it.
        game.register_thread(self.__t)
        # start the thread execution.
        self.__t.start()
    def __move_ball(self, game:Game):
        """
        Makes the ball move.
        """
        # retrieve the ball.
        ball = game.get_element("ball")
        # define a delta time.
        delta_time = 0.1
        # get the width and the height of the window.
        w, h = pygame.display.get_surface().get_size()
        # get the with and the height of the ball.
        bw, bh = ball.get_surface().get_size()
        # define the x and y values.
        x, y = ball.get_x(), ball.get_y()
        # define gravitation.
        g = 9.81
        vx, vy = 0.8 * (ball.get_initial_x() - ball.get_x()), 0.8 * (ball.get_initial_y() - ball.get_y())
        # define our vector
        v = Vector(vx, vy)
        # update x and y position.
        while True:
            if self.__t.stopped():
                break
            v.set_y(v.get_y() + g * delta_time)
            x += v.get_x() * delta_time
            y += v.get_y() * delta_time
            ball.set_x(x)
            ball.set_y(y)
            if y + bh >= h:
                # calculate alpha.
                alpha = atan(v.get_y() / v.get_x())
                # re-calculate alpha.
                alpha = -alpha
                # update vector.
                v.set_x(v.normalize() * cos(alpha) * 0.8)
                v.set_y(v.normalize() * sin(alpha) * 0.8)
            #print(y)
            time.wait(ceil(delta_time / 1000))