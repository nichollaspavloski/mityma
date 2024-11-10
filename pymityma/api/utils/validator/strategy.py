from abc import ABC, abstractmethod
from datetime import datetime

'''
    Strategy behavioral design pattern
    to validate input data from client
'''

class InputValidation(ABC):
    @abstractmethod
    def validate(self, data):
        pass

class AgeValidation(InputValidation):
    def validate(self, age):
        if 14 < age < 90:
            return True
        return False

class DateValidation(InputValidation):
    def validate(self, date):
        formats = ["%d-%m-%Y", "%d-%m-%Y %H:%M", "%d-%m-%Y %H:%M:%S"]
        for f in formats:
            try:
                datetime.strptime(date, f)
                return True
            except ValueError:
                continue
        return False


class ValidationContext:
    def __init__(self, strategy: InputValidation):
        self._strategy = strategy

    def set_strategy(self, strategy: InputValidation):
        self._strategy = strategy

    def validate(self, data):
        return self._strategy.validate(data)