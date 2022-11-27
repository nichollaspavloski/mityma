import json
import datetime

from flask import request, jsonify

from api.database.db import Database, interceptor
from api.model.models import Green
from api.schema.schemas import green_schema


@interceptor
def greens():
    db = Database()
    if request.method == 'GET':
        greens_response = Green.query.all()
        response = {
            "response": {
                "greens": green_schema.dump(greens_response)
            }
        }
        return jsonify(response)
    else:
        form = request.get_json()
        print(form['green_name'])
