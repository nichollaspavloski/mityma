from .command import Command
from sqlalchemy import Table

class SelectCommand(Command):
    def __init__(self, **kwargs) -> None:
        pass

    def execute(self) -> None:
        print('select')


class UpsertCommand(Command):
    def __init__(self, session, model) -> None:
        self.session = session
        self.model = model

    def execute(self) -> None:
        self.session.add(self.model)


class DeleteCommand(Command):
    def __init__(self, engine, model) -> None:
        self.engine = engine
        self.model = model

    def execute(self) -> None:
        table = Table(self.model.__tablename__)
        self.session.query(table.name).filter(table.c.id == self.model.id).delete()


class CommitCommand(Command):
    def __init__(self, session, statements: dict) -> None:
        self.session = session
        self.statements = statements


    def execute(self) -> None:
        transactions = ['upsert', 'delete']
        for transaction in transactions:
            for statement in self.statements[transaction]:
                if transaction == 'upsert':
                    command = UpsertCommand(self.session, statement)
                else:
                    command = DeleteCommand(self.session, statement)
                command.execute()

        self.session.commit()


class RollbackCommand(Command):
    def __init__(self, session) -> None:
        self.session = session

    def execute(self) -> None:
        self.session.rollback()

