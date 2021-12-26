"""
This module contains model which represents departments
"""
from department_app import db


class Department(db.Model):
    """
    Class describes department entity
    :field id: id of department
    :field name: name of department
    :field employees: list of employees
    """
    __tablename__ = "departments"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(40), unique=True, nullable=False)
    employees = db.relationship("Employee", backref="departments")
