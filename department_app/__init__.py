"""
This package contains app factory function
Import all necessary libs
"""
import datetime

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

from .config_files.config import Config

db = SQLAlchemy()
migrate = Migrate()


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    from .models.employee import Employee
    from .models.deparment import Department

    db.init_app(app)
    migrate.init_app(app, db)

    from .views.departments_view import department_bp
    from .views.employees_view import employee_bp

    app.register_blueprint(department_bp)
    app.register_blueprint(employee_bp)

    #with app.app_context():
        # db.create_all()

    return app
