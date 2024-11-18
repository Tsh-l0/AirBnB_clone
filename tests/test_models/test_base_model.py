#!/usr/bin/python3
"""
Unit tests for the BaseModel class
"""
import unittest
from models.base_model import BaseModel
from datetime import datetime
import uuid


class TestBaseModel(unittest.TestCase):
    """
    Test cases for the BaseModel class
    """

    def test_instance_creation(self):
        """
        Check that a new instance has been created successfully
        """
        instance = BaseModel()
        self.assertIsInstance(instance, BaseModel)
        self.assertIsInstance(instance.id, str)
        self.assertIsInstance(instance.created_at, datetime)
        self.assertIsInstance(instance.updated_at, datetime)

    def test_unique_uuid(self):
        """
        Test that each instance gets a unique uuid
        """
        instance1 = BaseModel()
        instance2 = BaseModel()
        self.assertNotEqual(instance1.id, instance2.id)

    def test_str_method(self):
        """
        Check the __str__ method for BaseModel
        """
        instance = BaseModel()
        expected_str = "[BaseModel] ({}) {}".format(instance.id,
                                                    instance.__dict__)
        self.assertEqual(str(instance), expected_str)

    def test_save_method(self):
        """
        Test the "updated_at" functionality
        """
        instance = BaseModel()
        old_updated_at = instance.updated_at
        instance.save()
        self.assertNotEqual(instance.updated_at, old_updated_at)

    def test_to_dict(self):
        """
        Check if the to_dict method returns correct dictionary
        """
        instance = BaseModel()
        instance_dict = instance.to_dict()
        self.assertEqual(instance_dict['__class__'], 'BaseModel')
        self.assertEqual(instance_dict['id'], instance.id)
        self.assertEqual(instance_dict['created_at'],
                         instance.created_at.isoformat())
        self.assertEqual(instance_dict['updated_at'],
                         instance.updated_at.isoformat())

    def test_to_dict_contains_correct_keys(self):
        """
        Check the to_dict method returns proper keys
        """
        instance = BaseModel()
        instance_dict = instance.to_dict()
        expected_keys = ['id', 'created_at', 'updated_at', '__class__']
        self.assertTrue(all(key in instance_dict for key in expected_keys))

    def test_dict_with_added_attributes(self):
        """
        Test to_dict method with added instance attributes
        """
        instance = BaseModel()
        instance.name = "My First Model"
        instance.my_number = 89
        instance_dict = instance.to_dict()
        self.assertEqual(instance_dict['name'], "My First Model")
        self.assertEqual(instance_dict['my_number'], 89)

    def test_datetime_format(self):
        """
        Test that the created_at and updated_at formats are correct
        """
        instance = BaseModel()
        instance_dict = instance.to_dict()
        created_at_format = instance_dict['created_at']
        updated_at_format = instance_dict['updated_at']
        try:
            datetime.fromisoformat(created_at_format)
            datetime.fromisoformat(updated_at_format)
        except ValueError:
            self.fail("datetime format is incorrect")

    def test_id_uniqueness(self):
        """
        Check that instance IDs are unique throught the different instance
        """
        instance1 = BaseModel()
        instance2 = BaseModel()
        self.assertNotEqual(instance1.id, instance2.id)
        self.assertIsInstance(uuid.UUID(instance1.id), uuid.UUID)
        self.assertIsInstance(uuid.UUID(instance2.id), uuid.UUID)


if __name__ == '__main__':
    unittest.main()
