"""
This module contains testcase class for department service
"""
from department_app.models.deparment import Department
from department_app.service.department_service import DepartmentService
from .conftest import BaseCase


class DepartmentServiceTest(BaseCase):
    """
    This is test case for department service
    """
    def test_get_with_wrong_id(self):
        """
        Check whether exception is raised when invalid id is provided
        """
        with self.assertRaises(ValueError) as exc:
            DepartmentService.get_department(5)
        assert str(exc.exception) == "Department with id: 5 doesn't exist"

    def test_create_with_wrong_name(self):
        """
        Check whether exception is raised when invalid name is provided
        """
        with self.assertRaises(ValueError) as exc:
            DepartmentService.create_department("Test1")
        assert str(exc.exception) == "Department with this name already exists"

    def test_delete_with_wrong_id(self):
        """
        Check whether exception is raised when invalid id is provided
        """
        with self.assertRaises(ValueError) as exc:
            DepartmentService.delete_department(5)
        assert str(exc.exception) == "Department with id: 5 doesn't exist"

    def test_get_employee_with_wrong_id(self):
        """
        Check whether exception is raised when invalid id is provided
        """
        with self.assertRaises(ValueError) as exc:
            DepartmentService.get_employees(5)
        assert str(exc.exception) == "Department with id: 5 doesn't exist"

    def test_update_with_wrong_id(self):
        """
        Check whether exception is raised when invalid id is provided
        """
        with self.assertRaises(ValueError) as exc:
            DepartmentService.delete_department(5)
        assert str(exc.exception) == "Department with id: 5 doesn't exist"

    def test_update_with_wrong_name(self):
        """
        Check whether exception is raised when invalid name is provided
        """
        with self.assertRaises(ValueError) as exc:
            DepartmentService.update_department(1, "Test4")
        assert str(exc.exception) == "Department with name: 'Test4' already exists"

    def test_get_department(self):
        """
        Tests ability to get department
        """
        query_result = Department.query.filter_by(id=1).first().as_dict()
        self.assertEqual(DepartmentService.get_department(1), query_result)

    def test_get_all(self):
        """
        Tests ability to get all departments
        """
        self.assertEqual(4, len(DepartmentService.get_all_departments()))

    def test_create(self):
        """
        Tests ability to create department
        """
        new_dep = DepartmentService.create_department("Test5")
        all_deps = DepartmentService.get_all_departments()
        self.assertIn(new_dep, all_deps)

    def test_delete(self):
        """
        Tests ability to delete department
        """
        self.assertEqual({"Deleted": True}, DepartmentService.delete_department(1))

    def test_get_employees(self):
        """
        Tests ability to get employees of department
        """
        employees = DepartmentService.get_department(2)["employees"]
        self.assertListEqual(employees, DepartmentService.get_employees(2))

    def test_update(self):
        """
        Tests ability to update
        """
        new_name = "UpdateTest"
        DepartmentService.update_department(2, new_name)
        self.assertEqual(new_name, DepartmentService.get_department(2)["name"])
