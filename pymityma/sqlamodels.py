# coding: utf-8
from sqlalchemy import BigInteger, Boolean, Column, Date, DateTime, Float, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
metadata = Base.metadata


class Location(Base):
    __tablename__ = 'location'

    id = Column(BigInteger, primary_key=True)
    street = Column(String, nullable=False)
    no = Column(String, nullable=False)
    zip_code = Column(String, nullable=False)
    city = Column(String, nullable=False)
    state = Column(String, nullable=False)


class Person(Base):
    __tablename__ = 'person'

    id = Column(BigInteger, primary_key=True)
    person_name = Column(String, nullable=False)
    login = Column(String, nullable=False)
    external_id = Column(String)
    active = Column(Boolean, nullable=False)
    location_id = Column(ForeignKey('location.id'), nullable=False)
    creation_date = Column(DateTime, nullable=False)

    location = relationship('Location')


class PlantingArea(Base):
    __tablename__ = 'planting_area'

    id = Column(Integer, primary_key=True)
    area_name = Column(String, nullable=False)
    location_id = Column(ForeignKey('location.id'), nullable=False)
    is_public = Column(Boolean, nullable=False)

    location = relationship('Location')


class PlantingAreaPlat(Base):
    __tablename__ = 'planting_area_plat'

    id = Column(Integer, primary_key=True)
    planting_area_id = Column(ForeignKey('planting_area.id', ondelete='CASCADE'), nullable=False)

    planting_area = relationship('PlantingArea')


class Producer(Base):
    __tablename__ = 'producer'

    id = Column(BigInteger, primary_key=True)
    person_id = Column(ForeignKey('person.id'), nullable=False)
    is_mentor = Column(Boolean, nullable=False)
    show_location = Column(Boolean, nullable=False)

    person = relationship('Person')


class Purchaser(Base):
    __tablename__ = 'purchaser'

    id = Column(BigInteger, primary_key=True)
    person_id = Column(ForeignKey('person.id'), nullable=False)

    person = relationship('Person')


class Green(Base):
    __tablename__ = 'green'

    id = Column(Integer, primary_key=True)
    green_name = Column(String, nullable=False)
    available = Column(Boolean, nullable=False)
    deadline = Column(Date)
    picked = Column(DateTime)
    producer_id = Column(ForeignKey('producer.id', ondelete='CASCADE'), nullable=False)
    pic_path = Column(String)
    price = Column(Float(53))

    producer = relationship('Producer')


class ProducerPlat(Base):
    __tablename__ = 'producer_plat'

    id = Column(Integer, primary_key=True)
    producer_id = Column(ForeignKey('producer.id', ondelete='CASCADE'), nullable=False)
    plat_id = Column(ForeignKey('planting_area_plat.id', ondelete='CASCADE'), nullable=False)

    plat = relationship('PlantingAreaPlat')
    producer = relationship('Producer')
