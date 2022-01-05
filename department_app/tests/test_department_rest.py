"""
This module contains testcase class for department REST
"""
import json
from .conftest import BaseCase
from ..service.department_service import DepartmentService


class DepartmentRESTTest(BaseCase):
    def setUp(self) -> None:
        super().setUp()
        self.client = self.app.test_client()

    def test_get_all(self):
        response = self.client.get('/api/department')
        self.assertEqual(200, response.status_code)
        self.assertIsNotNone(response.json.get("departments"))

    def test_create_with_no_name(self):
        response = self.client.post("/api/department")
        self.assertEqual(422, response.status_code)
        self.assertEqual("Missing arguments", response.json.get("message"))

    def test_create_with_wrong_name(self):
        response = self.client.post("/api/department", data=json.dumps(dict(name="Test1")), content_type='application/json')
        self.assertEqual(404, response.status_code)
        self.assertEqual("Department with this name already exists", response.json.get("message"))

    def test_create(self):
        response = self.client.post("/api/department", data=json.dumps(dict(name="TestCreate")), content_type='application/json')
        self.assertEqual(201, response.status_code)
        self.assertEqual(5, response.json.get("id"))

    def test_get_with_wrong_id(self):
        response = self.client.get("/api/department/100")
        self.assertEqual(404, response.status_code)
        self.assertEqual("Department with id: 100 doesn't exist", response.json.get("message"))

    def test_get_department(self):
        response = self.client.get("/api/department/1")
        self.assertEqual(200, response.status_code)
        self.assertEqual("Test1", response.json["name"])

    def test_delete_with_wrong_id(self):
        response = self.client.delete("/api/department/100")
        self.assertEqual(404, response.status_code)
        self.assertEqual("Department with id: 100 doesn't exist", response.json.get("message"))

    def test_delete(self):
        response = self.client.delete("/api/department/1")
        self.assertEqual(200, response.status_code)
        self.assertTrue(response.json["Deleted"])

    def test_update_with_no_arguments(self):
        response = self.client.patch("/api/department/1")
        self.assertEqual(422, response.status_code)
        self.assertEqual("Missing arguments", response.json.get("message"))

    def test_update_with_wrong_name(self):
        response = self.client.patch("/api/department/1", data=json.dumps(dict(name="Test1")), content_type='application/json')
        self.assertEqual(404, response.status_code)
        self.assertEqual("Department with name: 'Test1' already exists", response.json.get("message"))

    def test_update(self):
        response = self.client.patch("/api/department/1", data=json.dumps(dict(name="TestUpdate")), content_type='application/json')
        self.assertEqual(200, response.status_code)
        self.assertEqual(1, response.json.get("Updated").get("id"))
        self.assertEqual(DepartmentService.get_department(1).get("name"), response.json.get("Updated").get("name"))