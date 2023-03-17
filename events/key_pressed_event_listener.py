from events.event_listener import EventListener

class KeyPressedEventListener(EventListener):
    def __init__(self, key_pressed:int) -> None:
        super().__init__()
        self.__key_pressed = key_pressed

    def run(self, event, game):
        if self.__key_pressed == event.key:
            self.onKeyPressed(game)
    
    def onKeyPressed(self, game):
        pass