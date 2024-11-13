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

    def __init__(self):

        """
        Initializes the class BaseModel
        """
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = self.created_at

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
