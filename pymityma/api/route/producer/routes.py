from flask import Blueprint
from .main import *

producer_api = Blueprint('producer', __name__)
producer_api.add_url_rule('/', view_func=producers, methods=['GET', 'POST', 'OPTIONS'])
producer_api.add_url_rule('/<id>', view_func=remove_producer, methods=['DELETE'])
