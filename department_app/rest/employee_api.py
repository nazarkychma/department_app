"""

"""
# pylint: disable=no-self-use
from datetime import datetime
from flask_restful import Resource
from flask import jsonify, make_response, request
from ..service.employee_service import EmployeeService


class EmployeesApi(Resource):
    def get(self):
        try:
            employee_list = EmployeeService.get_all_employees()
            return make_response(jsonify(employee_list), 200)
        except Exception as exc:
            return make_response({"message": str(exc)}, 404)

    def post(self):
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
    def get(self, id_: int):
        try:
            return jsonify(EmployeeService.get_employee_by_id(id_))
        except ValueError as exc:
            return {"message": str(exc)}, 404

    def delete(self, id_: int):
        try:
            employee = EmployeeService.delete_employee(id_)
            return make_response({"Deleted": employee}, 200)
        except Exception as exc:
            return make_response({"message": str(exc)}, 404)

    def patch(self, id_: int):
        try:
            update_values = dict(request.json)
            employee = EmployeeService.update_employee(id_, update_values)
            return make_response({"Updated": employee}, 200)
        except Exception as exc:
            return make_response({"message": str(exc)}, 404)


class EmployeesFilter(Resource):
    def get(self):
        try:
            print(request.args)
            if not request.args.get("from_date"):
                return make_response({"message": "Setting lower bound is necessary"}, 422)
            if not request.args.get("to_date"):
                result = EmployeeService.get_employees_by_birthdate(datetime.strptime(request.args["fromdate"], "%Y-%m-%d"))
            else:
                result = EmployeeService.get_employees_by_birthdate(
                    datetime.strptime(request.args["from_date"], "%Y-%m-%d"),
                    datetime.strptime(request.args["to_date"], "%Y-%m-%d"))
            return make_response(jsonify(result), 200)
        except Exception as exc:
            return make_response({"message": str(exc)}, 404)

