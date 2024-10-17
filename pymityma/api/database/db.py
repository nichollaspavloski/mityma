from ..server import db
from sqlalchemy import func
from .commands import *
from .transaction import Transaction

"""
    Database class works as the receiver in Command behavioral 
    design pattern. It handles the execution of concrete commands
"""

_database = None
@staticmethod
def get_db():
    """
        Singleton creational design pattern to get only one instance of Database class
    """
    database = Database() if _database is None else _database
    return database


class Database:
    _session = None

    def __init__(self):
        if self._session is None:
            self._session = db.session()

        self.engine = db.get_engine()
        self.transaction = Transaction()

    def commit(self):
        command = CommitCommand(self._session, self.transaction)
        command.execute()
        self.transaction.clear_statements()

    def rollback(self):
        command = RollbackCommand(self._session)
        command.execute()
        self.transaction.clear_statements()

    def upsert(self, model: db.Model):
        command = UpsertCommand(self._session, model)
        self.transaction.append_statements(command)

    def delete(self, model: db.Model, id):
        command = DeleteCommand(self._session, model, id)
        self.transaction.append_statements(command)

    def query_by_id(self, model: db.Model, id):
        return self._session.query(model).filter_by(id=id).first()

    def next_id(self, model: db.Model) -> int:
        result = self._session.query(func.max(model.id)).scalar()
        next_id = 1 if result is None else result + 1
        return next_id


class DatabaseException(Exception):
    def __init__(self, message):
        super().__init__(message)
