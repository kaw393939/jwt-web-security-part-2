"""This allows Gunicorn to serve the app in production"""

from app import create_app, User

app = create_app()

