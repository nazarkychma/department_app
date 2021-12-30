"""
This module contains model which represents employee
"""
from department_app import db
from datetime import datetime
from .deparment import Department


class Employee(db.Model):
    """
    Class describes employee entity
    :field id: id of employee
    :field first_name: employees' first name
    :field last_name: employees' last name
    :field birthdate: employees' birthdate
    :field salary: employee's salary
    :field department_id: id of department employee belongs to
    """
    __tablename__ = "employees"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)
    birthdate = db.Column(db.DATE, default=datetime.now().date())
    salary = db.Column(db.Float, nullable=False)
    department_id = db.Column(db.Integer, db.ForeignKey("departments.id"))

    def as_dict(self):
        return {"id": self.id,
                "name": " ".join([self.first_name, self.last_name]),
                "birthdate": self.birthdate,
                "salary": self.salary,
                "department_id": self.department_id,
                "department_name": Department.query.filter_by(id=self.department_id).first().name}
