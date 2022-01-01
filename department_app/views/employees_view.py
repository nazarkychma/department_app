"""

"""
from datetime import datetime
from flask import Blueprint, render_template, request, abort, redirect, flash
from ..service.employee_service import EmployeeService
from ..service.department_service import DepartmentService

employee_bp = Blueprint("employees", __name__, url_prefix="/employee")


@employee_bp.route("/", methods=["GET"])
def all_employees():
    employees_list = EmployeeService.get_all_employees()
    return render_template("all_employees.html", employees=employees_list)


@employee_bp.route("/", methods=["POST"])
def filter_employees():
    if not request.form:
        abort(404)
    if not request.form.get("fromdate"):
        flash("Setting lower bound is necessary")
        return redirect('/employee')
    if not request.form.get("todate"):
        result = EmployeeService.get_employees_by_birthdate(datetime.strptime(request.form["fromdate"], "%Y-%m-%d"))
        filter_title = f"Employees who were born on {request.form['fromdate']}"
    else:
        result = EmployeeService.get_employees_by_birthdate(datetime.strptime(request.form["fromdate"], "%Y-%m-%d"),
                                                            datetime.strptime(request.form["todate"], "%Y-%m-%d"))
        filter_title = f"Employees who born between {request.form['fromdate']} and {request.form['todate']}"
    return render_template("all_employees.html", employees=result, title=filter_title)


@employee_bp.route("/<id_>", methods=["GET"])
def employee_view(id_: int):
    try:
        departments_list = DepartmentService.get_all_departments()
        employee_data = EmployeeService.get_employee_by_id(id_)
        return render_template("edit_employee.html", employee=employee_data, departments=departments_list)
    except Exception as exc:
        flash(str(exc))
        return redirect("/employee")


@employee_bp.route("/<id_>", methods=["POST"])
def employee_edit(id_: int):
    if not request.form:
        abort(404)
    try:
        new_values = dict(request.form)
        new_values["department_id"] = int(new_values["department"])
        new_values["salary"] = float(new_values["salary"])
        new_values["birthdate"] = datetime.strptime(new_values["birthdate"], "%Y-%m-%d")
        EmployeeService.update_employee(id_, new_values)
        flash("Employee is updated")
        return redirect(f"/employee/{id_}")
    except Exception as exc:
        flash(str(exc))
        return redirect("/employee")


@employee_bp.route("/create", methods=["GET"])
def create_employee_get():
    departments_list = DepartmentService.get_all_departments()
    return render_template("create_employee.html", departments=departments_list, create=True)


@employee_bp.route("/create", methods=["POST"])
def create_employee_post():
    if not request.form:
        abort(404)
    try:
        EmployeeService.create_employee(
            first_name=request.form["first_name"],
            last_name=request.form["last_name"],
            department_id=int(request.form["department"]),
            salary=float(request.form['salary']),
            birthdate=datetime.strptime(request.form["birthdate"], "%Y-%m-%d")
        )
        return redirect("/employee")
    except ValueError as exc:
        flash(str(exc))
    finally:
        return redirect("/employee/create")


@employee_bp.route("/<id_>/delete", methods=["GET"])
def employee_delete(id_: int):
    try:
        EmployeeService.delete_employee(id_)
        flash("Employee deleted")
    except Exception as exc:
        flash(str(exc))
    finally:
        return redirect("/employee")
