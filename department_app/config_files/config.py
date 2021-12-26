from os import getenv


class Config:
    SQLALCHEMY_DATABASE_URI = getenv("db_uri", "sqlite:///department_app.db")
    SQLALCHEMY_TRACK_MODIFICATIONS = False
