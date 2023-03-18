#!/usr/bin/python3
"""test for console to make it start working"""
import unittest
from io import StringIO
from console import HBNBCommand
import sys
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models.engine.file_storage import FileStorage
from models.engine.db_storage import DBStorage

class TestConsole(unittest.TestCase):
    def setUp(self):
        self.cli = HBNBCommand()

    def test_do_create_with_params(self):
        # create a class with parameters
        self.cli.onecmd('create User name="Alice" age=25 height=1.75')
        alice_id = self.cli.last_output.split()[-1]

        # verify that the instance was created correctly
        alice = self.cli.instances[alice_id]
        self.assertEqual(alice.name, "Alice")
        self.assertEqual(alice.age, 25)
        self.assertEqual(alice.height, 1.75)

        # create another class with parameters
        self.cli.onecmd('create Car brand="Tesla" model="Model S" year=2022')
        tesla_id = self.cli.last_output.split()[-1]

        # verify that the instance was created correctly
        tesla = self.cli.instances[tesla_id]
        self.assertEqual(tesla.brand, "Tesla")
        self.assertEqual(tesla.model, "Model S")
        self.assertEqual(tesla.year, 2022)

    def test_do_create_with_invalid_params(self):
        # create a class with invalid parameters
        self.cli.onecmd('create User name=Alice age=twenty-five height=1.75')
        self.assertIn("User instance created with id", self.cli.last_output)

        # verify that the instance was created with only valid parameters
        alice_id = self.cli.last_output.split()[-1]
        alice = self.cli.instances[alice_id]
        self.assertEqual(alice.name, "Alice")
        self.assertEqual(alice.age, 0)  # default value for invalid parameter
        self.assertEqual(alice.height, 1.75)

        # create a class with missing value
        self.cli.onecmd('create Car brand="Tesla" model=')
        self.assertIn("create: missing value", self.cli.last_output)

        # create a class with invalid value
        self.cli.onecmd('create Car brand=Tesla model="Model S" year=2022.5')
        self.assertIn("Car instance created with id", self.cli.last_output)

        # verify that the instance was created with only valid parameters
        tesla_id = self.cli.last_output.split()[-1]
        tesla = self.cli.instances[tesla_id]
        self.assertEqual(tesla.brand, "Tesla")
        self.assertIsNone(tesla.model)  # default value for missing value parameter
        self.assertEqual(tesla.year, 2022)  # integer conversion of valid parameter value
