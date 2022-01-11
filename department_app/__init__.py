"""
This package contains app factory function
Import all necessary libs
"""
# pylint: disable=import-outside-toplevel
# pylint: disable=unused-import
# pylint: disable=cyclic-import
import logging
from flask import Flask, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_restful import Api

from .config_files import Config as DefaultCfg, TestConfig

db = SQLAlchemy()
migrate = Migrate()
api = Api(prefix="/api")

# pylint: disable=wrong-import-position
from .rest.department_api import DepartmentsApi, DepartmentApi
from .rest.employee_api import EmployeeApi, EmployeesApi, EmployeesFilter

api.add_resource(DepartmentsApi, '/department')
api.add_resource(DepartmentApi, '/department/<int:id_>')
api.add_resource(EmployeesApi, '/employee')
api.add_resource(EmployeeApi, '/employee/<int:id_>')
api.add_resource(EmployeesFilter, '/employee/filter')


def create_app(cfg=DefaultCfg):
    """
    Creates Flask application
    :return: an instance of Flask application
    """
    app = Flask(__name__)
    app.config.from_object(cfg)

    from .views.departments_view import department_bp
    from .views.employees_view import employee_bp
    app.register_blueprint(department_bp)
    app.register_blueprint(employee_bp)

    from .models.employee import Employee
    from .models.deparment import Department

    db.init_app(app)
    migrate.init_app(app, db)
    api.init_app(app)

    @app.route("/", methods=["GET"])
    def index():
        return redirect(url_for("departments.all_departments"))

    return app
