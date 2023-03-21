#!/usr/bin/python3

"""
State class
"""

import os
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship
from models.base_model import BaseModel, Base


class State(BaseModel, Base):
    """
    This is the class for State.

    Attributes:
        name (str): input name
    """
    __tablename__ = "states"

    name = Column(String(128), nullable=False)

    if os.getenv("HBNB_TYPE_STORAGE") == "db":
        cities = relationship("City",
                              cascade="all, delete, delete-orphan",
                              backref="state")
    else:
        @property
        def cities(self):
            """Return a list of cities."""
            city_list = [city for city in models.storage.all(City).values()
                         if city.state_id == self.id]
            return city_list
