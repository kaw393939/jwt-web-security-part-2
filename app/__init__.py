"""A simple flask web app"""
import os

import pandas as pd
from flask import Flask
from flask_bcrypt import Bcrypt
from flask_jwt_extended import JWTManager
from flask_smorest import Api

from app.authentication import authentication
from app.db import db, database
from app.db.models import User, Country, City
from app.geography import geography
from app.logging_config import logging_config
from flask_cors import CORS

def create_app():
    """Create and configure an instance of the Flask application."""
    app = Flask(__name__)
    if app.config["ENV"] == "production":
        app.config.from_object("app.config.ProductionConfig")
    elif app.config["ENV"] == "development":
        app.config.from_object("app.config.DevelopmentConfig")
    elif app.config["ENV"] == "testing":
        app.config.from_object("app.config.TestingConfig")
    # initializes the database connection for the app
    db.init_app(app)
    app.register_blueprint(database)
    app.register_blueprint(logging_config)
    with app.app_context():
        jwt = JWTManager(app)

        api = Api(app)
        api.spec.components.security_scheme("bearerAuth", {"type": "http", "scheme": "bearer", "bearerFormat": "JWT"})
        api.register_blueprint(authentication)
        api.register_blueprint(geography)
        load_app_data()
        api_v1_cors_config = {
            "methods": ["OPTIONS", "GET", "POST", "PUT", "DELETE", "PATCH"],
        }
        CORS(app, resources={"/*": api_v1_cors_config})
        @jwt.user_identity_loader
        def user_identity_lookup(user):
            return user

        @jwt.user_lookup_loader
        def user_lookup_callback(_jwt_header, jwt_data):
            identity = jwt_data["sub"]
            return User.query.filter_by(username=identity).one_or_none()

    return app

def load_app_data():
    db.create_all()
    path = os.path.dirname(os.path.abspath(__file__))
    data_path = os.path.join(path, '..', 'data', 'worldcities.csv')
    # makes data frame to hold the world cities data
    df = pd.read_csv(data_path)
    # Gets a list of unique countries from the data frame
    countries = df.country.unique()
    for country_name in countries:
        # this creates a country model based on Sqlalchemy model
        country = Country(name=country_name)
        db.session.add(country)
        db.session.commit()
        # get a list of cities from the data frame that are in the country selected
        cities = df.loc[df.country == country_name]
        # looping through all the cities
        for city_string in cities['city_ascii']:
            # Create a new city
            city = City(name=city_string, country_id=country.id)
            # Set the name
            # append the city to the country
            db.session.add(city)
        db.session.commit()
