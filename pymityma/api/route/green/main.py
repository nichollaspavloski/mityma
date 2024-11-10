import json
from datetime import datetime

from flask import request, g

from api.model.models import Green
from api.schema.schemas import green_schema
from api.schema.response_schema import ApiResponseBuilder

from api.utils.validator.strategy import DateValidation, ValidationContext

def greens():
    db = g.get('db')
    final = None
    if request.method == 'GET':
        greens_response = Green.query.all()
        final = {
            "greens": green_schema.dump(greens_response)
        }
    elif request.method == 'POST':
        form = request.get_json()

        context = ValidationContext(DateValidation())
        if 'deadline' in form and form['deadline'] is not None:
            if not context.validate(form['deadline']):
                return (
                    ApiResponseBuilder()
                        .set_status_code(400)
                        .set_success(0)
                        .add_info('errors', 'invalid date format in "deadline" parameter')
                        .build()
                )

        if 'picked' in form and form['picked'] is not None:
            if not context.validate(form['picked']):
                return (
                    ApiResponseBuilder()
                    .set_status_code(400)
                    .set_success(0)
                    .add_info('errors', 'invalid date format in "picked" parameter')
                    .build()
                )

        if 'id' not in json.loads(request.data):
            green_id = db.next_id(Green)
            green = Green(identifier=green_id,
                          green_name=form['green_name'],
                          available=form['available'],
                          deadline=datetime.strptime(form['deadline'], '%d-%m-%Y %H:%M') if form['deadline'] is not None else None,
                          picked=datetime.strptime(form['picked'], '%d-%m-%Y %H:%M') if form['picked'] is not None else None,
                          producer=form['producer_id'],
                          pic_path=None,
                          price=form['price'])
            form['id'] = green_id
            db.upsert(green)
        else:
            exists_green = db.query_by_id(Green, form['id'])
            exists_green.green_name = form['green_name']
            exists_green.available = form['available']
            exists_green.deadline = form['deadline'] if form['deadline'] is not None else None
            exists_green.picked = form['picked'] if form['picked'] is not None else None
            exists_green.producer_id = form['producer_id']
            exists_green.price = form['price']
            db.upsert(exists_green)

        final = {
            'green_id': form['id']
        }

    return ApiResponseBuilder().add_data(final).set_success(1).build()


def remove_green(id):
    db = g.get('db')
    db.delete(Green, id)

    return ApiResponseBuilder().set_success(1).build()
