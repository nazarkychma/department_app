"""
This module contains testcase class for department service
"""
from base import BaseCase
from department_app.service.department_service import DepartmentService
from department_app.models.deparment import Department


class DepartmentTest(BaseCase):
    def test_get_with_wrong_id(self):
        with self.assertRaises(ValueError) as exc:
            DepartmentService.get_department(5)
        assert str(exc.exception) == "Department with id: 5 doesn't exist"

    def test_create_with_wrong_name(self):
        with self.assertRaises(ValueError) as exc:
            DepartmentService.create_department("Test1")
        assert str(exc.exception) == "Department with this name already exists"

    def test_delete_with_wrong_id(self):
        with self.assertRaises(ValueError) as exc:
            DepartmentService.delete_department(5)
        assert str(exc.exception) == "Department with id: 5 doesn't exist"

    def test_get_employees_with_wrong_id(self):
        with self.assertRaises(ValueError) as exc:
            DepartmentService.get_employees(5)
        assert str(exc.exception) == "Department with id: 5 doesn't exist"

    def test_update_with_wrong_id(self):
        with self.assertRaises(ValueError) as exc:
            DepartmentService.delete_department(5)
        assert str(exc.exception) == "Department with id: 5 doesn't exist"

    def test_update_with_wrong_name(self):
        with self.assertRaises(ValueError) as exc:
            DepartmentService.update_department(1, "Test4")
        assert str(exc.exception) == "Department with name: 'Test4' already exists"

    def test_get_department(self):
        query_result = Department.query.filter_by(id=1).first().as_dict()
        self.assertEqual(DepartmentService.get_department(1), query_result)

    def test_get_all(self):
        self.assertEqual(4, len(DepartmentService.get_all_departments()))

    def test_create(self):
        new_dep = DepartmentService.create_department("Test5")
        all_deps = DepartmentService.get_all_departments()
        self.assertIn(new_dep, all_deps)

    def test_delete(self):
        self.assertEqual({"Deleted": True}, DepartmentService.delete_department(1))

    def test_get_employees(self):
        employees = DepartmentService.get_department(2)["employees"]
        self.assertListEqual(employees, DepartmentService.get_employees(2))

    def test_update(self):
        new_name = "UpdateTest"
        DepartmentService.update_department(2, new_name)
        self.assertEqual(new_name, DepartmentService.get_department(2)["name"])