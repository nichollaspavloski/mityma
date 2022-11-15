from marshmallow_sqlalchemy import auto_field
from api.server import ma
from api.model.models import *


class ProducerSchema(ma.SQLAlchemySchema):
    class Meta:
        model = Producer
        include_fk = True

    id = auto_field()
    name = ma.Function(lambda obj: obj.person.person_name + " " + obj.person.lastname)
    is_mentor = auto_field()
    show_location = auto_field()
    person_id = auto_field()
    created_at = ma.Function(lambda obj: obj.person.creation_date)
    location = ma.Function(lambda obj:
                           obj.person.location.street + ", " +
                           obj.person.location.no + " - " +
                           obj.person.location.city + " [" +
                           obj.person.location.state + "]")


class PurchaserSchema(ma.SQLAlchemySchema):
    class Meta:
        model = Purchaser

    id = auto_field()
    person = ma.Function(lambda obj: obj.category.description)
    person_id = auto_field()


producers_schema = ProducerSchema(many=True)
purchasers_schema = PurchaserSchema(many=True)
