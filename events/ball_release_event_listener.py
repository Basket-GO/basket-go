from math import (atan, cos, sin, pi, copysign, tan, sqrt)
from events.event_listener import EventListener
from utils.stoppable_thread import StoppableThread
from utils.vector import Vector
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
        # retrieve the first part of the basket.
        basket_parts = (game.get_window().get_element("basket_part_1"), game.get_window().get_element("basket_part_2"))
        # retrieve basket width.
        basket_w = basket_parts[0].get_surface().get_size()[0]
        # retrieve baskets coordinates.
        bx, by = (((basket_w / 2 - 2) + basket_parts[0].get_x(), (basket_w / 2 - 2) + basket_parts[1].get_x()), ((basket_w / 2 - 2) + basket_parts[0].get_y(), (basket_w / 2 - 2) + basket_parts[1].get_y()))
        # retrieve the ball.
        ball = game.get_window().get_element("ball")
        # define a delta time.
        delta_time = 0.01
        # get the width and the height of the window.
        w, h = pygame.display.get_surface().get_size()
        # get the with and the height of the ball.
        bw = ball.get_surface().get_size()[0]
        # define the x and y values.
        x, y = ball.get_x(), ball.get_y()
        # define gravitation.
        g = 9.81
        vx, vy = 0.1 * (ball.get_initial_x() - ball.get_x()
                        ), 0.1 * (ball.get_initial_y() - ball.get_y())
        # define our vector
        v = Vector(vx, vy)
        # define our reference time.
        tr = time()
        # update x and y position.
        while True:
            if self.__t.paused():
                pass
            if self.__t.stopped():
                break
            ts = time() - tr
            if ts >= delta_time:
                v.set_y(v.get_y() + g * delta_time)
                # update the ball's current coordinates.
                x += v.get_x() * delta_time * 60
                y = v.get_y() * delta_time * 60 + y if (v.get_y() * delta_time * 60) + y < h - bw else h - bw
                # display the ball.
                ball.set_x(x)
                ball.set_y(y)
                # represents respectively the x and y center of the ball.
                cx, cy = ((bw / 2 - 2) + ball.get_x(), (bw / 2 - 2) + ball.get_y())
                # calculate the euclidian distance between the basket and the ball
                basket_distance = (sqrt(((cx - bx[0]) ** 2) + ((cy - by[0]) ** 2)), sqrt(((cx - bx[1]) ** 2) + ((cy - by[1]) ** 2)))
                # pre-calculate alpha.
                if v.get_x() == 0:
                        alpha = copysign(pi / 2, v.get_y())
                elif v.get_x() > 0:
                        alpha = atan(v.get_y() / v.get_x())
                elif v.get_x() < 0:
                        alpha = pi + atan(v.get_y() / v.get_x())
                if basket_distance[0] <= 35:
                    ox = cx + 2 * ((bx[0] - cx) / basket_distance[0])
                    oy = cy + 2 * ((by[0] - cy) / basket_distance[0])
                    print(ox - cx)
                    if ox - cx == 0:
                        omega = pi / 2 if ox > cx else -(pi / 2)
                    elif ox - cx < 0:
                        omega = pi + atan((oy - cy) / (ox - cx))
                    elif ox - cx > 0:
                        omega = atan((oy - cy) / (ox - cx))
                    alpha = pi + 2 * omega - alpha
                    # update vector.
                    v.set_x(v.normalize() * cos(alpha) * 0.6)
                    v.set_y(v.normalize() * sin(alpha) * 0.6)
                elif basket_distance[1] <= 35:
                    if bx[0] - cx <= 0:
                        # calculate omega.
                        omega = pi / 2 if cx < bx[0] else -(pi / 2) 
                    else:
                        # calculate omega.
                        omega = atan((by[1] - y) / (bx[1] - x))
                    alpha = pi + 2 * omega - alpha
                    # update vector.
                    v.set_x(v.normalize() * cos(alpha) * 0.6)
                    v.set_y(v.normalize() * sin(alpha) * 0.6)
                if y + bw >= h:
                    # re-calculate alpha.
                    alpha = -alpha
                    # update vector.
                    v.set_x(v.normalize() * cos(alpha) * 0.6)
                    v.set_y(v.normalize() * sin(alpha) * 0.6)
                # check if the ball is out of the screen.
                if x - bw >= w or x + bw <= 0 or (y >= 570 and v.get_y() > -0.05):
                    # reset ball's coordinates.
                    ball.respawn()
                    break
                tr += delta_time