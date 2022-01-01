"""

"""
from flask import Blueprint, render_template, request, abort, flash, redirect
from ..service.department_service import DepartmentService

department_bp = Blueprint("departments", __name__, url_prefix="/department")


@department_bp.route("/", methods=["GET"])
def all_departments():
    departments = DepartmentService.get_all_departments()
    return render_template("all_departments.html", departments=departments)


@department_bp.route("/", methods=["POST"])
def create_department():
    if not request.form:
        abort(404)
    department_name = request.form.get("department_name")
    try:
        DepartmentService.create_department(department_name)
        flash("New department is created")
    except ValueError as exc:
        flash(str(exc))
    finally:
        return redirect("/department")


@department_bp.route("/<id_>", methods=["GET"])
def department_view(id_: int):
    try:
        dep = DepartmentService.get_department(id_)
        return render_template("department.html", department=dep)
    except Exception as exc:
        print(exc)
        return redirect("/department")


@department_bp.route("/<id_>/delete", methods=["GET"])
def delete_department(id_: int):
    try:
        DepartmentService.delete_department(id_)
    except ValueError as exc:
        flash(str(exc))
    finally:
        return redirect("/department")
