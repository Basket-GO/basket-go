import pygame
import sys

from components.hoop import Hoop
from components.player import Player
from element import Element
from interface.window import Window
from components.ball import Ball
from components.basket import Basket

from random import randint
from events.event_listener import EventListener
from events.drag_event_listener import DragEventListener
from events.ball_release_event_listener import BallReleaseEventListener
from events.ball_respawn_event_listener import BallRespawnEventListener


class Game():
    def __init__(self, screen: pygame.Surface, img_location: str, img_name: str, img_terrain: str, sound_location: str, available_colors: list) -> None:
        self.__players_index = 0
        # init players index. (used for turn by turn games)
        self.__available_colors = available_colors
        # init available colors for the players.
        # get the actual display screen.
        self.__screen = screen
        # set up playing players.
        self.__players = {}
        # set up the events pair.
        self.__events = []
        # set up our window.
        self.__window = Window()
        # game threads.
        self.__threads = {}
        self.clock = pygame.time.Clock()
        self.fps = 150
        # get the actual basket ball field.
        field = pygame.image.load(
            img_location + "basket-ball/" + img_terrain+".jpg")
        spec = pygame.image.load(img_location + "basket-ball/" + "spec.png")
        panier = pygame.image.load(
            img_location + "basket-ball/" + "panier.png")
        self.field = field
        # get the cursor
        cursor_init = pygame.image.load("img/cursor.png").convert_alpha()
        self.cursor = cursor_init
        # get the actual ball.
        ball = pygame.image.load(
            img_location + "basket-ball/" + img_name+".png")
        # get the placeholder ball.
        placeholder_ball = pygame.image.load(
            img_location + "basket-ball/" + img_name+"-placeholder.png")
        # register the field without public.
        self.get_window().register_element("field", Element(field, 0, 0))
        # self.get_window().register_element("spec", Element(spec, 0, 0))
        # register the ball.
        self.get_window().register_element("ball", Ball(ball, 170, 450))
        # register the placeholder ball.
        self.get_window().register_element("placeholder_ball",
                                           Element(placeholder_ball, 170, 450, False))
        collider = pygame.image.load("img/basket-ball/white_dot.png")
        collider = pygame.transform.scale(collider, (20, 20))
        basket = pygame.image.load("img/basket.png")
        # register basket elements.
        self.get_window().register_element("basket",  Basket(
            Element(basket, 300, 300), Hoop(collider, 300, 320), Hoop(collider, 400, 320)))
        # listen to events.
        self.listen(pygame.MOUSEMOTION, DragEventListener(self))
        self.listen(pygame.MOUSEBUTTONUP, BallReleaseEventListener())
        self.listen(pygame.KEYDOWN, BallRespawnEventListener(pygame.K_r))

    def get_window(self) -> Window:
        """
        :return: the game's window.
        """
        return self.__window

    def register_player(self, player_name: str, score: int) -> None:
        """
        Register a player by its name.
        :param: str player_name: the player's name.
        """
        # retrieve player's color based on its index.
        color = self.__available_colors[len(self.__players)]
        # create the player.
        player = Player(self, player_name, color, score)
        # register the player.
        self.__players[player_name, score] = player
        print("Player {} registered.".format(player_name))
        print("Player point : {}".format(player.get_score()))

    def get_player(self, player_name: str) -> Player:
        """
        Retrieve a player by its name.
        :param: str player_name: the player's name.
        """
        return self.__players[player_name]

    def get_playing_player(self) -> Player:
        """
        Retrieve and returns the current playing player.
        """
        return list(self.__players.values())[self.__players_index]

    def register_thread(self, name: str, thread) -> None:
        """
        Register the given thread into a list.
        """
        self.__threads[name] = thread

    def get_thread(self, name: str):
        """
        Get a thread by its name.
        Can be None.
        """
        return self.__threads[name]

    def has_thread(self, name: str):
        return name in self.__threads

    def display_fps(self):
        """Show the program's FPS in the window handle."""
        caption = "{} - FPS: {:.2f}".format("ʙᴀsᴋᴇᴛ ɢᴏ !",
                                            self.clock.get_fps())
        pygame.display.set_caption(caption)

    def setup(self):
        """
        Setup the ressources (background image, audio, etc.)
        and listen to all the events built in the game.
        """
        # check if the game as enough players to start.
        if len(self.__players) == 0:
            raise RuntimeError(
                "The game requires at least one player to start...")
        # loop through each player.
        for i in range(len(self.__players)):
            # retrieve the player.
            player = list(self.__players.values())[i]
            # render text.
            text = pygame.font.Font('freesansbold.ttf', 32).render(
                str(player.get_score()), True, player.get_color(), None)
            # set the x position of the text.
            x = (self.__screen.get_width() - text.get_width() * len(self.__players) -
                 80 * (len(self.__players) - 1)) / 2 + 80 * (i) + text.get_width() / 2
            # register the game element.
            self.get_window().register_element("player_" + player.get_name() +
                                               "_score", Element(text, x, 10, True, True))
        # update basket's position
        self.__update_basket_pos()
        while True:
            x, y = pygame.mouse.get_pos()
            x -= self.cursor.get_width()/2-5
            y -= self.cursor.get_height()/2-8
            self.clock.tick(self.fps)
            self.display_fps()
            # loop through each elements.
            for element in self.__window.get_elements():
                # retrive the object.
                obj = element[1]
                if obj != None and obj.is_visible():
                    self.__screen.blit(obj.get()[0], obj.get()[1])
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    # stop ongoing threads.
                    for thread in self.__threads.values():
                        thread.stop()
                    # exit.
                    sys.exit()
                # loop through each listeners.
                for event_pair in self.__events:
                    # compare the triggered event with the target event.
                    if event_pair[0] == event.type:
                        # run the event.
                        event_pair[1].run(event, self)
            # cursor init
            self.__screen.blit(self.cursor, (x, y))
            pygame.display.update()

    def listen(self, event_type: int, event_listener: EventListener) -> None:
        """
        Takes in parameter an event to call and an event type to listen to.
        Bind in pair the event type and the event to call.
        :param int event_type: the event type to listen to.
        :param EventListener event_listener: the event listener that will be called.
        """
        self.__events.append([event_type, event_listener])

    def end(self):
        pass

    def get_screen(self):
        """
        Return game's screen.
        """
        return self.__screen

    def next_turn(self):
        # retrieve the ball.
        ball = self.get_window().get_element("ball")
        # make the ball respawn.
        ball.respawn()
        # retrieve the basket.
        basket = self.get_window().get_element("basket")
        # reset ball rebounces on the hood.
        basket.set_rebounces(0)
        # update basket's position
        self.__update_basket_pos()
        # make the next player play.
        self.__players_index = 0 if self.__players_index + \
            1 >= len(self.__players) else self.__players_index + 1

    def __update_basket_pos(self):
        # retrieve the ball.
        ball = self.get_window().get_element("ball")
        # retrieve the basket.
        basket = self.get_window().get_element("basket")
        # calculate the x & y coordinates.
        x, y = randint(ball.get_x() + 180 + ball.get_surface().get_width(),
                       self.__screen.get_width() - basket.get_surface().get_width()), randint(200, 430)
        # move the basket.
        basket.move(x, y)
