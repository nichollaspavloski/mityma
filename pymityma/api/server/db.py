from . import db
from sqlalchemy import func
from functools import wraps


def interceptor(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        try:
            result = func(*args, **kwargs)
            db.session.commit()
        except DatabaseException:
            db.session.rollback()
        except Exception as e:
            print(e)
            db.session.rollback()

        return result
    return wrapper


class Database:
    def __init__(self):
        self._engine = db.get_engine()
        self._session = db.session()
        self._statements = []

    def commit(self):
        self._session.commit()
        self._statements.clear()

    def rollback(self):
        self._session.rollback()
        self._statements.clear()

    def insert(self, model: db.Model):
        self._statements.append(self._session.add(model))

    def delete(self, model: db.Model):
        self._statements.append(self._session.delete(model))

    def query(self, qry: str):
        self._statements.append(self._session.execute(qry))

    def next_id(self, model: db.Model) -> int:
        result = self._session.query(func.max(model.id)).scalar()
        next_id = 1 if result is None else result + 1
        return next_id

    @staticmethod
    def has_id(model: db.Model, model_id):
        result = model.query.filter_by(id=model_id).first()
        return result is not None


class DatabaseException(Exception):
    def __init__(self, message):
        super().__init__(message)
