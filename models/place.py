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


class Place(BaseModel, Base):
    """
    Place class to represent places
    """
    __tablename__ = "places"
    city_id = Column(String(60), ForeignKey("cities.id"), nullable=False)
    user_id = Column(String(60), ForeignKey("users.id"), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024), nullable=True)
    number_rooms = Column(Integer, nullable=False, default=0)
    number_bathrooms = Column(Integer, nullable=False, default=0)
    max_guest = Column(Integer, nullable=False, default=0)
    price_by_night = Column(Integer, nullable=False, default=0)
    latitude = Column(Float, nullable=True)
    longitude = Column(Float, nullable=True)
    amenity_ids = List[str] = []
    reviews = relationship("Review", back_populates="place")
    amenities = relationship("Amenity",
                             secondary=place_amenity,
                             back_populates="place_amenities",
                             viewonly=False)

    @property
    def reviews(self) -> List["Review"]:
        """Getter function for reviews attribute"""
        return [r for r in models.storage.all("Review").values()
                if r.place_id == self.id]

    @property
    def amenities(self) -> List["Amenity"]:
        """Getter function for amenity attribute"""
        return [a for a in models.storage.all("Amenity").values()
                if a.id in self.amenity_ids]

    @amenities.setter
    def amenities(self, amenity_obj: "Amenity") -> None:
        """Setter function for amenity attribute"""
        if isinstance(amenity_obj, Amenity):
            self.amenity_ids.append(amenity_obj.id)
