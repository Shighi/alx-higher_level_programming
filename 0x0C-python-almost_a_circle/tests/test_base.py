#!/usr/bin/python3
"""Unittest for Base class"""
import unittest
from models.base import Base


class TestBase(unittest.TestCase):
    """Test cases for Base class"""

    def test_id_assignment(self):
        """Test id assignment"""
        b1 = Base()
        self.assertEqual(b1.id, 1)

        b2 = Base()
        self.assertEqual(b2.id, 2)

        b3 = Base(12)
        self.assertEqual(b3.id, 12)


if __name__ == "__main__":
    unittest.main()
