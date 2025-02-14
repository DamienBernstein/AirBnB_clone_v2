#!/usr/bin/python3

"""
This is the user class.
"""

from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship


class User(BaseModel, Base):
    """
    This is the class for user.

    Attributes:
        email (str): email address
        password (str): password for your login
        first_name (str): first name
        last_name (str): last name
    """
    __tablename__ = "users"
    email = Column(String(128), nullable=False)
    password = Column(String(128), nullable=False)
    first_name = Column(String(128))
    last_name = Column(String(128))
    places = relationship("Place",
                          backref="user",
                          cascade="all, delete, delete-orphan")
    reviews = relationship("Review",
                           backref="user",
                           cascade="all, delete, delete-orphan")
