from flask import Blueprint
from .main import *

green_api = Blueprint('green', __name__)
green_api.add_url_rule('/', view_func=greens, methods=['GET', 'POST'])
green_api.add_url_rule('/<id>', view_func=remove_green, methods=['DELETE'])
