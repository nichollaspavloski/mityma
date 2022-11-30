import json

from flask import request, jsonify

from api.database.db import Database, interceptor
from api.model.models import Green
from api.schema.schemas import green_schema


@interceptor
def greens():
    db = Database()
    if request.method == 'GET':
        greens_response = Green.query.all()
        response = {
            "response": {
                "greens": green_schema.dump(greens_response)
            }
        }
        return jsonify(response)
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
            db.insert(green)
        else:
            exists_green = db.get_id(Green, form['id'])
            exists_green.green_name = form['green_name']
            exists_green.available = form['available']
            exists_green.deadline = form['deadline'] if form['deadline'] is not None else None
            exists_green.picked = form['picked'] if form['picked'] is not None else None
            exists_green.producer_id = form['producer_id']
            exists_green.price = form['price']

        response = {
            'green_id': form['id']
        }
        return jsonify(response)


@interceptor
def remove_green(id):
    db = Database()
    g = db.session.query(Green).filter_by(id=id).first()
    db.delete(g)
    return 'OK'
