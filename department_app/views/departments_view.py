"""
Module contains Department views
"""
# pylint: disable=relative-beyond-top-level
# pylint: disable=broad-except
from flask import Blueprint, render_template, request, abort, flash, redirect, url_for
from ..service.department_service import DepartmentService

department_bp = Blueprint("departments", __name__, url_prefix="/department")


@department_bp.route("/", methods=["GET"])
def all_departments():
    """
    Show all the departments
    """
    departments = DepartmentService.get_all_departments()
    return render_template("all_departments.html", departments=departments)


@department_bp.route("/", methods=["POST"])
def create_department():
    """
    Creates new department with name provided in form
    :raises 404: if form is not provided
    """
    department_name = request.form.get("department_name")
    if not department_name:
        abort(404)
    try:
        DepartmentService.create_department(department_name)
        flash("New department is created")
        return redirect(url_for("departments.all_departments"))
    except ValueError as exc:
        flash(str(exc))
        return redirect(url_for("departments.all_departments"))


@department_bp.route("/<id_>", methods=["GET"])
def department_view(id_: int):
    """
    Shows department with given id
    """
    try:
        dep = DepartmentService.get_department(id_)
        return render_template("department.html", department=dep)
    except Exception:
        return redirect(url_for("departments.all_departments"))


@department_bp.route("/<id_>/delete", methods=["GET"])
def delete_department(id_: int):
    """
    Deletes department with given id and redirects to all department view
    """
    try:
        DepartmentService.delete_department(id_)
        flash(f"Department with id: {id_} deleted")
        return redirect(url_for("departments.all_departments"))
    except ValueError as exc:
        flash(str(exc))
        return redirect(url_for("departments.all_departments"))
