#!/usr/bin/python3
"""
Initializes the storage engine and reloads the storage objects
"""
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review

storage = FileStorage()
storage.reload()

# Add the imported classes to the namespace
__all__ = ["BaseModel", "User", "State", "City", "Amenity", "Place", "Review"]
