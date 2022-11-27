from ..server import db
from sqlalchemy import func
from functools import wraps


def interceptor(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        try:
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
        self.engine = db.get_engine()
        self.session = db.session()
        self.statements = []

    def commit(self):
        self.session.commit()
        self.statements.clear()

    def rollback(self):
        self.session.rollback()
        self.statements.clear()

    def insert(self, model: db.Model):
        self.statements.append(self.session.add(model))

    def delete(self, model: db.Model):
        self.statements.append(self.session.delete(model))

    def query(self, qry: str):
        self.statements.append(self.session.execute(qry))

    def next_id(self, model: db.Model) -> int:
        result = self.session.query(func.max(model.id)).scalar()
        next_id = 1 if result is None else result + 1
        return next_id

    @staticmethod
    def get_id(model: db.Model, model_id):
        result = model.query.filter_by(id=model_id).first()
        return None if result is None else result


class DatabaseException(Exception):
    def __init__(self, message):
        super().__init__(message)
