from threading import (Thread, Event)

class StoppableThread(Thread):
    """Thread class with a stop() method. The thread itself has to check
    regularly for the stopped() condition."""

    def __init__(self, *args, **kwargs):
        super(StoppableThread, self).__init__(*args, **kwargs)
        self._stop_event = Event()
        self.__return_value = None

    def stop(self):
        """
        Mark the thread as stopping.
        """
        self._stop_event.set()

    def set_return_value(self, return_value) -> None:
        """
        For in thread use only.
        :param: object return_value: the value to return at the end of the thread execution.
        """
        self.__return_value = return_value
    
    def get_return_value(self) -> object:
        """
        :return: the value returned by the thread.
        """
        return self.__return_value

    def stopped(self) -> bool:
        """
        For in thread use only.
        :return: whether the thread is marked as stopped or not.
        """
        return self._stop_event.is_set()