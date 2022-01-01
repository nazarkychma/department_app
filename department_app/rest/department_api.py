"""

"""
# pylint: disable=no-self-use

from flask_restful import Resource
from flask import request, make_response, jsonify
from ..service.department_service import DepartmentService


class DepartmentsApi(Resource):
    def get(self):
        try:
            departments_list = DepartmentService.get_all_departments()
            return make_response(jsonify(departments_list), 200)
        except Exception as exc:
            return make_response({"message": str(exc)}, 404)

    def post(self):
        try:
            if not request.json["name"]:
                return make_response({"message": "Missing arguments"}, 422)
            department = DepartmentService.create_department(request.json["name"])
            return make_response({"id": department['id']}, 201)
        except Exception as exc:
            return make_response({"message": str(exc)}, 404)


class DepartmentApi(Resource):
    def get(self, id_: int):
        try:
            department = DepartmentService.get_department(id_)
            return make_response(department, 200)
        except Exception as exc:
            return make_response({"message": str(exc)}, 404)

    def patch(self, id_: int):
        try:
            if not request.json["name"]:
                return make_response({"message": "Missing arguments"}, 422)
            department = DepartmentService.update_department(id_, request.json["name"])
            return make_response({"Updated": department}, 200)
        except Exception as exc:
            return make_response({"message": str(exc)}, 404)

    def delete(self, id_: int):
        try:
            department = DepartmentService.delete_department(id_)
            return make_response({"Deleted": department}, 200)
        except Exception as exc:
            return make_response({"message": str(exc)}, 404)
