"""
This module contains base class to inherit in others test classes
"""
import unittest
from department_app import create_app, TestConfig, db
from department_app.helpers.populate_db import seed_data


class BaseCase(unittest.TestCase):
    def setUp(self) -> None:
        self.app = create_app(TestConfig)
        self.app.app_context().push()
        db.init_app(self.app)
        db.create_all()
        seed_data()

    def tearDown(self) -> None:
        db.session.remove()
        db.drop_all()
