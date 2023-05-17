"""
This module contains testcase class for department view
"""
# pylint: disable=invalid-name
from .conftest import BaseCase


class DepartmentViewTest(BaseCase):
    """
    This is test case for employee views
    """
    def test_get_all(self):
        """
        Tests whether view returns correct data
        """
        rv = self.client.get('/department', follow_redirects=True)
        assert b"Test10" not in rv.data
        assert b"Test1" in rv.data

    def test_get_wrong_id(self):
        """
        Check for correct response when wrong id is provided
        """
        rv = self.client.get('/department/20', follow_redirects=True)
        self.assertEqual("/department/", rv.request.path)

    def test_get_department(self):
        """
        Tests whether view returns correct data for provided id
        """
        rv = self.client.get('/department/2', follow_redirects=True)
        self.assertEqual("/department/2", rv.request.path)
        assert b"2017-11-06" in rv.data

    def test_create_wrong_name(self):
        """
        Check for correct response when bad department name is provided
        """
        rv = self.client.post('/department', content_type='multipart/form-data',
                              data=dict(department_name="Test1"), follow_redirects=True)
        assert b"Department with this name already exists" in rv.data

    def test_create_wrong_form(self):
        """
        Check for correct response when inappropriate value is provided
        """
        rv = self.client.post('/department', content_type='multipart/form-data',
                              data=dict(name="Test1"), follow_redirects=True)
        self.assertEqual(rv.status_code, 404)

    def test_create(self):
        """
        Tests ability to create department through view
        """
        rv = self.client.post('/department', content_type='multipart/form-data',
                              data=dict(department_name="Test11"), follow_redirects=True)
        assert b"New department is created" in rv.data
        assert b"Test11" in rv.data

    def test_update_wrong_name(self):
        """
        Check for correct response when bad department name is provided
        """
        rv = self.client.post('/department/2', content_type='multipart/form-data',
                              data=dict(department_name="Test1"), follow_redirects=True)
        assert b"Department with name: &#39;Test1&#39; already exists" in rv.data

    def test_update_wrong_form(self):
        """
        Check for correct response when inappropriate value is provided
        """
        rv = self.client.post('/department/2', content_type='multipart/form-data',
                              data=dict(name="Test1"), follow_redirects=True)
        self.assertEqual(rv.status_code, 404)

    def test_update(self):
        """
        Tests ability to update department through view
        """
        rv = self.client.post('/department/2', content_type='multipart/form-data',
                              data=dict(department_name="Test11"), follow_redirects=True)
        assert b"Department is updated" in rv.data
        assert b"Test11" in rv.data

    def test_delete_wrong_id(self):
        """
        Check for correct response when wrong id is provided
        """
        rv = self.client.get('/department/50/delete', follow_redirects=True)
        assert b"Department with id: 50 doesn&#39;t exist" in rv.data

    def test_delete(self):
        """
        Tests ability to delete department through view
        """
        rv = self.client.get('/department/2/delete', follow_redirects=True)
        assert b"Department with id: 2 deleted" in rv.data
