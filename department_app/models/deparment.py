"""
This module contains model which represents departments
"""
# pylint: disable=too-few-public-methods
# pylint: disable=no-member
from department_app import db


class Department(db.Model):
    """
    Class describes department entity
    :field id: id of department
    :field name: name of department
    :field employees: list of employees
    """
    __tablename__ = "departments"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(40), unique=True, nullable=False)
    employees = db.relationship("Employee", backref="departments")

    def get_avg_salary(self) -> float:
        """
        Returns average salary of department
        :rtype: float
        """
        salaries = [employee.salary for employee in self.employees]
        if salaries:
            return round(sum(salaries) / len(salaries), 2)
        return 0

    def as_dict(self) -> dict:
        """
        Returns department model converted to dict
        :rtype: dict
        """
        return {"id": self.id,
                "name": self.name,
                "avg_salary": self.get_avg_salary(),
                "num_of_employees": len(self.employees),
                "employees": [employee.as_dict() for employee in self.employees]}
