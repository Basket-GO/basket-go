from math import (atan, cos, sin, pi, copysign, tan, sqrt, floor)
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
        if abs(ball.get_x() - ball.get_initial_x(False)) < 60 and abs(ball.get_y() - ball.get_initial_y(False)) < 60 or ball.is_released():
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
        w, h = pygame.display.get_surface().get_size()[0], pygame.display.get_surface().get_size()[1]
        # get the with and the height of the ball.
        bw = ball.get_surface().get_size()[0]
        # define gravitation.
        g = 9.81
        vx, vy = 0.1 * (ball.get_initial_x(False) - ball.get_x()
                        ), 0.1 * (ball.get_initial_y(False) - ball.get_y())
        
        # define our vector
        v = Vector(vx, vy)
        # define our reference time.
        tr = time()
        # update x and y position.
        while True:
            if self.__t.paused():
                pass
            if self.__t.stopped():
                ball.respawn()
                break
            ts = time() - tr
            if ts >= delta_time:
                # update the y coordinate of the ball's speed vector.
                v.set_y(v.get_y() + g * delta_time)
                # make the ball rotate
                #ball.rotate(v.get_x())
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
                    b_d = ball.distance(bx[0], by[0], True), ball.distance(bx[1], by[1], True)
                    # loop through each hoop point.
                    for i in range(len(b_d)):
                        # retrieve hoop.
                        hoop = basket.hoops()[i]
                        # retrieve the distance between the hoop and the ball.
                        distance = b_d[i]
                        # calculate the radius between the first basket and the ball.
                        r = distance / (bw / 2)
                        # check if we touch the hood.
                        if distance >= bw // 2 and hoop.has_been_touched():
                            ball.set_rebounced(False)
                            hoop.set_touched(False)
                        if distance <= bw // 2 and not ball.has_rebounced():
                            # calcuate the point of impact on the ball radius with the basket.
                            ox = ball.center_x() + (bx[i] - ball.center_x()) * r
                            oy = ball.center_y() + (by[i] - ball.center_y()) * r
                            # copy the actual vector.
                            v_second = copy(v)
                            # calculate the alpha rebounce.
                            alpha_second = ball.rebounce(ox, oy, alpha)
                            # update the vector.
                            v_second.set_x(v_second.normalize() * cos(alpha_second) * absorption)
                            v_second.set_y(-v_second.normalize() * sin(alpha_second) * absorption)
                            # update intial vector.
                            v = v_second
                            # update intial alpha.
                            alpha = alpha_second
                            # states that the ball rebounced.
                            ball.set_rebounced(True)
                            # states that the hoop has been touched.
                            hoop.set_touched(True)
                            # break the check loop.
                            break
                # check if the ball has stopped moving and is on the floor.
                if (abs(ball.get_x() - x_prime) - bw // 2) < 0.001 and (abs(ball.get_y() - y_prime) - bw // 2) <= 0.001 and floor(h - (ball.get_y() + bw)) == 0:
                    ball.respawn()
                    break
                # check if the ball is our of screen.
                if ball.get_x() > w or ball.get_x() + bw < 0:
                    ball.respawn()
                    break
                # update ball's coordinates.
                ball.set_x(x_prime - bw // 2)
                ball.set_y(y_prime - bw // 2)
                tr += delta_time