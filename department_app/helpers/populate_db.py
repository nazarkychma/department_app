# pylint: skip-file
import datetime

from ..models.deparment import Department
from ..models.employee import Employee
from .. import db


def seed_data():
    dep1 = Department(id=1, name="Test1")
    dep2 = Department(id=2, name="Test2")
    dep3 = Department(id=3, name="Test3")
    dep4 = Department(id=4, name="Test4")

    db.session.add(dep1)
    db.session.add(dep2)
    db.session.add(dep3)
    db.session.add(dep4)

    emp1 = Employee(id=1, first_name="Test", last_name="Test", salary=100, department_id=1)
    emp2 = Employee(id=2, first_name="Test", last_name="Test", salary=100, birthdate=datetime.date(2017, 11, 6), department_id=2)
    emp3 = Employee(id=3, first_name="Test", last_name="Test", salary=100, birthdate=datetime.date(2002, 11, 6), department_id=3)
    emp4 = Employee(id=4, first_name="Test", last_name="Test", salary=100, birthdate=datetime.date(2005, 11, 6),department_id=4)
    emp5 = Employee(id=5, first_name="Test", last_name="Test", salary=100, department_id=1)

    db.session.add(emp1)
    db.session.add(emp2)
    db.session.add(emp3)
    db.session.add(emp4)
    db.session.add(emp4)
    db.session.add(emp5)
    db.session.commit()
