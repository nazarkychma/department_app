"""
This module contains classes which provides an API for Department
Classes:
    - DepartmentsApi
    - DepartmentApi
"""
# pylint: disable=no-self-use
# pylint: disable=broad-except
from flask_restful import Resource
from flask import request, make_response, jsonify
from ..service.department_service import DepartmentService


class DepartmentsApi(Resource):
    """
    Class provides API for all departments
    Handles POST and GET requests
    Available at /api/department
    """
    def get(self):
        """
        Called during GET request
        Response with json, which includes all departments or error message
        """
        try:
            departments_list = DepartmentService.get_all_departments()
            return make_response(jsonify({"departments": departments_list}), 200)
        except Exception as exc:
            return make_response({"message": str(exc)}, 404)

    def post(self):
        """
        Called during POST request
        Creates new department with values given in request body
        Returns created department in json
        """
        try:
            if not request.json or request.json.get("name") is None:
                return make_response({"message": "Missing arguments"}, 422)
            department = DepartmentService.create_department(request.json.get("name"))
            return make_response({"id": department['id']}, 201)
        except Exception as exc:
            return make_response({"message": str(exc)}, 404)


class DepartmentApi(Resource):
    """
    Class provides API for selected department
    Handles PATH, DELETE and GET requests
    Available at /api/department/<id_>
    """
    def get(self, id_: int):
        """
        Called during GET request
        Returns department with given id in json format
        """
        try:
            department = DepartmentService.get_department(id_)
            return make_response(department, 200)
        except Exception as exc:
            return make_response({"message": str(exc)}, 404)

    def patch(self, id_: int):
        """
        Called during PATCH request
        Updates department with given id with values provided in request body
        Returns updated employee in json format
        """
        try:
            if not request.json or request.json.get("name") is None:
                return make_response({"message": "Missing arguments"}, 422)
            department = DepartmentService.update_department(id_, request.json["name"])
            return make_response({"Updated": department}, 200)
        except Exception as exc:
            return make_response({"message": str(exc)}, 404)

    def delete(self, id_: int):
        """
        Called during DELETE request
        Deletes department with given id
        Returns deleted departments in json format
        """
        try:
            result = DepartmentService.delete_department(id_)
            return make_response(result, 200)
        except Exception as exc:
            return make_response({"message": str(exc)}, 404)
