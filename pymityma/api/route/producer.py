from . import *
from api.model.models import Producer
from api.schema.schemas import producers_schema


@record_api.route('/', methods=['GET'])
def records():
    result = Producer.query.all()
    return jsonify(producers_schema.dump(result))
