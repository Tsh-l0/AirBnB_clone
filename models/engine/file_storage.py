#!/usr/bin/python3
"""
A class to manage file storage for objects
"""
import json
from models.base_model import BaseModel


class FileStorage:
    """
    Serializes instance to a JSON file and deserializes JSON files
    to instance
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """
        Returns the dictionary '__objects'
        """
        return self.__objects

    def new(self, obj):
        """
        Sets in '__objects the obj with key <obj class name> id
        """
        key = f"{obj.__class__.__name__}.{obj.id}"
        self.__objects[key] = obj

    def save(self):
        """
        Serializes __objects to the JSON file
        """
        obj_dict = {key: obj.to_dict() for key, obj in self.__objects.items()}
        with open(self.__file_path, "w") as f:
            json.dump(obj_dict, f)

    def reload(self):
        """
        Deserializes the JSON file to __objects, if the JSON file exists
        """
        cls_map = {"BaseModel": BaseModel}
        try:
            with open(self.__file_path, "r") as f:
                obj_dict = json.load(f)
                for key, value in obj_dict.items():
                    cls_name = value["__class__"]
                    if cls_name in cls_map:
                        self.__objects[key] = cls_map[cls_name](**value)
        except FileNotFoundError:
            pass
