import json

from flask import request, g

from api.database.db import Database
from api.model.models import Green
from api.schema.schemas import green_schema
from api.schema.response_schema import ResponseSchema


def greens():
    db = g.get('db')
    final = None
    if request.method == 'GET':
        greens_response = Green.query.all()
        final = {
            "greens": green_schema.dump(greens_response)
        }
    else:
        form = request.get_json()
        if 'id' not in json.loads(request.data):
            green_id = db.next_id(Green)
            green = Green(identifier=green_id,
                          green_name=form['green_name'],
                          available=form['available'] ,
                          deadline=form['deadline'] if form['deadline'] is not None else None,
                          picked=form['picked'] if form['picked'] is not None else None,
                          producer=form['producer_id'],
                          pic_path=None,
                          price=form['price'])
            form['id'] = green_id
            db.upsert(green)
        else:
            exists_green = db.get_id(Green, form['id'])
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

    response = ResponseSchema(ResponseSchema.success, final)
    return json.dumps(response.__dict__)


def remove_green(id):
    db = Database()
    g = db._session.query(Green).filter_by(id=id).first()
    db.delete(g)
    return 'OK'
