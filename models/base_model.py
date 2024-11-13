#!/usr/bin/python3

"""
Modules to be imported
"""
import uuid
from datetime import datetime


class BaseModel:
    """
    Defines all common methods/attributes for other classes
    """

    def __init__(self, *args, **kwargs):
        """
        Initializes the class BaseModel
        if kwargs is not empty, each key of the dictionary is an
        attribute name
        Otherwise, create id and created_at as a new instance
        """
        if kwargs:
            for key, value in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    value = datetime.fromisoformat(value)
                if key != "__class__":
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            self._get_storage().new(self)

    def __str__(self):
        """
        Prints the string representation of an instance
        """
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """
        Updates public instance attribute 'updated_at' with the current
        datetime
        """
        self.updated_at = datetime.now()
        self._get_storage().save()

    def to_dict(self):
        """
        Returns a dictionary contailing all the keys/values of __dict__ of
        the instance.
        Adds a key __class__ with the class name of the object
        Converts created_at and updated_at to string object in ISO format
        """
        dict_rep = self.__dict__.copy()
        dict_rep["__class__"] = self.__class__.__name__
        dict_rep["created_at"] = self.created_at.isoformat()
        dict_rep["updated_at"] = self.updated_at.isoformat()
        return dict_rep

    def _get_storage(self):
        from models import storage
        return storage
