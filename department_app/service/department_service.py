"""
This module contains class which implements CRUD operations for Department

Classes:
    DepartmentService
"""
# pylint: disable=no-member
from department_app import db
from ..models.deparment import Department


class DepartmentService:
    """
    Class which provides functions to perform CRUD operations on Department
    All functions are static
    """
    @staticmethod
    def get_department(department_id: int) -> dict:
        """
        Returns departments by giver id
        :type department_id: int
        :rtype: dict
        """
        department = Department.query.filter_by(id=department_id).first()
        if department is None:
            raise ValueError(f"Department with id: {department_id} doesn't exist")
        return department.as_dict()

    @staticmethod
    def get_all_departments() -> list:
        """
        Returns all departments
        :rtype: list
        """
        return [department.as_dict() for department in Department.query.all()]

    @staticmethod
    def create_department(name: str) -> dict:
        """
        Create and returns department with given name
        :type name: str
        :rtype: dict
        """
        department = Department.query.filter_by(name=name).first()
        if department is not None:
            raise ValueError("Department with this name already exists")
        department = Department(name=name)
        db.session.add(department)
        db.session.commit()
        return department.as_dict()

    @staticmethod
    def delete_department(department_id: int) -> dict:
        """
        Deletes department by given id
        Returns deleted department
        :type department_id: int
        :rtype: dict
        """
        department = Department.query.filter_by(id=department_id).first()
        if department is None:
            raise ValueError(f"Department with id: {department_id} doesn't exist")
        db.session.delete(department)
        db.session.commit()
        return department.as_dict()

    @staticmethod
    def get_employees(department_id: int) -> list:
        """
        Returns list of employees of department with given id
        :type department_id: int
        :rtype: list
        """
        department = Department.query.filter_by(id=department_id).first()
        if department is None:
            raise ValueError(f"Department with id: {department_id} doesn't exist")
        return [employee.as_dict() for employee in department.employees]

    @staticmethod
    def update_department(department_id: int, department_name: str) -> dict:
        """
        Updates department with given id
        Returns updated department
        :type department_id: int
        :type department_name: str
        :rtype: dict
        """
        department = Department.query.filter_by(name=department_name).first()
        if department is not None:
            raise ValueError(f"Department with name: '{department_name}' already exists")
        department = Department.query.filter_by(id=department_id).first()
        if department is None:
            raise ValueError(f"Department with id: {department_id} doesn't exist")
        department.name = department_name
        db.session.add(department)
        db.session.commit()
        return department.as_dict()
