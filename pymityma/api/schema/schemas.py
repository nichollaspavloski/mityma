from marshmallow_sqlalchemy import auto_field
from api.server import ma
from api.model.models import *


class ProducerSchema(ma.SQLAlchemySchema):
    class Meta:
        model = Producer
        include_fk = True

    id = auto_field()
    name = ma.Function(lambda obj: obj.person.person_name)
    is_mentor = auto_field()
    show_location = auto_field()
    person_id = auto_field()
    active = ma.Function(lambda obj: obj.person.active)
    login = ma.Function(lambda obj: obj.person.login)
    created_at = ma.Function(lambda obj: obj.person.creation_date.strftime("%d-%b-%Y %Hh%M"))
    location = ma.Function(lambda obj:
                           obj.person.location.street + ", " +
                           obj.person.location.no + " - " +
                           obj.person.location.city + " [" +
                           obj.person.location.state + "]")
    location_obj = ma.Function(lambda obj:
                               {
                                   'id': obj.person.location.id,
                                   'street': obj.person.location.street,
                                   'no': obj.person.location.no,
                                   'zip_code': obj.person.location.zip_code,
                                   'city': obj.person.location.city,
                                   'state': obj.person.location.state
                               })


class PurchaserSchema(ma.SQLAlchemySchema):
    class Meta:
        model = Purchaser

    id = auto_field()
    person = ma.Function(lambda obj: obj.category.description)
    person_id = auto_field()


class GreensSchema(ma.SQLAlchemySchema):
    class Meta:
        model = Green

    id = auto_field()
    green_name = auto_field()
    available = auto_field()
    deadline = ma.Function(lambda obj:
                           obj.deadline.strftime("%d-%m-%Y %H:%M")
                           if obj.deadline is not None
                           else None)
    picked = ma.Function(lambda obj:
                         obj.picked.strftime("%d-%m-%Y %H:%M")
                         if obj.picked is not None
                         else None)
    producer = ma.Function(lambda obj: obj.producer.person.person_name)
    producer_id = auto_field()
    price = ma.Function(lambda obj: '{:.2f}'.format(obj.price))


class LogSchema(ma.SQLAlchemySchema):
    class Meta:
        model = Log

    id = auto_field()
    method = auto_field()
    path = auto_field()
    success = auto_field()


producers_schema = ProducerSchema(many=True)
purchasers_schema = PurchaserSchema(many=True)
green_schema = GreensSchema(many=True)
log_schema = LogSchema(many=True)
