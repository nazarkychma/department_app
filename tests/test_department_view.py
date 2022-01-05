"""
This module contains testcase class for department view
"""
from conftest import BaseCase


class DepartmentViewTest(BaseCase):
    def setUp(self) -> None:
        super().setUp()
        self.client = self.app.test_client()

    def test_get_all(self):
        rv = self.client.get('/department', follow_redirects=True)
        assert b"Test10" not in rv.data
        assert b"Test1" in rv.data

    def test_get_wrong_id(self):
        rv = self.client.get('/department/20', follow_redirects=True)
        self.assertEqual("/department/", rv.request.path)

    def test_get_department(self):
        rv = self.client.get('/department/2', follow_redirects=True)
        self.assertEqual("/department/2", rv.request.path)
        assert b"2017-11-06" in rv.data

    def test_create_wrong_name(self):
        rv = self.client.post('/department', content_type='multipart/form-data',
                              data=dict(department_name="Test1"), follow_redirects=True)
        assert b"Department with this name already exists" in rv.data

    def test_create_wrong_form(self):
        rv = self.client.post('/department', content_type='multipart/form-data',
                              data=dict(name="Test1"), follow_redirects=True)
        self.assertEqual(rv.status_code, 404)

    def test_create(self):
        rv = self.client.post('/department', content_type='multipart/form-data',
                              data=dict(department_name="Test11"), follow_redirects=True)
        assert b"New department is created" in rv.data
        assert b"Test11" in rv.data

    def test_delete_wrong_id(self):
        rv = self.client.get('/department/50/delete', follow_redirects=True)
        assert b"Department with id: 50 doesn&#39;t exist" in rv.data

    def test_delete(self):
        rv = self.client.get('/department/2/delete', follow_redirects=True)
        assert b"Department with id: 2 deleted" in rv.data
