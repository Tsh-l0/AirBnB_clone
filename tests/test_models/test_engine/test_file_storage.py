#!/usr/bin/python3
"""
Unit tests for FileStorage
"""
import unittest
import json
import os
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel


class TestFileStorage(unittest.TestCase):
    """
    Test cases for FileStorage
    """

    def setUp(self):
        """
        Set up test environment
        """
        self.storage = FileStorage()
        self.file_path = self.storage._FileStorage__file_path
        self.storage._FileStorage__objects = {}

    def tearDown(self):
        """
        Clean uo the test environment
        """
        if os.path.exists(self.file_path):
            os.remove(self.file_path)

    def test_all_method(self):
        """
        Test that the all() returns the __objects dictionary
        """
        self.assertEqual(self.storage.all(),
                         self.storage._FileStorage__objects)

    def test_new_method(self):
        """
        Test the new() method adds an object to __objects
        """
        instance = BaseModel()
        self.storage.new(instance)
        key = "{}.{}".format(type(instance).__name__, instance.id)
        self.assertIn(key, self.storage.all())
        self.assertEqual(self.storage.all()[key], instance)

    def test_save_method(self):
        """
        Test the save() method serializes __objects to the JSON file
        """
        instance = BaseModel()
        self.storage.new(instance)
        self.storage.save()
        with open(self.file_path, "r") as f:
            obj_dict = json.load(f)
        key = "{}.{}".format(type(instance).__name__, instance.id)
        self.assertIn(key, obj_dict)
        self.assertEqual(obj_dict[key]['id'], instance.id)
        self.assertEqual(obj_dict[key]['__class__'], 'BaseModel')

    def test_reload_method(self):
        """
        Test the reload() method deserializes the JSON file to __objects
        """
        instance = BaseModel()
        self.storage.new(instance)
        self.storage.save()
        self.storage._FileStorage__objects = {}
        self.storage.reload()
        key = "{}.{}".format(type(instance).__name__, instance.id)
        self.assertIn(key, self.storage.all())
        self.assertEqual(self.storage.all()[key].id, instance.id)
        self.assertEqual(self.storage.all()[key].__class__.__name__,
                         'BaseModel')

    def test_reload_no_file(self):
        """
        Test that reload() does nothing if the JSON file does not exist
        """
        if os.path.exists(self.file_path):
            os.remove(self.file_path)
        self.storage.reload()
        self.assertEqual(self.storage.all(), {})

    def test_serialization_deserialization(self):
        """
        Test the full serialization and deserialization flow
        """
        instance = BaseModel()
        self.storage.new(instance)
        self.storage.save()
        self.storage._FileStorage__objects = {}
        self.storage.reload()
        key = "{}.{}".format(type(instance).__name__, instance.id)
        self.assertIn(key, self.storage.all())
        self.assertEqual(self.storage.all()[key].id, instance.id)
        self.assertEqual(self.storage.all()[key].__class__.__name__,
                         'BaseModel')


if __name__ == '__main__':
    unittest.main()
