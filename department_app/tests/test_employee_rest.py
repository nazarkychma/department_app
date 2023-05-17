"""
This module contains testcase class for employee REST
"""
# pylint: disable=line-too-long
import json
from .conftest import BaseCase
from ..service.employee_service import EmployeeService


class EmployeeRESTTest(BaseCase):
    """
    This is test case for employee REST
    """
    def setUp(self) -> None:
        """
        Called before each test
        Setting up environment for tests
        """
        super().setUp()
        self.employee_values = dict(first_name="testcreate",
                                    last_name="testcreate",
                                    department_id=1,
                                    birthdate="2020-10-10",
                                    salary=50.6)

    def test_get_all(self):
        """
        Tests ability to get all employee using rest
        """
        response = self.client.get('/api/employee')
        self.assertEqual(200, response.status_code)
        self.assertIsNotNone(response.json.get("employees"))

    def test_create_with_no_data(self):
        """
        Check for correct response when request body is not provided
        """
        response = self.client.post("/api/employee")
        self.assertEqual(422, response.status_code)
        self.assertEqual("Missing arguments", response.json.get("message"))

    def test_create_with_missing_name(self):
        """
        Check for correct response when request body misses some values
        """
        response = self.client.post("/api/employee", data=json.dumps(dict(first_name="Test")))
        self.assertEqual(422, response.status_code)
        self.assertEqual("Missing arguments", response.json.get("message"))

    def test_create_with_invalid_salary(self):
        """
        Check for correct response when wrong salary value is provided
        """
        update_values = self.employee_values
        update_values["salary"] = -5
        response = self.client.post("/api/employee", data=json.dumps(update_values), content_type='application/json')
        self.assertEqual(404, response.status_code)
        self.assertEqual("Salary can't be lower than 0", response.json.get("message"))

    def test_create_with_invalid_department(self):
        """
        Check for correct response when wrong department id is provided
        """
        update_values = self.employee_values
        update_values["department_id"] = 20
        response = self.client.post("/api/employee", data=json.dumps(update_values), content_type='application/json')
        self.assertEqual(404, response.status_code)
        self.assertEqual("Department with id: 20 doesn't exist", response.json.get("message"))

    def test_create(self):
        """
        Tests ability to create employee using REST
        """
        response = self.client.post("/api/employee", data=json.dumps(self.employee_values), content_type='application/json')
        self.assertEqual(201, response.status_code)
        self.assertEqual(6, response.json.get("id"))

    def test_filter_no_form(self):
        """
        Check for correct response when inappropriate values are provided
        """
        response = self.client.get('/api/employee/filter', query_string=dict(blah="blah"))
        self.assertEqual(422, response.status_code)
        self.assertEqual("Setting lower bound is necessary", response.json.get("message"))

    def test_filter_wrong_date(self):
        """
        Check for correct response when wrong dates are provided
        """
        response = self.client.get('/api/employee/filter', query_string=dict(to_date="2020-12-12", from_date="2021-12-12"))
        self.assertEqual(404, response.status_code)
        self.assertEqual("Upper bound should be higher than lower", response.json.get("message"))

    def test_filter_with_one_date(self):
        """
        Tests ability to get employees who born on provided date using rest
        """
        response = self.client.get('/api/employee/filter', query_string=dict(from_date="2017-11-06"))
        self.assertEqual(200, response.status_code)
        self.assertIsNotNone(response.json.get("employees"))

    def test_filter(self):
        """
        Tests ability to get employees who born between provided dates using rest
        """
        response = self.client.get('/api/employee/filter', query_string=dict(from_date="2020-12-12", to_date="2021-12-12"))
        self.assertEqual(200, response.status_code)
        self.assertIsNotNone(response.json.get("employees"))

    def test_delete_wrong_id(self):
        """
        Check for correct response when invalid id is provided
        """
        response = self.client.delete('/api/employee/50')
        self.assertEqual(404, response.status_code)
        self.assertEqual("Employee with id: 50 doesn't exist", response.json.get("message"))

    def test_delete(self):
        """
        Tests ability to delete employee using rest
        """
        response = self.client.delete('/api/employee/2')
        self.assertEqual(200, response.status_code)
        self.assertEqual(2, response.json.get("Deleted").get("id"))

    def test_get_with_wrong_id(self):
        """
        Check for correct response when invalid id is provided
        """
        response = self.client.get('/api/employee/50')
        self.assertEqual(404, response.status_code)
        self.assertEqual("Employee with id: 50 doesn't exist", response.json.get("message"))

    def test_get(self):
        """
        Tests ability to get employee using rest
        """
        response = self.client.get('/api/employee/5')
        self.assertEqual(200, response.status_code)
        self.assertEqual(5, response.json.get("id"))

    def test_update_no_form(self):
        """
        Check for correct response when request body is not provided
        """
        response = self.client.patch('/api/employee/5')
        self.assertEqual(404, response.status_code)
        self.assertEqual("Missing values", response.json.get("message"))

    def test_update_wrong_values(self):
        """
        Check for correct response when inappropriate values are provided
        """
        response = self.client.patch('/api/employee/5', data=json.dumps({"blah": "blah"}),
                                     content_type='application/json')
        self.assertEqual(404, response.status_code)
        self.assertEqual("Nothing to update", response.json.get("message"))

    def test_update_wrong_salary_value(self):
        """
        Check for correct response when wrong salary value is provided
        """
        update_values = self.employee_values
        update_values["salary"] = -50
        response = self.client.patch('/api/employee/5', data=json.dumps(update_values), content_type='application/json')
        self.assertEqual(404, response.status_code)
        self.assertEqual("Salary can't be lower than 0", response.json.get("message"))

    def test_update_wrong_department(self):
        """
        Check for correct response when wrong department id is provided
        """
        update_values = self.employee_values
        update_values["department_id"] = 20
        response = self.client.patch('/api/employee/5', data=json.dumps(update_values), content_type='application/json')
        self.assertEqual(404, response.status_code)
        self.assertEqual("Department with id: 20 doesn't exist", response.json.get("message"))

    def test_update(self):
        """
        Tests ability to update employee using rest
        """
        response = self.client.patch('/api/employee/5', data=json.dumps(self.employee_values), content_type='application/json')
        self.assertEqual(200, response.status_code)
        self.assertEqual("testcreate testcreate", EmployeeService.get_employee_by_id(5).get("name"))
