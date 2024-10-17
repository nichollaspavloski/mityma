from ..pubsub import Subscriber
from api.database.db import get_db
from api.model.models import Log
"""
    Concrete Subscribers 
    Log the called requests in the console
    and register the logs in the database 
"""


class Logger(Subscriber):
    def update(self, event: str, data: dict):
        if event == 'logger':
            print(f"[LOGGER] >>> [{data['method']}] {data['path']}")
            if data['parameters'] is not None and data['parameters'] != '':
                print(f"[LOGGER] PARAMS: {data['parameters']}")


class DatabaseLogger(Subscriber):
    def update(self, event: str, data: dict):
        if event == 'database':
            db = get_db()
            log = Log(method=data['method'],
                      path=data['path'],
                      parameters=data['parameters'],
                      success=data['success'])
            db.upsert(log)
            db.commit()
