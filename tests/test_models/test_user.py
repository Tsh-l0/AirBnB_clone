#!/usr/bin/python3
"""
Unit tests for the user class
"""
import unittest
from models.user import User
from models.base_model import BaseModel
from datetime import datetime


class TestUser(unittest.TestCase):
    """
    Unit tests for the User class
    """

    def test_instance_creation(self):
        """
        Test that a new user is created successfully
        """
        user = User()
        self.assertIsInstance(user, User)
        self.assertIsInstance(user, BaseModel)
        self.assertIsInstance(user.id, str)
        self.assertIsInstance(user.created_at, datetime)
        self.assertIsInstance(user.updated_at, datetime)
        self.assertEqual(user.email, "")
        self.assertEqual(user.password, "")
        self.assertEqual(user.first_name, "")
        self.assertEqual(user.last_name, "")

    def test_strmethod(self):
        """
        Test the str method for user
        """
        user = User()
        expected_str = "[User] ({}) {}".format(user.id, user.__dict__)
        self.assertEqual(str(user), expected_str)

    def test_todict(self):
        """
        Test the to_dict method returns a correct dictionary
        """
        user = User()
        user_dict = user.to_dict()
        self.assertEqual(user_dict['__class__'], 'User')
        self.assertEqual(user_dict['id'], user.id)
        self.assertEqual(user_dict['created_at'],
                         user.created_at.isoformat())
        self.assertEqual(user_dict['updated_at'],
                         user.updated_at.isoformat())
        self.assertIn('password', user_dict)
        self.assertIn('first_name', user_dict)
        self.assertIn('last_name', user_dict)

    def test_instance_creation_with_kwargs(self):
        """
        Test that a new instance can be created using a dictionary (kwargs)
        """
        user = User()
        user.email = "airbnb@mail.com"
        user.password = "root"
        user.first_name = "Betty"
        user.last_name = "Bar"
        user_dict = user.to_dict()

        new_user = User(**user_dict)
        self.assertEqual(new_user.id, user.id)
        self.assertEqual(new_user.created_at, user.created_at)
        self.assertEqual(new_user.updated_at, user.updated_at)
        self.assertEqual(new_user.email, user.email)
        self.assertEqual(new_user.password, user.password)
        self.assertEqual(new_user.first_name, user.first_name)
        self.assertEqual(new_user.last_name, user.last_name)

    def test_savemethod(self):
        """
        Test the save method updates `updated_at`
        """
        user = User()
        old_updated_at = user.updated_at
        user.save()
        self.assertNotEqual(user.updated_at, old_updated_at)


if __name__ == '__main__':
    unittest.main()
