#!/usr/bin/python3
"""
Unittest for a City class
"""
import unittest
from models.city import City
import datetime


class TestCity(unittest.TestCase):
    """
    TestCity class
    """

    city = City()

    def test_city_class(self):
        """
        Test for city class
        """
        self.assertEqual(str(type(self.city)), "<class 'models.city.City'>")

    def test_city_inheritance(self):
        """
        Test for city inheritance
        """
        self.assertIsInstance(self.city, City)

    def test_city_attributes(self):
        """
        Test for city attributes
        """
        self.assertTrue(hasattr(self.city, "name"))
        self.assertTrue(hasattr(self.city, "id"))
        self.assertTrue(hasattr(self.city, "created_at"))
        self.assertTrue(hasattr(self.city, "updated_at"))

    def test_city_type(self):
        """
        Test for city type
        """
        self.assertIsInstance(self.city.name, str)
        self.assertIsInstance(self.city.state_id, str)
        self.assertIsInstance(self.city.id, str)
        self.assertIsInstance(self.city.created_at, datetime.datetime)
        self.assertIsInstance(self.city.updated_at, datetime.datetime)


if __name__ == '__main__':
    unittest.main()
