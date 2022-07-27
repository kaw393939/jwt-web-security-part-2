"""These are the routes to login, register, and protect a route"""
import json
from datetime import datetime
from pprint import pprint

from flask import request, jsonify
from flask_jwt_extended import create_access_token, jwt_required, current_user, decode_token
from flask_smorest import Blueprint, abort
from marshmallow import Schema, fields, EXCLUDE

from app.db import db
from app.db.models import User

authentication = Blueprint('authentication', __name__, url_prefix="/", description="Operations on users")


class RegisterUserSchema(Schema):
    id = fields.Int(dump_only=True)
    username = fields.String()
    password = fields.String()

    class Meta:
        type_ = "User"
        strict = True


class RegisterUserResponseSchema(Schema):
    username = fields.String()

    class Meta:
        type_ = "User"
        strict = True


class LoginUserSchemaResponse(Schema):
    access_token = fields.String()


class LoginUserSchemaPost(Schema):
    id = fields.Int(dump_only=True)
    username = fields.String()
    password = fields.String()

    class Meta:
        type_ = "User"
        strict = True


class ProtectedRouteSchema(Schema):
    Authorization = fields.String()


class JWTSchema(Schema):
    class Meta:
        unknown = EXCLUDE
        ordered = True

    access_token = fields.Str()
    token_type = fields.Str()
    expires = fields.Str()


@authentication.route('/register', methods=['POST'])
@authentication.arguments(RegisterUserSchema, location="json")
@authentication.response(201, RegisterUserResponseSchema)
def register(data):
    """Register a User

    Return a user.
    ---
    Internal comment not meant to be exposed.
    """
    # Check if there are any users.  The first user will be made an admin

    username = data['username']
    password = data['password']
    if User.query.count() == 0:
        user = User(username=username, password=password)
    else:
        user = User.query.filter_by(username=username).first()
        if user is None:
            user = User(username=username, password=password)
        else:
            return jsonify("Already Registered"), 200
    db.session.add(user)
    db.session.commit()
    return user, 201


# Create a route to authenticate your users and return JWTs. The
# create_access_token() function is used to actually generate the JWT.
@authentication.route("/auth", methods=["POST"])
@authentication.arguments(LoginUserSchemaPost, location="json")
@authentication.response(201, JWTSchema)
def login(data):
    username = data['username']
    password = data['password']
    user = User.query.filter_by(username=username).first()
    if user is None or not user.check_password(password):
        abort(401, message="Invalid Username or Password")
    else:
        user.authenticated = True
        db.session.add(user)
        db.session.commit()
        access_token = create_access_token(identity=username)
        pure_decoded = decode_token(access_token)
        return jsonify(access_token=access_token,
                       token_type='Bearer',
                       expires=datetime.fromtimestamp(pure_decoded["exp"]).strftime('%Y-%m-%d %H:%M:%S')), 200


@authentication.route("/user_info", methods=["GET"])
@authentication.doc(security=[{"bearerAuth": []}])
@jwt_required()
def protected():
    # We can now access our sqlalchemy User object via `current_user`.
    return jsonify(
        id=current_user.id,
        username=current_user.username,
    )
