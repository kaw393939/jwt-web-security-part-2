"""First Test to make sure it runs locally"""
import json
from pprint import pprint

from flask_jwt_extended import create_access_token, decode_token

from app.db.models import User


def test_register(client):
    """This registers the user"""
    response = client.post("/register", json={"username": "keith", "password": "test"})
    response_data = response.get_json()
    assert response.status_code == 201
    assert response_data['username'] == 'keith'


def test_auth(client, create_user):
    """Test User Authentication"""
    data = {"username": "testUser", "password": "test"}
    response = client.post("/auth", json=data)
    response_data = response.get_json()
    access_token = response_data['access_token']
    token_value = decode_token(access_token)
    assert token_value['sub'] == 'testUser'


def test_protected(client, create_user):
    with client.application.app_context():
        access_token = create_token()
    token_value = decode_token(access_token)
    username = token_value['sub']
    assert username == 'testUser'
    headers = {
        'Authorization': 'Bearer {}'.format(access_token)
    }
    response = client.get('/user_info', headers=headers)
    response_data = response.get_json()
    assert response_data['username'] == 'testUser'


def create_token():
    user = User.query.first()
    access_token = create_access_token(user.username)
    return access_token
