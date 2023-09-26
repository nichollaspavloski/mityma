from .command import Command

class ReceiverStatement:
    def __init__(self):
        self.transactions = ['upsert', 'delete']
        self.statements = {
            'upsert': [],
            'delete': []
        }

    def set_statements(self, transaction: str, statements: list):
        self.statements[transaction] = statements

    def get_statements(self):
        return self.statements

    def append_statements(self, transaction: str, statement):
        self.statements[transaction].append(statement)

    def clear_statements(self):
        for transaction in self.transactions:
            if self.statements[transaction]:
                self.statements[transaction].clear()


class Invoker:
    _on_start = None
    _on_finish = None

    def __init__(self, receiver: ReceiverStatement, session):
        self.receiver = receiver
        self.session = session

    def set_on_start(self, command: Command):
        self._on_start = command

    def set_on_finish(self, command: Command):
        self._on_finish = command

    def handle_transaction(self):
        if isinstance(self._on_start, Command):
            self._on_start.execute()

        if isinstance(self._on_finish, Command):
            self._on_finish.execute()
