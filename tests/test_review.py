#!/usr/bin/python3
"""
Unittest for review.py file

"""
import datetime
import unittest
from models.review import Review


class TestReview(unittest.TestCase):
    """
    test instances for review class
    """

    review = Review()

    def test_review_class(self):
        """
        test for review class
        """
        self.assertEqual(
            str(type(self.review)),
            "<class 'models.review.Review'>"
        )

    def test_review_inheritance(self):
        """
        test for review inheritance
        """
        self.assertIsInstance(self.review, Review)

    def test_review_attributes(self):
        """
        test for review attributes
        """
        self.assertTrue(hasattr(self.review, "place_id"))
        self.assertTrue(hasattr(self.review, "user_id"))
        self.assertTrue(hasattr(self.review, "text"))
        self.assertTrue(hasattr(self.review, "id"))
        self.assertTrue(hasattr(self.review, "created_at"))
        self.assertTrue(hasattr(self.review, "updated_at"))

    def test_review_type(self):
        """
        test for review type
        """
        self.assertIsInstance(self.review.place_id, str)
        self.assertIsInstance(self.review.user_id, str)
        self.assertIsInstance(self.review.text, str)
        self.assertIsInstance(self.review.id, str)
        self.assertIsInstance(self.review.created_at, datetime.datetime)
        self.assertIsInstance(self.review.updated_at, datetime.datetime)


if __name__ == '__main__':
    unittest.main()
