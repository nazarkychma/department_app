"""
This module contains base class to inherit in others test classes
"""
import unittest
from department_app import create_app, TestConfig, db
from department_app.helpers.populate_db import seed_data


class BaseCase(unittest.TestCase):
    """
    This is test case to inherit
    Creates environment to test
    """
    def setUp(self) -> None:
        """
        Called before each test
        Setting up all needed for testing
        """
        self.app = create_app(TestConfig)
        self.app.app_context().push()
        self.client = self.app.test_client()
        db.init_app(self.app)
        db.create_all()
        seed_data()

    def tearDown(self) -> None:
        """
        Called after each test
        Closing db session and drops all the data
        """
        db.session.remove()
        db.drop_all()
