from . import *
from api.model.models import Producer
from api.schema.schemas import producers_schema


def producers():
    result = Producer.query.all()
    return jsonify(producers_schema.dump(result))
