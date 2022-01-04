"""
This module contains classes which provides an API for Employee
Classes:
    - EmployeesApi
    - EmployeeApi
    - EmployeesFilter
"""
# pylint: disable=no-self-use
# pylint: disable=broad-except
from datetime import datetime
from flask_restful import Resource
from flask import jsonify, make_response, request
from ..service.employee_service import EmployeeService


class EmployeesApi(Resource):
    """
    Class provides API for all employee
    Handles POST and GET requests
    Available at /api/employee
    """
    def get(self):
        """
        Called during GET request
        Returns json, which includes all employees or error message
        """
        try:
            employee_list = EmployeeService.get_all_employees()
            return make_response(jsonify(employee_list), 200)
        except Exception as exc:
            return make_response({"message": str(exc)}, 404)

    def post(self):
        """
        Called during POST request
        Creates new employee with values given in request body
        Returns created employee in json format
        """
        try:
            employee = EmployeeService.create_employee(
                first_name=request.json["first_name"],
                last_name=request.json["last_name"],
                salary=request.json["salary"],
                birthdate=datetime.strptime(request.json["birthdate"], "%Y-%m-%d"),
                department_id=request.json["department_id"]
            )
            return make_response(employee, 201)
        except KeyError:
            return make_response({"message": "Missing arguments"}, 422)
        except Exception as exc:
            return make_response({"message": str(exc)}, 400)


class EmployeeApi(Resource):
    """
    Class provides API for selected employee
    Handles PATH, DELETE and GET requests
    Available at /api/employee/<id_>
    """
    def get(self, id_: int):
        """
        Called during GET request
        Returns employee with given id in json format
        """
        try:
            return jsonify(EmployeeService.get_employee_by_id(id_))
        except ValueError as exc:
            return {"message": str(exc)}, 404

    def delete(self, id_: int):
        """
        Called during DELETE request
        Deletes employee with given id
        Returns deleted employee in json format
        """
        try:
            employee = EmployeeService.delete_employee(id_)
            return make_response({"Deleted": employee}, 200)
        except Exception as exc:
            return make_response({"message": str(exc)}, 404)

    def patch(self, id_: int):
        """
        Called during PATCH request
        Updates employee with given id with values provided in request body
        Returns updated employee in json format
        """
        try:
            update_values = dict(request.json)
            employee = EmployeeService.update_employee(id_, update_values)
            return make_response({"Updated": employee}, 200)
        except Exception as exc:
            return make_response({"message": str(exc)}, 404)


# pylint: disable=line-too-long
class EmployeesFilter(Resource):
    """
    Class provides API for filtering employee
    Handles GET requests
    Available at /api/employee/filter
    """
    def get(self):
        """
        Called during GET request
        Returns all employees, who satisfies filter criteria in json format
        """
        try:
            print(request.args)
            if not request.args.get("from_date"):
                return make_response({"message": "Setting lower bound is necessary"}, 422)
            if not request.args.get("to_date"):
                res = EmployeeService.get_employees_by_birthdate(datetime.strptime(request.args["fromdate"], "%Y-%m-%d"))
            else:
                res = EmployeeService.get_employees_by_birthdate(
                    datetime.strptime(request.args["from_date"], "%Y-%m-%d"),
                    datetime.strptime(request.args["to_date"], "%Y-%m-%d"))
            return make_response(jsonify(res), 200)
        except Exception as exc:
            return make_response({"message": str(exc)}, 404)
