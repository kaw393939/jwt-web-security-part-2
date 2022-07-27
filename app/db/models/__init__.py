from datetime import datetime
from sqlalchemy.orm import relationship, declarative_base
from flask_bcrypt import generate_password_hash, check_password_hash
from app.db import db

Base = declarative_base()


class Country(db.Model):
    __tablename__ = "countries"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, default="")
    cities = db.relationship("City", back_populates="country")

    def __init__(self, name):
        self.name = name


class City(db.Model):
    __tablename__ = "cities"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, default="")
    country_id = db.Column(db.Integer, db.ForeignKey("countries.id"))
    country = db.relationship("Country", back_populates="cities")

    def __init__(self, name, country_id):
        self.name = name
        self.country_id = country_id

class User(db.Model):
    """THis is the SQL Alchemy User model"""
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(300), nullable=False)
    about = db.Column(db.String(300), nullable=True, unique=False)
    authenticated = db.Column(db.Boolean, default=False)
    registered_on = db.Column('registered_on', db.DateTime)
    active = db.Column('is_active', db.Boolean(), nullable=False, server_default='1')

    def __init__(self, username, password):
        self.username = username
        self.set_password(password)
        self.registered_on = datetime.utcnow()

    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        return self.id

    def set_password(self, password):
        self.password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)

    def __repr__(self):
        return '<User %r>' % self.email
