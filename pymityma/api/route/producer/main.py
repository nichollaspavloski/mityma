import json
from datetime import datetime
from zoneinfo import ZoneInfo
from dateutil.relativedelta import relativedelta

from flask import request, g

from api.model.models import Person, Producer, Location
from api.schema.schemas import producers_schema
from api.schema.response_schema import ApiResponseBuilder

from api.utils.validator.strategy import AgeValidation, DateValidation, ValidationContext


def producers():
    db = g.get('db')
    final = None
    if request.method == 'GET':
        producers_response = Producer.query.all()
        final = {
            "producers": producers_schema.dump(producers_response)
        }
    elif request.method == 'POST':
        form = request.get_json()

        context = ValidationContext(DateValidation())
        if not context.validate(form['date_of_birth']):
            return (
                ApiResponseBuilder()
                    .set_status_code(400)
                    .add_info('errors', 'invalid date of birth')
                    .set_success(0)
                    .build()
            )

        context.set_strategy(AgeValidation())
        age = relativedelta(datetime.today(), datetime.strptime(form['date_of_birth'], '%d-%m-%Y')).years
        if not context.validate(age):
            return (
                ApiResponseBuilder()
                .set_status_code(400)
                .add_info('errors', 'invalid age range [14~80]')
                .set_success(0)
                .build()
            )

        location = form['consolidate_location']

        if 'person_id' in json.loads(request.data):
            # location
            exists_location = db.query_by_id(Location, location['id'])
            exists_location.street = location['street']
            exists_location.no = location['no']
            exists_location.zip_code = location['zip_code']
            exists_location.city = location['city']
            exists_location.state = location['state']

            # person
            exists_person = db.query_by_id(Person, form['person_id'])
            exists_person.person_name = form['name']
            exists_person.login = form['login']
            exists_person.location_id = location['id']
            exists_person.age = form['age']

            # producer
            exists_producer = db.query_by_id(Producer, form['id'])
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
            db.upsert(location)

            person_id = db.next_id(Person)
            person = Person(identifier=person_id,
                            person_name=form['name'],
                            login=form['login'],
                            date_of_birth=datetime.strptime(form['date_of_birth'], '%d-%m-%Y'),
                            location_id=location_id,
                            creation_date=datetime.now(tz=ZoneInfo('America/Sao_Paulo')))
            db.upsert(person)
            form['person_id'] = person_id

            producer_id = db.next_id(Producer)
            p = Producer(identifier=producer_id,
                         person_id=person_id,
                         is_mentor=form['is_mentor'] if 'is_mentor' in form else False,
                         show_location=form['show_location'] if 'show_location' in form else False)
            form['id'] = producer_id

            db.upsert(p)

        final = {
            'person_id': form['person_id'],
            'producer_id': form['id']
        }

    return ApiResponseBuilder().set_success(1).add_data(final).build()


def remove_producer(id):
    db = g.get('db')
    db.delete(Producer, id)

    return ApiResponseBuilder().set_success(1).build()
