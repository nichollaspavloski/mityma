from abc import ABC, abstractmethod

"""
    Interfaces classes for Publisher and Subscriber
    objects for Observer behavioral design pattern
"""


class Subscriber(ABC):
    @abstractmethod
    def update(self, event: str, data: dict):
        pass


class Publisher(ABC):
    @abstractmethod
    def register_sub(self, observer: Subscriber):
        pass

    @abstractmethod
    def remove_sub(self, observer: Subscriber):
        pass

    @abstractmethod
    def _notify_sub(self, event: str, data: dict):
        pass
