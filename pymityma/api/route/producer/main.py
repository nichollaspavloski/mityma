import json
import datetime

from flask import request, jsonify

from api.database.db import Database, interceptor
from api.model.models import Person, Producer, Location
from api.schema.schemas import producers_schema
from api.schema.response_schema import ResponseSchema


@interceptor
def producers():
    db = Database()
    final = None
    if request.method == 'GET':
        producers_response = Producer.query.all()
        final = {
            "producers": producers_schema.dump(producers_response)
        }
    elif request.method == 'POST':
        form = request.get_json()
        location = form['location_obj']

        if 'person_id' in json.loads(request.data):
            # location
            exists_location = db.get_id(Location, location['id'])
            exists_location.street = location['street']
            exists_location.no = location['no']
            exists_location.zip_code = location['zip_code']
            exists_location.city = location['city']
            exists_location.state = location['state']

            # person
            exists_person = db.get_id(Person, form['person_id'])
            exists_person.person_name = form['name']
            exists_person.login = form['login']
            exists_person.location_id = location['id']

            # producer
            exists_producer = db.get_id(Producer, form['id'])
            exists_producer.is_mentor = form['is_mentor']
            exists_producer.show_location = form['show_location']
        else:
            location_id = db.next_id(Location)
            location = Location(identifier=location_id,
                                street=location['street'],
                                no=location['no'],
                                zip_code=location['zip_code'],
                                city=location['city'],
                                state=location['state'])
            db.insert(location)

            person_id = db.next_id(Person)
            person = Person(identifier=person_id,
                            person_name=form['name'],
                            login=form['login'],
                            location_id=location_id,
                            creation_date=datetime.datetime.utcnow())
            db.insert(person)
            form['person_id'] = person_id

            producer_id = db.next_id(Producer)
            p = Producer(identifier=producer_id,
                         person_id=person_id,
                         is_mentor=form['is_mentor'],
                         show_location=form['show_location'])
            form['id'] = producer_id

            db.insert(p)

        final = {
            'person_id': form['person_id'],
            'producer_id': form['id']
        }

    response = ResponseSchema(ResponseSchema.success, final)
    return json.dumps(response.__dict__)


@interceptor
def remove_producer(id):
    db = Database()
    p = db.session.query(Producer).filter_by(id=id).first()
    db.delete(p)
    return 'OK'
