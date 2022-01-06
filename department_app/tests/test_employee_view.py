"""
This module contains testcase class for employee view
"""
# pylint: disable=invalid-name
# pylint: disable=line-too-long
from .conftest import BaseCase


class EmployeeViewTest(BaseCase):
    """
    This is test case for employee views
    """
    def test_get_all(self):
        """
        Tests whether view returns correct data
        """
        rv = self.client.get('/employee', follow_redirects=True)
        assert b"Test3 Test" in rv.data

    def test_filter_no_form(self):
        """
        Check for correct response when form is not provided
        """
        rv = self.client.post('/employee', follow_redirects=True)
        self.assertEqual(rv.status_code, 404)

    def test_filter_wrong_values(self):
        """
        Check for correct response when bad data is provided
        """
        rv = self.client.post('/employee', data=dict(bla="blahblah"), follow_redirects=True)
        assert b"Setting lower bound is necessary" in rv.data

    def test_filter_wrong_date(self):
        """
        Check for correct response when bad data is provided
        """
        rv = self.client.post('/employee', data=dict(todate="2020-12-12", fromdate="2021-12-12"), follow_redirects=True)
        assert b"Upper bound should be higher than lower" in rv.data

    def test_filter_with_one_date(self):
        """
        Tests whether view returns correct data when one date is provided
        """
        rv = self.client.post('/employee', data=dict(fromdate="2021-12-12"), follow_redirects=True)
        assert b"Employees who were born on 2021-12-12" in rv.data

    def test_filter(self):
        """
        Tests whether view returns correct data when both dates are provided
        """
        rv = self.client.post('/employee', data=dict(fromdate="2020-12-12", todate="2021-12-12"), follow_redirects=True)
        assert b"Employees who born between 2020-12-12 and 2021-12-12" in rv.data

    def test_delete_wrong_id(self):
        """
        Check for correct response when wrong id is provided
        """
        rv = self.client.get('/employee/50/delete', follow_redirects=True)
        assert b"Employee with id: 50 doesn&#39;t exist" in rv.data

    def test_delete(self):
        """
        Tests ability to delete employee through view
        """
        rv = self.client.get('/employee/2/delete', follow_redirects=True)
        assert b"Employee with id: 2 deleted" in rv.data

    def test_get_with_wrong_id(self):
        """
        Check for correct response when wrong id is provided
        """
        rv = self.client.get('/employee/50', follow_redirects=True)
        assert b"Employee with id: 50 doesn&#39;t exist" in rv.data

    def test_get(self):
        """
        Tests whether view returns correct data for provided id
        """
        rv = self.client.get('/employee/5', follow_redirects=True)
        assert b"TestView" in rv.data

    def test_update_no_form(self):
        """
        Check for correct response when form is not provided
        """
        rv = self.client.post('/employee/5', follow_redirects=True)
        self.assertEqual(404, rv.status_code)

    def test_update_wrong_salary_value(self):
        """
        Check for correct response when bad salary value is provided
        """
        rv = self.client.post('/employee/5', data=dict(fist_name="testupdate",
                                                       last_name="testupdate",
                                                       department=2,
                                                       birthdate="2020-10-10",
                                                       salary=-50), follow_redirects=True)
        assert b"Salary can&#39;t be lower than 0" in rv.data

    def test_update_wrong_department(self):
        """
        Check for correct response when bad department id is provided
        """
        rv = self.client.post('/employee/5', data=dict(fist_name="testupdate",
                                                       last_name="testupdate",
                                                       department=20,
                                                       birthdate="2020-10-10",
                                                       salary=50), follow_redirects=True)
        assert b"Department with id: 20 doesn&#39;t exist" in rv.data

    def test_update(self):
        """
        Tests ability to update employee through view
        """
        rv = self.client.post('/employee/5', data=dict(fist_name="testupdate",
                                                       last_name="testupdate",
                                                       department=3,
                                                       birthdate="2020-10-10",
                                                       salary=50), follow_redirects=True)
        assert b"Employee is updated" in rv.data
        assert b"Test3" in rv.data

    def test_get_create(self):
        """
        Tests whether correct page is returned
        """
        rv = self.client.get("/employee/create", follow_redirects=True)
        self.assertEqual(rv.request.path, "/employee/create")

    def test_create_no_form(self):
        """
        Check for correct response when form is not provided
        """
        rv = self.client.post("/employee/create")
        self.assertEqual(404, rv.status_code)

    def test_create(self):
        """
        Tests ability to create employee through view
        """
        rv = self.client.post("/employee/create", content_type='multipart/form-data',
                              data=dict(first_name="testcreate",
                                        last_name="testcreate",
                                        department=1,
                                        birthdate="2020-10-10",
                                        salary=50.6), follow_redirects=True)
        assert b"Created" in rv.data
        self.assertEqual("/employee/6", rv.request.path)

    def test_create_wrong_salary(self):
        """
        Check for correct response when bad salary value is provided
        """
        rv = self.client.post("/employee/create", content_type='multipart/form-data',
                              data=dict(first_name="testcreate",
                                        last_name="testcreate",
                                        department=1,
                                        birthdate="2020-10-10",
                                        salary=-50.6), follow_redirects=True)
        assert b"Salary can&#39;t be lower than 0" in rv.data
        self.assertEqual("/employee/create", rv.request.path)

    def test_create_wrong_department(self):
        """
        Check for correct response when bad department id is provided
        """
        rv = self.client.post("/employee/create", content_type='multipart/form-data',
                              data=dict(first_name="testcreate",
                                        last_name="testcreate",
                                        department=20,
                                        birthdate="2020-10-10",
                                        salary=50.6), follow_redirects=True)
        assert b"Department with id: 20 doesn&#39;t exist" in rv.data
        self.assertEqual("/employee/create", rv.request.path)
