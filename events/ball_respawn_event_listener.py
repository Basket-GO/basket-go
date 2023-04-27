from events.key_pressed_event_listener import KeyPressedEventListener
from random import randint

class BallRespawnEventListener(KeyPressedEventListener):
    def __init__(self, key_pressed:int) -> None:
        super().__init__(key_pressed)
    
    def onKeyPressed(self, game):
        if not game.has_thread("b_thread"):
            return
        # retrieve the ongoing thread
        thread = game.get_thread("b_thread")
        # check if there's an ongoing thread
        if thread is not None:
            # stop the ball movement
            thread.stop()