from flask_marshmallow import Marshmallow, Schema


class ResponseSchema(Schema):
    class Meta:
        fields = ('result', 'data')
