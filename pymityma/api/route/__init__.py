from flask import Blueprint, request, jsonify, flash, abort
from api.model.models import Producer
from api.schema.schemas import producers_schema
from api.server.db import interceptor

record_api = Blueprint('records', __name__)


@record_api.route('/', methods=['GET'])
def records():
    result = Producer.query.all()
    return jsonify(producers_schema.dump(result))


@record_api.route('/import_data', methods=['POST'])
@interceptor
def import_data():

    return 'OK'
