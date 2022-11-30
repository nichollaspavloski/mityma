from api.server import db
import datetime

"""generic entities"""


class Person(db.Model):
    __tablename__ = 'person'

    id = db.Column(db.BigInteger, primary_key=True, autoincrement=False)
    person_name = db.Column(db.String, nullable=False)
    login = db.Column(db.String, nullable=False)
    external_id = db.Column(db.String)
    active = db.Column(db.Boolean, nullable=False, default=True)
    location_id = db.Column(db.BigInteger, db.ForeignKey('location.id'), nullable=False)
    location = db.relationship('Location', backref='person_location')
    creation_date = db.Column(db.DateTime, nullable=False, default=datetime.datetime.utcnow())

    def __init__(self, identifier, person_name, login, location_id, creation_date):
        self.id = identifier
        self.person_name = person_name
        self.login = login
        self.location_id = location_id
        self.creation_date = creation_date


class Location(db.Model):
    __tablename__ = 'location'

    id = db.Column(db.BigInteger, primary_key=True, autoincrement=False)
    street = db.Column(db.String, nullable=False)
    no = db.Column(db.String, nullable=False)
    zip_code = db.Column(db.String, nullable=False)
    city = db.Column(db.String, nullable=False)
    state = db.Column(db.String, nullable=False)

    def __init__(self, identifier, street, no, zip_code, city, state):
        self.id = identifier
        self.street = street
        self.no = no
        self.zip_code = zip_code
        self.city = city
        self.state = state


"""personas entities"""


class Producer(db.Model):
    __tablename__ = 'producer'

    id = db.Column(db.BigInteger, primary_key=True, autoincrement=False)
    person_id = db.Column(db.BigInteger, db.ForeignKey('person.id'), nullable=False)
    person = db.relationship('Person', backref='producer_person')
    is_mentor = db.Column(db.Boolean, nullable=False)
    show_location = db.Column(db.Boolean, nullable=False, default=False)

    def __init__(self, identifier, person_id, is_mentor, show_location):
        self.id = identifier
        self.person_id = person_id
        self.is_mentor = is_mentor
        self.show_location = show_location


class Purchaser(db.Model):
    __tablename__ = 'purchaser'

    id = db.Column(db.BigInteger, primary_key=True, autoincrement=False)
    person_id = db.Column(db.BigInteger, db.ForeignKey('person.id'), nullable=False)
    person = db.relationship('Person', backref='purchaser_person')

    def __init__(self, person):
        self.person = person


"""planting area entities"""


class PlantingArea(db.Model):
    __tablename__ = 'planting_area'

    id = db.Column(db.Integer, primary_key=True, autoincrement=False)
    area_name = db.Column(db.String, nullable=False)
    location_id = db.Column(db.BigInteger, db.ForeignKey('location.id'), nullable=False)
    location = db.relationship('Location', backref='planting_area_location')
    is_public = db.Column(db.Boolean, nullable=False)

    def __init__(self, area_name, location, is_public):
        self.area_name = area_name
        self.location = location
        self.is_public = is_public


class PlantingAreaPlat(db.Model):
    __tablename__ = 'planting_area_plat'

    id = db.Column(db.Integer, primary_key=True, autoincrement=False)
    planting_area_id = db.Column(db.Integer, db.ForeignKey('planting_area.id', ondelete="CASCADE"), nullable=False)
    planting_area = db.relationship('PlantingArea', backref='planting_area_plat')

    def __init__(self, planting_area):
        self.planting_area = planting_area


class ProducerPlat(db.Model):
    __tablename__ = 'producer_plat'

    id = db.Column(db.Integer, primary_key=True, autoincrement=False)
    producer_id = db.Column(db.Integer, db.ForeignKey('producer.id', ondelete="CASCADE"), nullable=False)
    producer = db.relationship('Producer', backref='producer_plat')
    plat_id = db.Column(db.Integer, db.ForeignKey('planting_area_plat.id', ondelete="CASCADE"), nullable=False)
    plat = db.relationship('PlantingAreaPlat', backref='producer_planting_area_plat')

    def __init__(self, producer, plat):
        self.producer = producer
        self.plat = plat


"""products entities"""


class Green(db.Model):
    __tablename__ = 'green'

    id = db.Column(db.Integer, primary_key=True, autoincrement=False)
    green_name = db.Column(db.String, nullable=False)
    available = db.Column(db.Boolean, nullable=False)
    deadline = db.Column(db.Date)
    picked = db.Column(db.DateTime)
    producer_id = db.Column(db.Integer, db.ForeignKey('producer.id', ondelete="CASCADE"), nullable=False)
    producer = db.relationship('Producer', backref='producer_green')
    pic_path = db.Column(db.String)
    price = db.Column(db.Float)

    def __init__(self, identifier, green_name, available, deadline, picked, producer, pic_path, price):
        self.id = identifier
        self.green_name = green_name
        self.available = available
        self.deadline = deadline
        self.picked = picked
        self.producer_id = producer
        self.pic_path = pic_path
        self.price = price
