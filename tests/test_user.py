#!/usr/bin/python3
"""
unitest for user class

"""
import unittest
from models.user import User
import datetime


class TestUser(unittest.TestCase):
    """
    unitest for user class
    """
    user = User()

    def test_user_init(self):
        """
        test user init
        """
        self.assertEqual(str(type(self.user)), "<class 'models.user.User'>")

    def test_user_inheritance(self):
        """
        test user inheritance
        """
        self.assertIsInstance(self.user, User)

    def test_user_attributes(self):
        """
        test user attributes
        """
        self.assertTrue(hasattr(self.user, "email"))
        self.assertTrue(hasattr(self.user, "password"))
        self.assertTrue(hasattr(self.user, "first_name"))
        self.assertTrue(hasattr(self.user, "last_name"))
        self.assertTrue(hasattr(self.user, "id"))
        self.assertTrue(hasattr(self.user, "created_at"))
        self.assertTrue(hasattr(self.user, "updated_at"))

    def test_user_type(self):
        """
        test user type
        """
        self.assertEqual(type(self.user.email), str)
        self.assertEqual(type(self.user.password), str)
        self.assertEqual(type(self.user.first_name), str)
        self.assertEqual(type(self.user.last_name), str)
        self.assertEqual(type(self.user.id), str)
        self.assertEqual(type(self.user.created_at), datetime.datetime)
        self.assertEqual(type(self.user.updated_at), datetime.datetime)


if __name__ == "__main__":
    unittest.main()
