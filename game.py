import pygame
import sys

from components.player import Player
from element import Element
from interface.window import Window
from components.ball import Ball

from events.event_listener import EventListener
from events.drag_event_listener import DragEventListener
from events.ball_release_event_listener import BallReleaseEventListener


class Game():
    def __init__(self, screen: pygame.Surface, img_location: str, img_name: str, sound_location: str) -> None:
        # get the actual display screen.
        self.__screen = screen
        # set up playing players.
        self.__players = []
        # set up the events pair.
        self.__events = []
        # set up our window.
        self.__window = Window()
        # game threads.
        self.__threads = []
        self.clock = pygame.time.Clock()
        self.fps = 150
        # get the actual basket ball field.
        field = pygame.image.load(img_location + "terrain_basket_public.png")
        field = pygame.transform.scale(field, (1024, 640))
        field2 = pygame.image.load(
            img_location + "terrain_basket_public_2.png")
        field2 = pygame.transform.scale(field2, (1024, 640))
        self.field = field
        self.field2 = field2
        # get the cursor
        cursor_init = pygame.image.load("img/cursor.png").convert_alpha()
        self.cursor = cursor_init
        # get the actual ball.
        ball = pygame.image.load(img_location + img_name+".png")
        # get the placeholder ball.
        placeholder_ball = pygame.image.load(
            img_location + img_name+"-placeholder.png")
        # register the field without public.
        self.get_window().register_element("field", Element(field2, 0, 0))
        # register the ball.
        self.get_window().register_element("ball", Ball(ball, 170, 450))
        # register the placeholder ball.
        self.get_window().register_element("placeholder_ball",
                                           Element(placeholder_ball, 170, 450))
        # listen to events.
        self.listen(pygame.MOUSEMOTION, DragEventListener(self))
        self.listen(pygame.MOUSEBUTTONUP, BallReleaseEventListener())

    def get_window(self) -> Window:
        """
        :return: the game's window.
        """
        return self.__window

    def register_player(self, player_name: str) -> None:
        """
        Register a player by its name.
        :param: str player_name: the player's name.
        """
        # create the player.
        player = Player(self, player_name)
        # setup the player.
        player.setup()
        # register the player.
        self.__players.append(player)

    def register_thread(self, thread) -> None:
        """
        Register the given thread into a list.
        """
        self.__threads.append(thread)

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
                    # stop ongoin threads.
                    for thread in self.__threads:
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
