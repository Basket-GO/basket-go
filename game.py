import pygame
import sys

from event_listener import EventListener
from player import Player
from element import Element

class Game():
    def __init__(self, screen:pygame.Surface, img_location:str, sound_location:str) -> None:
        # get the actual display screen.
        self.__screen = screen
        # set up playing players.
        self.__players = []
        # set up the events pair.
        self.__events = []
        # game elements (objects, background etc.)
        self.__elements = []
        # game threads.
        self.__threads = []
        # get the actual basket ball field.
        field = pygame.image.load(img_location + "terrain_basket_sans_public2.png")
        field = pygame.transform.scale(field, (1024, 640))

        # get the actual ball.
        ball = pygame.image.load(img_location + "basket-ball.png")
        ball = pygame.transform.scale(ball, (70, 70))
        # get the placeholder ball.
        placeholder_ball = pygame.image.load(img_location + "basket-ball-placeholder.png")
        placeholder_ball = pygame.transform.scale(placeholder_ball, (70, 70))
        # register the field without public.
        self.register_element("field", Element(field, 0, 0))

        # register the ball.
        self.register_element("ball", Element(ball, 170, 450))
        # register the placeholder ball.
        self.register_element("placeholder_ball", Element(placeholder_ball, 170, 450))
    def register_player(self, player_name:str) -> None:
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
    def register_element(self, key:str, element):
        """
        Register a game element into the cache.
        :param str key: the key to pair to the given element.
        :param object element: the element to store.
        """
        self.__elements.append([key, element])

    def get_element(self, key:str):
        """
        If present returns the element paired with the given key
        else it raises RuntimeError.
        :param str key: the key paired to the game element.
        :return: the game element.
        """
        for element in self.__elements:
            if element[0] == key:
                return element[1]
        raise RuntimeError("element not found for key: ", key)

    def setup(self):
        """
        Setup the ressources (background image, audio, etc.)
        and listen to all the events built in the game.
        """
        while True:
            # loop through each elements.
            for element in self.__elements:
                # retrive the object.
                obj = element[1]
                if(obj.is_visible()):
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
            pygame.display.update()
    def listen(self, event_type:int, event_listener:EventListener) -> None:
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
    
