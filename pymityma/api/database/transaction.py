"""
    Transaction class works as the invoker in Command pattern
    It appends and clears the commands from a list and is responsible to execute
    the upsert and delete commands when the commit command is called
"""


class Transaction:
    def __init__(self):
        self.statements = []

    def get_statements(self):
        return self.statements

    def append_statements(self, statement):
        self.statements.append(statement)

    def clear_statements(self):
        self.statements.clear()

    def execute_all(self):
        for statement in self.statements:
            statement.execute()
