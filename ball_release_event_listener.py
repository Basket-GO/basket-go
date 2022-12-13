from event_listener import EventListener
from stoppable_thread import StoppableThread
from vector import Vector
from math import (atan, cos, sin, pi, copysign, tan)
from time import time
import pygame

class BallReleaseEventListener(EventListener):
    def __init__(self) -> None:
        super().__init__()
    
    def run(self, event, game):
        # retrieve the ball.
        ball = game.get_window().get_element("ball")
        # check if the ball is already released.
        if ball.is_released():
            return
        # retrieve the placeholder ball.
        placeholder_ball = game.get_window().get_element("placeholder_ball")
        # retrive game's window.
        window = game.get_window()
        # check if the ball is at the same position
        if abs(ball.get_x() - ball.get_initial_x()) < 60 and abs(ball.get_y() - ball.get_initial_y()) < 60 or ball.is_released():
            ball.respawn()
            # clear dots.
            for i in range(20):
                window.get_element(("dot_",str(i))).set_visible(False)
            return
        ball.set_released(True)
        # disable ball.
        placeholder_ball.set_visible(False)
        # clear dots.
        for i in range(20):
            window.get_element(("dot_",str(i))).set_visible(False)
        # launch new thread.
        self.__t = StoppableThread(target=self.__move_ball, args=(game,))
        # register the thread in order to be able to kill it.
        game.register_thread(self.__t)
        # start the thread execution.
        self.__t.start()
    def __move_ball(self, game):
        """
        Makes the ball move.
        """
        # retrieve the ball.
        ball = game.get_window().get_element("ball")
        # define a delta time.
        delta_time = 0.01
        # get the width and the height of the window.
        w, h = pygame.display.get_surface().get_size()
        # get the with and the height of the ball.
        bw, bh = ball.get_surface().get_size()
        # define the x and y values.
        x, y = ball.get_x(), ball.get_y()
        # define gravitation.
        g = 9.81
        vx, vy = 0.1 * (ball.get_initial_x() - ball.get_x()), 0.1 * (ball.get_initial_y() - ball.get_y())
        # define our vector
        v = Vector(vx, vy)
        # define our reference time.
        tr = time()
        # update x and y position.
        while True:
            if self.__t.stopped():
                break
            ts = time() - tr
            if ts >= delta_time:
                v.set_y(v.get_y() + g * delta_time)
                # update the ball's current coordinates.
                x += v.get_x() * delta_time * 60
                y = v.get_y() * delta_time * 60 + y if (v.get_y() * delta_time * 60) + y < h - bh else h - bh
                # display the ball.
                ball.set_x(x)
                ball.set_y(y)
                if y + bh >= h:
                    if v.get_x() == 0:
                        alpha = copysign(pi / 2, v.get_y())
                    elif v.get_x() > 0:
                        alpha = atan(v.get_y() / v.get_x())
                    elif v.get_x() < 0:
                        alpha = pi + atan(v.get_y() / v.get_x())
                    # re-calculate alpha.
                    alpha = -alpha
                    # update vector.
                    v.set_x(v.normalize() * cos(alpha) * 0.8)
                    v.set_y(v.normalize() * sin(alpha) * 0.8)
                # check if the ball is out of the screen.
                if x - bw >= w or x + bw <= 0 or (y >= 570 and v.get_y() > -0.05):
                    # reset ball's coordinates.
                    ball.respawn()
                    break
                tr += delta_time