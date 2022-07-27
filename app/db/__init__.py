"""Database Setup"""
import os

import pandas as pd
from flask import Blueprint, current_app
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

database = Blueprint('database', __name__)


@database.cli.command('create')
def init_db():
    """manual command to create the datbase file"""
    db.create_all()


@database.before_app_first_request
def create_db_file_if_does_not_exist():
    """Creates the db file if it doesn't exist"""
    if not os.path.exists(current_app.config['DB_DIRECTORY_LOCATION']):
        os.mkdir(current_app.config['DB_DIRECTORY_LOCATION'])
        db.create_all()


