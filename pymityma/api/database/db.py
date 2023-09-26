from ..server import db
from sqlalchemy import func
from .invoker_receiver import *
from .commands import *


database = None
@staticmethod
def get_db():
    if database is None:
        return Database()
    else:
        return database


class Database:
    _session = None
    def __init__(self):
        if self._session is None:
            self._session = db.session()

        self.engine = db.get_engine()

        self.receiver = ReceiverStatement()
        self.invoker = Invoker(self.receiver, self._session)

        self.invoker.set_on_finish(CommitCommand(self._session, self.receiver.get_statements()))

    def commit(self):
        command = CommitCommand(self._session, self.receiver.get_statements())
        command.execute()
        self.receiver.clear_statements()

    def rollback(self):
        command = RollbackCommand(self._session)
        command.execute()
        self.receiver.clear_statements()

    def upsert(self, model: db.Model):
        self.receiver.append_statements('upsert', model)

    def delete(self, model: db.Model):
        self.receiver.append_statements('delete', model)

    def query(self, qry: str):
        self.statements.append(self._session.execute(qry))

    def next_id(self, model: db.Model) -> int:
        result = self._session.query(func.max(model.id)).scalar()
        next_id = 1 if result is None else result + 1
        return next_id

    @staticmethod
    def get_id(model: db.Model, model_id):
        result = model.query.filter_by(id=model_id).first()
        return None if result is None else result

class DatabaseException(Exception):
    def __init__(self, message):
        super().__init__(message)
