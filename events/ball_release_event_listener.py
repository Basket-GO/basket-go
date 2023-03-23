from math import (atan, cos, sin, pi, copysign, tan, sqrt)
from events.event_listener import EventListener
from utils.stoppable_thread import StoppableThread
from utils.vector import Vector
from time import time
from components.basket import Basket
from copy import copy
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
        game.register_thread("b_thread", self.__t)
        # start the thread execution.
        self.__t.start()
    def __arctan(self, x, y):
        """
        :return: the arctan of an angle based on the x and y position of this element.
        :param float x: an x coordinate.
        :param float y: an y coordinate.
        """
        if y == 0:  # Sur l'axe des ordonnées
            if x >= 0:
                return 0
            else:
                return pi
        elif x > 0:  # Premier et quatrième quadrants
            return -atan(y/x)
        else:
            if y > 0:  # Troisième quadrant
                return atan(x/y) - pi/2
            else:  # Second quadrant
                return atan(x/y) + pi/2
    def __move_ball(self, game):
        """
        Makes the ball move.
        """
        # retrieve the first part of the basket.
        basket = game.get_window().get_element("basket")
        # retrieve baskets coordinates.
        bx, by = ((basket.hoops()[0].center_x(), basket.hoops()[1].center_x()), (basket.hoops()[0].center_y(), basket.hoops()[1].center_y()))
        # retrieve the ball.
        ball = game.get_window().get_element("ball")
        # init x' & y'
        x_prime, y_prime = ball.center_x(), ball.center_y()
        # define a delta time.
        delta_time = 0.01
        # define the absorption
        absorption = 0.8
        # get the width and the height of the window.
        h = pygame.display.get_surface().get_size()[1]
        # get the with and the height of the ball.
        bw = ball.get_surface().get_size()[0]
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
                # update the y coordinate of the ball's speed vector.
                v.set_y(v.get_y() + g * delta_time)
                # pre-calculate alpha.
                if v.get_x() == 0:
                    alpha = copysign(pi / 2, v.get_y())
                elif v.get_x() > 0:
                    alpha = self.__arctan(v.get_x(), v.get_y())
                elif v.get_x() < 0:
                    alpha = self.__arctan(v.get_x(), v.get_y())
                # calculate the future x coordinate of the ball.
                x_prime += v.get_x() * delta_time * 60
                # calculate the future y coordinate of the ball.
                y_prime = v.get_y() * delta_time * 60 + y_prime if (v.get_y() * delta_time * 60) + y_prime < h - bw // 2 else h - bw // 2
                if y_prime + bw // 2 < h:
                    ball.set_grnd_rebounced(False)
                # check if the ball touches the ground.
                if y_prime + bw // 2 >= h and not ball.has_grnd_rebounced():
                    ball.set_grnd_rebounced(True)
                    alpha = ball.rebounce(x_prime, h, alpha)
                    # update vector.
                    v.set_x(v.normalize() * cos(alpha) * absorption)
                    v.set_y(-v.normalize() * sin(alpha) * absorption)
                    # calculate the future x coordinate of the ball.
                    x_prime += v.get_x() * delta_time * 60
                    # calculate the future y coordinate of the ball.
                    y_prime = v.get_y() * delta_time * 60 + y_prime if (v.get_y() * delta_time * 60) + y_prime < h - bw // 2 else h - bw //2
                else:
                    # calculate the euclidian distance between the basket and the center of the ball.
                    b_d1 = ball.distance(bx[0], by[0])
                    b_d2 = ball.distance(bx[1], by[1])
                    # calculate the radius between the first basket and the ball.
                    r1 = b_d1 / (bw / 2)
                    r2 = b_d2 / (bw / 2)
                    # check if we touch the hood.
                    if b_d1 >= bw // 2:
                        ball.set_rebounced(False)
                    if b_d1 <= bw // 2 and not ball.has_rebounced():
                         # calcuate the point of impact on the ball radius with the basket.
                        ox = ball.center_x() + (bx[0] - ball.center_x()) * r1
                        oy = ball.center_y() + (by[0] - ball.center_y()) * r1
                        # copy the actual vector.
                        v_second = copy(v)
                        # calculate the alpha rebounce.
                        alpha_second = ball.rebounce(ox, oy, alpha)
                        # update the vector.
                        v_second.set_x(v_second.normalize() * cos(alpha_second) * absorption)
                        v_second.set_y(-v_second.normalize() * sin(alpha_second) * absorption)
                        # calculate the future x coordinate of the ball.
                        x_second = v_second.get_x() * delta_time * 60 + x_prime
                        # calculate the future y coordinate of the ball.
                        y_second = v_second.get_y() * delta_time * 60 + y_prime
                        # re-calculate the distance.
                        b_d1_prime = ball.distance_two_points(x_second, y_second, bx[0], by[0])
                        # check the next distance isn't within the bounds of the hood.
                        if b_d1_prime > b_d1:
                            v = v_second
                            alpha = alpha_second
                            x_prime, y_prime = x_second, y_second
                            ball.set_rebounced(True)
                ball.set_x(x_prime - bw // 2)
                ball.set_y(y_prime - bw // 2)
                """v.set_y(v.get_y() + g * delta_time)
                # update the ball's current coordinates.
                x += v.get_x() * delta_time * 60
                y = v.get_y() * delta_time * 60 + y if (v.get_y() * delta_time * 60) + y < h - bw else h - bw
                # display the ball.
                ball.set_x(x)
                ball.set_y(y)
                # represents respectively the x and y center of the ball.
                cx, cy = ((bw / 2) + ball.get_x(), (bw / 2) + ball.get_y())
                # calculate the euclidian distance between the basket and the ball
                basket_distance = (sqrt(((cx - bx[0]) ** 2) + ((cy - by[0]) ** 2)), sqrt(((cx - bx[1]) ** 2) + ((cy - by[1]) ** 2)))
                # pre-calculate alpha.
                if v.get_x() == 0:
                    alpha = copysign(pi / 2, v.get_y())
                elif v.get_x() > 0:
                    alpha = self.__arctangente(v.get_x(), v.get_y())
                elif v.get_x() < 0:
                    alpha = pi + self.__arctangente(v.get_x(), v.get_y())
                if basket_distance[0] <= 35:
                    r = basket_distance[0] / 35
                    ox = cx + (bx[0] - cx) * r
                    oy = cy + (by[0] - cy) * r
                    alpha = self.__rebounce(cx, cy, ox, oy, alpha)
                    # update vector.
                    v.set_x(v.normalize() * cos(alpha) * 0.6)
                    v.set_y(-v.normalize() * sin(alpha) * 0.6)
                    # calculate the euclidian distance between the basket and the ball
                    basket_distance = (sqrt(((cx - bx[0]) ** 2) + ((cy - by[0]) ** 2)), sqrt(((cx - bx[1]) ** 2) + ((cy - by[1]) ** 2)))
                    # update the ball's current coordinates.
                    while basket_distance[0] <= 35:
                        x += v.get_x() * delta_time * 60
                        y = v.get_y() * delta_time * 60 + y if (v.get_y() * delta_time * 60) + y < h - bw else h - bw
                        ball.set_x(x)
                        ball.set_y(y)
                        # represents respectively the x and y center of the ball.
                        cx, cy = ((bw / 2) + ball.get_x(), (bw / 2) + ball.get_y())
                        # calculate the euclidian distance between the basket and the ball
                        basket_distance = (sqrt(((cx - bx[0]) ** 2) + ((cy - by[0]) ** 2)), sqrt(((cx - bx[1]) ** 2) + ((cy - by[1]) ** 2)))
                if y + bw >= h:
                    # re-calculate alpha.
                    alpha = self.__rebounce(cx, cy, cx, h, alpha)
                    # update vector.
                    v.set_x(v.normalize() * cos(alpha) * 0.6)
                    v.set_y(-v.normalize() * sin(alpha) * 0.6)
                # check if the ball is out of the screen.
                if x - bw >= w or x + bw <= 0 or (y >= 570 and v.get_y() < -.03 and v.get_y() > -.05):
                    # reset ball's coordinates.
                    ball.respawn()
                    break"""
                tr += delta_time