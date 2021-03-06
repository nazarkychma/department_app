"""
This module contains testcase class for employee service
"""
from datetime import date

from .conftest import BaseCase
from ..service.employee_service import EmployeeService
from ..models.employee import Employee


class EmployeeServiceTest(BaseCase):
    """
    This is test case for employee service
    """
    def test_get_with_wrong_id(self):
        """
        Check whether exception is raised when invalid id is provided
        """
        with self.assertRaises(ValueError) as exc:
            EmployeeService.get_employee_by_id(10)
        assert str(exc.exception) == "Employee with id: 10 doesn't exist"

    def test_delete_with_wrong_id(self):
        """
        Check whether exception is raised when invalid id is provided
        """
        with self.assertRaises(ValueError) as exc:
            EmployeeService.delete_employee(10)
        assert str(exc.exception) == "Employee with id: 10 doesn't exist"

    def test_wrong_filter_criteria(self):
        """
        Check whether exception is raised when invalid perios is provided
        """
        with self.assertRaises(ValueError) as exc:
            EmployeeService.get_employees_by_birthdate(date(2021, 12, 12), date(2020, 12, 12))
        assert str(exc.exception) == "Upper bound should be higher than lower"

    def test_update_with_wrong_id(self):
        """
        Check whether exception is raised when invalid id is provided
        """
        with self.assertRaises(ValueError) as exc:
            EmployeeService.update_employee(10, {"first_name": "Evanko"})
        assert str(exc.exception) == "Employee with id: 10 doesn't exist"

    def test_update_with_wrong_salary_value(self):
        """
        Check whether exception is raised when invalid salary value is provided
        """
        with self.assertRaises(ValueError) as exc:
            EmployeeService.update_employee(1, {"salary": -50})
        assert str(exc.exception) == "Salary can't be lower than 0"

    def test_update_with_wrong_department(self):
        """
        Check whether exception is raised when invalid department id is provided
        """
        with self.assertRaises(ValueError) as exc:
            EmployeeService.update_employee(1, {"department_id": 50})
        assert str(exc.exception) == "Department with id: 50 doesn't exist"

    def test_update_with_wrong_keys(self):
        """
        Check whether exception is raised when inappropriate data is provided
        """
        with self.assertRaises(ValueError) as exc:
            EmployeeService.update_employee(1, {"id": 5, "randomKey": 40})
        assert str(exc.exception) == "Nothing to update"

    def test_get_employee(self):
        """
        Tests ability to get employee by id
        """
        query_result = Employee.query.filter_by(id=1).first().as_dict()
        self.assertEqual(EmployeeService.get_employee_by_id(1), query_result)

    def test_get_all(self):
        """
        Tests ability to get all employees
        """
        self.assertEqual(5, len(EmployeeService.get_all_employees()))

    def test_delete(self):
        """
        Tests ability to delete employee
        """
        employee = Employee.query.filter_by(id=1).first().as_dict()
        self.assertDictEqual(employee, EmployeeService.delete_employee(1))
        self.assertEqual(4, len(EmployeeService.get_all_employees()))

    def test_update(self):
        """
        Tests ability to update employee
        """
        first_name = "UpdateFirst"
        last_name = "UpdateLast"
        birthdate = date(2017, 11, 6)
        EmployeeService.update_employee(2, {"first_name": first_name,
                                            "last_name": last_name,
                                            "birthdate": birthdate})
        result = Employee.query.filter_by(id=2).first().as_dict()
        self.assertEqual(result["name"], "UpdateFirst UpdateLast")
        self.assertEqual(result["birthdate"], birthdate)

    def test_filter(self):
        """
        Tests ability to filter employee using only one date
        """
        result = EmployeeService.get_employees_by_birthdate(date(2017, 11, 6))
        self.assertIn(EmployeeService.get_employee_by_id(2), result)

    def test_filter_period(self):
        """
        Tests ability to filter employee when period is provided
        """
        result = EmployeeService.get_employees_by_birthdate(date(2001, 11, 6), date(2008, 11, 6))
        self.assertEqual(2, len(result))
        self.assertIn(EmployeeService.get_employee_by_id(3), result)
        self.assertIn(EmployeeService.get_employee_by_id(4), result)

    def test_create_wrong_salary(self):
        """
        Check whether exception is raised when invalid salary value is provided
        """
        with self.assertRaises(ValueError) as exc:
            EmployeeService.create_employee(first_name="TestCreate",
                                            last_name="TestCreate",
                                            birthdate=date(2001, 11, 6),
                                            salary=-50.6,
                                            department_id=2)
        assert str(exc.exception) == "Salary can't be lower than 0"

    def test_create_wrong_department(self):
        """
        Check whether exception is raised when invalid department id is provided
        """
        with self.assertRaises(ValueError) as exc:
            EmployeeService.create_employee(first_name="TestCreate",
                                            last_name="TestCreate",
                                            birthdate=date(2001, 11, 6),
                                            salary=50.6,
                                            department_id=100)
        assert str(exc.exception) == "Department with id: 100 doesn't exist"

    def test_create(self):
        """
        Test ability to create new employee
        """
        result = EmployeeService.create_employee(first_name="TestCreate",
                                                 last_name="TestCreate",
                                                 birthdate=date(2001, 11, 6),
                                                 salary=50.6,
                                                 department_id=2)
        self.assertDictEqual(result, Employee.query.filter_by(id=result["id"]).first().as_dict())
