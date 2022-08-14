#!/usr/bin/python3
"""
The State class Unitest
"""
import unittest
from models.state import State
import datetime


class TestState(unittest.TestCase):
    """
    unitest for state class
    """
    state = State()

    def test_state_init(self):
        """
        test state init
        """
        self.assertEqual(str(type(self.state)), "<class 'models.state.State'>")

    def test_state_inheritance(self):
        """
        Test state inheritance

        """
        self.assertIsInstance(self.state, State)

    def test_state_attributes(self):
        """
        test state attributes
        """
        self.assertTrue(hasattr(self.state, "name"))
        self.assertTrue(hasattr(self.state, "id"))
        self.assertTrue(hasattr(self.state, "created_at"))
        self.assertTrue(hasattr(self.state, "updated_at"))

    def test_state_type(self):
        """
        test state type
        """
        self.assertEqual(type(self.state.name), str)
        self.assertEqual(type(self.state.id), str)
        self.assertEqual(type(self.state.created_at), datetime.datetime)
        self.assertEqual(type(self.state.updated_at), datetime.datetime)


if __name__ == "__main__":
    unittest.main()
