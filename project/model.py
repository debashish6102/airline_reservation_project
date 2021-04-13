from project import db
from datetime import datetime
from project import db
from flask_login import UserMixin
from sqlalchemy.sql import func


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    fname = db.Column(db.String(20), nullable=False)
    mname = db.Column(db.String(20))
    lname = db.Column(db.String(20), nullable=False)
    password_hash = db.Column(db.String(16), nullable=False)
    sex = db.Column(db.String(20), nullable=False)
    phone = db.Column(db.Integer, nullable=False, unique=True)
    email = db.Column(db.String(20), nullable=False, unique=True)
    adhaar = db.Column(db.Integer, nullable=False, unique=True)
    city_id = db.column(db.Integer, db.ForeignKey('city.id'))
    user_name = db.Column(db.String(30), nullable=False, unique=True)


class City(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    city_name = db.Column(db.String(30), nullable=False, unique=True)
    state = db.Column(db.String(10), nullable=False)
    country = db.Column(db.String(10), nullable=False)


class Flight(db.Model):
    flight_no = db.Column(db.Integer, unique=True, nullable=False, primary_key=True)
    city_source = db.Column(db.String(10), db.ForeignKey('airport.id'))
    city_destination = db.Column(db.String(10), db.ForeignKey('airport.id'))
    no_of_seats = db.Column(db.Integer, nullable=False)
    time_dept = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    time_arrival = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    time_duration = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    price = db.Column(db.Integer, nullable=False)


class Airport(db.Model):
    airport_name = db.Column(db.String(50), unique=True, nullable=False)
    id = db.Column(db.Integer, primary_key=True)
