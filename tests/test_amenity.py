#!/usr/bin/python3
"""
Unittest for Amenity class
"""
import unittest
from models.amenity import Amenity
import datetime


class TestAmenity(unittest.TestCase):
    """
    Test aminity class
    """

    amenity = Amenity()

    def test_amenity_class(self):
        """
        Test for amenity class
        """
        self.assertEqual(
            str(type(self.amenity)),
            "<class 'models.amenity.Amenity'>"
        )

    def test_amenity_inheritance(self):
        """
        Test for amenity inheritance
        """
        self.assertIsInstance(self.amenity, Amenity)

    def test_amenity_attributes(self):
        """
        Test for amenity attributes
        """
        self.assertTrue(hasattr(self.amenity, "name"))
        self.assertTrue(hasattr(self.amenity, "id"))
        self.assertTrue(hasattr(self.amenity, "created_at"))
        self.assertTrue(hasattr(self.amenity, "updated_at"))

    def test_amenity_type(self):
        """
        Test for amenity type
        """
        self.assertIsInstance(self.amenity.name, str)
        self.assertIsInstance(self.amenity.id, str)
        self.assertIsInstance(self.amenity.created_at, datetime.datetime)
        self.assertIsInstance(self.amenity.updated_at, datetime.datetime)


if __name__ == '__main__':
    unittest.main()
