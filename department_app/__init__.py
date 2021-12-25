"""
This package contains app factory function
Import all necessary libs
"""
from flask import Flask


def create_app():
    app = Flask(__name__)

    return app
