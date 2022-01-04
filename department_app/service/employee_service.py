"""
This module contains class which implements CRUD operations for Employee

Classes:
    EmployeeService
"""
# pylint: disable=no-member
# pylint: disable=line-too-long
# pylint: disable=relative-beyond-top-level

import datetime

from department_app import db
from ..models.employee import Employee
from ..models.deparment import Department


class EmployeeService:
    """
    Class which provides functions to perform CRUD operations on Employee
    All functions are static
    """
    @staticmethod
    def get_employee_by_id(employee_id: int) -> dict:
        """
        Returns employee with given id
        :type employee_id: int
        :rtype: dict
        """
        employee = Employee.query.filter_by(id=employee_id).first()
        if employee is None:
            raise ValueError(f"Employee with id: {employee_id} doesn't exist")
        return employee.as_dict()

    @staticmethod
    def get_all_employees() -> list:
        """
        Returns all employees
        :rtype: list
        """
        return [employee.as_dict() for employee in Employee.query.all()]

    @staticmethod
    def delete_employee(employee_id: int) -> dict:
        """
        Deletes employee by given id
        Returns deleted employee
        :type employee_id: int
        :rtype: dict
        """
        employee = Employee.query.filter_by(id=employee_id).first()
        if employee is None:
            raise ValueError(f"Employee with id: {employee_id} doesn't exist")
        db.session.delete(employee)
        db.session.commit()
        return employee.as_dict()

    @staticmethod
    def update_employee(employee_id: int, updated_values: dict) -> dict:
        """
        Updates employee with given id by given values
        Returns updated employee
        :type employee_id: int
        :type updated_values: dict
        :rtype: dict
        """
        attrs = Employee.__dict__.keys()
        for key in list(updated_values.keys()):
            if key not in attrs or key == "id":
                del updated_values[key]
        if not updated_values:
            raise ValueError("Nothing to update")
        rows = Employee.query.filter_by(id=employee_id).update(updated_values)
        if rows == 0:
            raise ValueError(f"Employee with id: {employee_id} doesn't exist")
        db.session.commit()
        return Employee.query.filter_by(id=employee_id).first().as_dict()

    @staticmethod
    def get_employees_by_birthdate(lower_bound, upper_bound=None):
        """
        Filters and return list employees:
            - who were born on selected date if only lower bound is provided
            - who were born between lower and upper bounds if both are provided
        :type lower_bound: datetime.date
        :type upper_bound: datetime.date
        :rtype: list
        """
        if upper_bound is None:
            return [employee.as_dict() for employee in Employee.query.filter_by(birthdate=lower_bound).all()]
        if lower_bound > upper_bound:
            raise ValueError("Upper bound should be higher than lower")
        return [employee.as_dict() for employee in Employee.query.filter(Employee.birthdate >= lower_bound,
                                                                             Employee.birthdate <= upper_bound).all()]

    @staticmethod
    def create_employee(first_name: str, last_name: str, birthdate: datetime.date, salary: float, department_id: int) -> dict:
        """
        Creates and returns new employee with given values
        :type first_name: str
        :type last_name: str
        :type birthdate: datetime.date
        :type salary: float
        :param department_id:
        :type department_id: int
        :rtype: dict
        """
        if salary < 0:
            raise ValueError("Salary can't be lower than 0")
        if Department.query.filter_by(id=department_id).first() is None:
            raise ValueError(f"Department with id: {department_id} doesn't exist")
        employee = Employee(first_name=first_name, last_name=last_name,
                            birthdate=birthdate, salary=salary, department_id=department_id)
        db.session.add(employee)
        db.session.commit()
        return employee.as_dict()
