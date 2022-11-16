from flask import Blueprint, request, jsonify, flash, abort
from .producer import *
from api.model.models import Producer
from api.schema.schemas import producers_schema
from api.server.db import interceptor

producer_api = Blueprint('producer', __name__)
producer_api.add_url_rule('/', view_func=producers, methods=['GET', 'POST'])
producer_api.add_url_rule('/<id>', view_func=remove_producer, methods=['DELETE'])
