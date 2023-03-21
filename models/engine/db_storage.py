import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from models.base_model import Base
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User


class DBStorage:
    __engine = None
    __session = None

    def __init__(self):
        self.__engine = create_engine(
            'mysql+mysqldb://{}:{}@{}/{}'.
            format(
                os.getenv("HBNB_MYSQL_USER"),
                os.getenv("HBNB_MYSQL_PWD"),
                os.getenv("HBNB_MYSQL_HOST"),
                os.getenv("HBNB_MYSQL_DB")),
            pool_pre_ping=True
        )
        if os.getenv("HBNB_ENV") == "test":
            Base.metadata.drop_all(bind=self.__engine)

    def all(self, cls=None):
        classes = [City, State, User, Place, Review, Amenity]
        objs = {}
        if cls:
            query = self.__session.query(cls)
        else:
            query = self.__session.query(*classes)

        for obj in query:
            key = type(obj).__name__ + "." + obj.id
            objs[key] = obj

        return objs

    def new(self, obj):
        self.__session.add(obj)

    def save(self):
        self.__session.commit()

    def delete(self, obj=None):
        if obj:
            self.__session.delete(obj)

    def reload(self):
        Base.metadata.create_all(self.__engine)

        Session = sessionmaker(bind=self.__engine, expire_on_commit=False)
        self.__session = scoped_session(Session)

    def close(self):
        self.__session.remove()
