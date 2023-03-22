import unittest
from io import StringIO
import sys
from unittest.mock import patch
from console import HBNBCommand
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class TestConsole(unittest.TestCase):
    """This class contains test cases for the console"""

    def setUp(self):
        """Redirect stdout to a temporary buffer to check output"""
        self.temp_out = StringIO()
        sys.stdout = self.temp_out

    def tearDown(self):
        """Reset stdout to its original value"""
        sys.stdout = sys.__stdout__

    def test_prompt(self):
        """Test the prompt of the console"""
        self.assertEqual("(hbnb) ", HBNBCommand().prompt)

if __name__ == "__main__":
    unittest.main()
