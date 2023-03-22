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
class HBNBCommand(cmd.Cmd):
    """This class defines the command line interpreter"""

    prompt = "(hbnb) "

    def emptyline(self):
        """Do nothing when emptyline is entered"""
        pass

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def do_create(self, arg):
        """
        Create a new instance of a class

        Usage: create <class_name>
 
        """
        temp_out = StringIO()
        sys.stdout = temp_out

        HBNBCommand().do_create(None)
        self.assertEqual(temp_out.getvalue(), '** class name missing **\n')
        temp_out.close()

        temp_out = StringIO()
        sys.stdout = temp_out
        HBNBCommand().do_create("base")
        self.assertEqual(temp_out.getvalue(), '** class doesn\'t exist **\n')
        temp_out.close()

        temp_out = StringIO()
        sys.stdout = temp_out
        HBNBCommand().do_create("BaseModel")
        self.assertEqual(temp_out.getvalue(), '** class doesn\'t exist **\n')
        temp_out.close()
        sys.stdout = sys.__stdout__

if __name__ == "__main__":
    unittest.main()
