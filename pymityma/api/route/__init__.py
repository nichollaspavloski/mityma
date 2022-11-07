from flask import Blueprint, request, jsonify, flash, abort
from api.model.models import Producer
from api.schema.schemas import producers_schema
from api.server.db import interceptor

producer_api = Blueprint('producer', __name__)


@producer_api.route('/', methods=['GET'])
def producers():
    # result = Producer.query.all()
    # return jsonify(producers_schema.dump(result))
    print('test url prefix')
    return 'OK'


@producer_api.route('/import_data', methods=['POST'])
@interceptor
def import_data():

    return 'OK'
