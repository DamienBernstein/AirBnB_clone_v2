import unittest
from models.base_model import BaseModel, Base
from sqlalchemy.orm import relationship
from sqlalchemy import Column, String, Integer, Float, ForeignKey, Table
from typing import List

# Define storage engine here
storage_engine = "db"

if storage_engine == "db":
    place_amenity = Table('place_amenity', Base.metadata,
                          Column('place_id', String(60),
                                 ForeignKey('places.id'),
                                 primary_key=True, nullable=False),
                          Column('amenity_id', String(60),
                                 ForeignKey('amenities.id'),
                                 primary_key=True, nullable=False))


class TestPlace(unittest.TestCase):

    def test_place(self):
        # Create a new Place object
        place = Place()

        # Set some values for the object
        place.name = "My Place"
        place.description = "A great place to stay!"

        # Test that the values were set correctly
        self.assertEqual(place.name, "My Place")
        self.assertEqual(place.description, "A great place to stay!")


    def setUp(self):
        self.place = Place()

    def test_reviews(self):
        self.place.reviews = [Review()]
        self.assertEqual(len(self.place.reviews), 1)

    def test_amenities(self):
        self.place.amenities = Amenity()
        self.assertEqual(len(self.place.amenities), 1)
        self.assertTrue(isinstance(self.place.amenities[0], Amenity))

    def test_amenities_setter(self):
        amenity = Amenity()
        self.place.amenities = amenity
        self.assertEqual(len(self.place.amenity_ids), 1)
        self.assertEqual(self.place.amenity_ids[0], amenity.id)
