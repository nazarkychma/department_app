"""
This module contains class which implements CRUD operations for Department

Classes:
    DepartmentService
"""
# pylint: disable=no-member
# pylint: disable=relative-beyond-top-level
from department_app import db
from ..log import logger
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
            logger.error("User is trying to get department, which doesn't exist")
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
        if Department.query.filter_by(name=name).first() is not None:
            logger.error("User is trying to create department with invalid name")
            raise ValueError("Department with this name already exists")
        department = Department(name=name)
        db.session.add(department)
        db.session.commit()
        logger.info("New department with name %s was created", name)
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
            logger.error("User is trying to delete department, which doesn't exist")
            raise ValueError(f"Department with id: {department_id} doesn't exist")
        db.session.delete(department)
        db.session.commit()
        logger.info("Department with id %d was deleted", department_id)
        return {"Deleted": True}

    @staticmethod
    def get_employees(department_id: int) -> list:
        """
        Returns list of employees of department with given id
        :type department_id: int
        :rtype: list
        """
        department = Department.query.filter_by(id=department_id).first()
        if department is None:
            logger.error("User is trying to get employees of department, which doesn't exist")
            raise ValueError(f"Department with id: {department_id} doesn't exist")
        return [employee.as_dict() for employee in department.employees]

    # pylint: disable=line-too-long
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
            logger.error("User is trying to update department with invalid name")
            raise ValueError(f"Department with name: '{department_name}' already exists")
        department = Department.query.filter_by(id=department_id).first()
        if department is None:
            logger.error("User is trying to update department, which doesn't exist")
            raise ValueError(f"Department with id: {department_id} doesn't exist")
        department.name = department_name
        db.session.add(department)
        db.session.commit()
        logger.info("Department with id %d was updated with new name: {department_name}", department.id)
        return department.as_dict()
