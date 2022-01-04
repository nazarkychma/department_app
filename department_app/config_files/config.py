"""
This module contains configs for Flask application.
"""
# pylint: disable=too-few-public-methods
from os import getenv


class Config:
    """
    Default config for Flask app
    """
    SQLALCHEMY_DATABASE_URI = getenv("db_uri")
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SESSION_TYPE = 'null'
    SECRET_KEY = 'super secret key'
    SESSION_PERMANENT = False
