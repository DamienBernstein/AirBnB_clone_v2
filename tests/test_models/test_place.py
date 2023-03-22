import unittest
from models.place import Place
from models.base_model import BaseModel
from unittest.mock import patch
import os


class TestPlace(unittest.TestCase):
    """
    Test the Place model class
    """

    @classmethod
    def setUpClass(cls):
        """
        Create an instance of the Place class before each test
        """
        cls.place = Place()

    @classmethod
    def tearDownClass(cls):
        """
        Delete the instance of the Place class after each test
        """
        del cls.place

    def test_inheritance(self):
        """
        Test that the Place class inherits from BaseModel
        """
        self.assertIsInstance(self.place, BaseModel)

    def test_attributes(self):
        """
        Test that the Place class has the required attributes
        """
        self.assertTrue(hasattr(self.place, "city_id"))
        self.assertTrue(hasattr(self.place, "user_id"))
        self.assertTrue(hasattr(self.place, "name"))
        self.assertTrue(hasattr(self.place, "description"))
        self.assertTrue(hasattr(self.place, "number_rooms"))
        self.assertTrue(hasattr(self.place, "number_bathrooms"))
        self.assertTrue(hasattr(self.place, "max_guest"))
        self.assertTrue(hasattr(self.place, "price_by_night"))
        self.assertTrue(hasattr(self.place, "latitude"))
        self.assertTrue(hasattr(self.place, "longitude"))
        self.assertTrue(hasattr(self.place, "amenity_ids"))

    def test_place_amenity_relationship(self):
        """
        Test that the Place and Amenity classes have a many-to-many relationship
        """
        self.assertTrue(hasattr(self.place, "amenities"))
        self.assertIsInstance(self.place.amenities, list)

    @unittest.skipIf(os.environ.get("HBNB_TYPE_STORAGE") == "db", "Testing database storage only")
    def test_getter_methods(self):
        """
        Test the getter methods when using file storage
        """
        with patch("models.storage.all") as mock_storage:
            mock_storage.return_value = {
                "Review.1": Review(place_id=self.place.id),
                "Review.2": Review(place_id=self.place.id)
            }
            self.assertIsInstance(self.place.reviews, list)
            self.assertEqual(len(self.place.reviews), 2)

            mock_storage.return_value = {
                "Amenity.1": Amenity(id="1", name="Wifi"),
                "Amenity.2": Amenity(id="2", name="Pool"),
                "Amenity.3": Amenity(id="3", name="Hot tub")
            }
            self.assertIsInstance(self.place.amenities, list)
            self.assertEqual(len(self.place.amenities), 0)

    @unittest.skipIf(os.environ.get("HBNB_TYPE_STORAGE") == "file", "Testing file storage only")
    def test_amenities_relationship(self):
        """
        Test the amenities relationship when using database storage
        """
        with patch("models.storage.all") as mock_storage:
            mock_amenity = Amenity(id="1", name="Wifi")
            self.place.amenities.append(mock_amenity)
            mock_storage.return_value = { "Amenity.1": mock_amenity }
            self.assertIn(mock_amenity, self.place.amenities)
