from abc import ABC, abstractmethod


class Command(ABC):

    @abstractmethod
    def execute(self):
        print('not implemented yet')
        pass
