import os

import pandas as pd
from flask.views import MethodView
from flask_jwt_extended import jwt_required
from flask_smorest import Blueprint, Page
from app.db.models import Country, City
from app.db import db
from marshmallow import Schema, fields, EXCLUDE

geography = Blueprint('geography', __name__, url_prefix="/geography", description="Operations on Locations")


class CountrySchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.String()

    class Meta:
        type_ = "Country"
        strict = True


class CitySchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.String()
    country_id = fields.Integer()

    class Meta:
        type_ = "City"
        strict = True


@geography.route('/countries')
class Countries(MethodView):

    @geography.etag
    @geography.response(200, CountrySchema(many=True))
    def get(self):
        """List Countries"""
        ret = Country.query.all()

        return ret

    @geography.etag
    @geography.arguments(CountrySchema, location="json")
    @geography.response(201, CountrySchema)
    @geography.doc(security=[{"bearerAuth": []}])
    @jwt_required()
    def post(self, new_item):
        """Add a Country"""

        item = Country(**new_item)
        db.session.add(item)
        db.session.commit()
        return item


@geography.route('/cities')
class Countries(MethodView):

    @geography.etag
    @geography.response(200, CitySchema(many=True))
    def get(self):
        """List Cities"""
        ret = City.query.all()
        return ret

    @geography.etag
    @geography.arguments(CitySchema, location="json")
    @geography.response(201, CitySchema)
    @geography.doc(security=[{"bearerAuth": []}])
    @jwt_required()
    def post(self, new_item):
        """Add a City"""

        item = City(**new_item)
        db.session.add(item)
        db.session.commit()
        return item

