from . import *
from api.model.models import Producer
from api.schema.schemas import producers_schema


@producer_api.route('/', methods=['GET'])
def records():
    # result = Producer.query.all()
    # return jsonify(producers_schema.dump(result))
    print('test url prefix')
    return 'OK'
