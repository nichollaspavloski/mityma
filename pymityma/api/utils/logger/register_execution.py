from ..pubsub import Publisher, Subscriber
from typing import List


"""
    Concrete Publisher registers/unregisters subscribers and notifies them
"""


class RegisterExecution(Publisher):
    def __init__(self):
        self.subscribers: List[Subscriber] = []

    def register_sub(self, subscriber: Subscriber):
        self.subscribers.append(subscriber)

    def remove_sub(self, subscriber: Subscriber):
        self.subscribers.remove(subscriber)

    def _notify_sub(self, event: str, data: dict):
        for subscriber in self.subscribers:
            subscriber.update(event, data)

    # methods to register logs into database
    def create_log_record(self, data: dict):
        # notify subscribers
        self._notify_sub(data['label'], data)
