from abc import ABC, abstractmethod
from .transaction import Transaction

"""
    Implementations for the Command class 
"""


# interface
class Command(ABC):

    @abstractmethod
    def execute(self):
        print('not implemented yet')
        pass


# concrete implementations
class UpsertCommand(Command):
    def __init__(self, session, model) -> None:
        self.session = session
        self.model = model

    def execute(self) -> None:
        self.session.add(self.model)


class DeleteCommand(Command):
    def __init__(self, session, model, id) -> None:
        self.session = session
        self.model = model
        self.id = id

    def execute(self) -> None:
        record = self.model.query.filter_by(id=self.id).first()
        self.session.delete(record)


class CommitCommand(Command):
    def __init__(self, session, transaction: Transaction) -> None:
        self.session = session
        self.transaction = transaction

    def execute(self) -> None:
        self.transaction.execute_all()
        self.session.commit()


class RollbackCommand(Command):
    def __init__(self, session) -> None:
        self.session = session

    def execute(self) -> None:
        self.session.rollback()

