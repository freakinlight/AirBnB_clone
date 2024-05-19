#!/usr/bin/python3
"""
Unittest module for the BaseModel class.
"""

import unittest
from models.base_model import BaseModel
from datetime import datetime


class TestBaseModel(unittest.TestCase):
    """
    Test cases for the BaseModel class.
    """

    def test_instance_creation(self):
        """
        Test if instance is created correctly.
        """
        instance = BaseModel()
        self.assertIsInstance(instance, BaseModel)
        self.assertIsInstance(instance.id, str)
        self.assertIsInstance(instance.created_at, datetime)
        self.assertIsInstance(instance.updated_at, datetime)

    def test_save_method(self):
        """
        Test if save method updates `updated_at` attribute.
        """
        instance = BaseModel()
        old_updated_at = instance.updated_at
        instance.save()
        self.assertNotEqual(instance.updated_at, old_updated_at)

    def test_to_dict_method(self):
        """
        Test if to_dict method creates correct dictionary.
        """
        instance = BaseModel()
        instance_dict = instance.to_dict()
        self.assertEqual(instance_dict['__class__'], 'BaseModel')
        self.assertEqual(instance_dict['id'], instance.id)
        self.assertEqual(instance_dict['created_at'], instance.created_at.isoformat())
        self.assertEqual(instance_dict['updated_at'], instance.updated_at.isoformat())


if __name__ == '__main__':
    unittest.main()

