#!/usr/bin/python3
"""
Module for unit testing of Base, Rectangle, and Square classes.

This test suite provides comprehensive coverage of all methods and attributes
for the geometric shape classes. It includes tests for initialization,
validation, calculations, display methods, and JSON serialization.

Classes:
    TestBase: Test cases for the Base class
    TestRectangle: Test cases for the Rectangle class
    TestSquare: Test cases for the Square class
"""
import unittest
import os
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square
from io import StringIO
from unittest.mock import patch


class TestBase(unittest.TestCase):
    """
    Test cases for Base class.

    Tests ID assignment, JSON string conversion, and documentation standards.
    """

    def setUp(self):
        """Reset nb_objects counter before each test."""
        Base._Base__nb_objects = 0

    def test_base_module_docstring(self):
        """Verify presence and length of module docstring."""
        self.assertIsNotNone(Base.__doc__)
        self.assertGreater(len(Base.__doc__), 1)

    def test_base_class_docstring(self):
        """Verify presence and length of class docstring."""
        self.assertIsNotNone(Base.__doc__)
        self.assertGreater(len(Base.__doc__), 1)

    def test_base_init_id(self):
        """Test Base instance ID assignment with various inputs."""
        b1 = Base()
        b2 = Base()
        b3 = Base(12)
        b4 = Base(-5)
        self.assertEqual(b1.id, 1)
        self.assertEqual(b2.id, 2)
        self.assertEqual(b3.id, 12)
        self.assertEqual(b4.id, -5)

    def test_base_init_large_id(self):
        """Test Base instance with large integer ID."""
        b = Base(100000000000)
        self.assertEqual(b.id, 100000000000)

    def test_base_to_json_string(self):
        """Test conversion of dictionary list to JSON string."""
        list_dicts = [
            {'id': 1, 'width': 10, 'height': 7},
            {'id': 2, 'width': 2, 'height': 4}
        ]
        json_str = Base.to_json_string(list_dicts)
        self.assertIsInstance(json_str, str)
        self.assertIn('"id": 1', json_str)
        self.assertIn('"width": 10', json_str)

    def test_base_to_json_string_empty(self):
        """Test JSON string conversion with empty list."""
        json_str = Base.to_json_string([])
        self.assertEqual(json_str, "[]")

    def test_base_to_json_string_none(self):
        """Test JSON string conversion with None input."""
        json_str = Base.to_json_string(None)
        self.assertEqual(json_str, "[]")

    def test_base_from_json_string(self):
        """Test conversion of JSON string to dictionary list."""
        json_str = '[{"id": 1, "width": 10, "height": 7}]'
        list_dicts = Base.from_json_string(json_str)
        self.assertIsInstance(list_dicts, list)
        self.assertEqual(list_dicts[0]['id'], 1)

    def test_base_from_json_string_empty(self):
        """Test conversion of empty JSON string."""
        list_dicts = Base.from_json_string("[]")
        self.assertEqual(list_dicts, [])

    def test_base_from_json_string_none(self):
        """Test conversion of None JSON string."""
        list_dicts = Base.from_json_string(None)
        self.assertEqual(list_dicts, [])


class TestRectangle(unittest.TestCase):
    """
    Test cases for Rectangle class.

    Tests initialization, validation, area calculation, display, and updates.
    """

    def setUp(self):
        """Reset nb_objects counter before each test."""
        Base._Base__nb_objects = 0

    def test_rectangle_module_docstring(self):
        """Verify presence and length of module docstring."""
        self.assertIsNotNone(Rectangle.__doc__)
        self.assertGreater(len(Rectangle.__doc__), 1)

    def test_rectangle_init(self):
        """Test Rectangle initialization with various parameters."""
        r1 = Rectangle(10, 2)
        r2 = Rectangle(2, 10, 1, 1, 12)
        self.assertEqual(r1.width, 10)
        self.assertEqual(r1.height, 2)
        self.assertEqual(r2.x, 1)
        self.assertEqual(r2.y, 1)
        self.assertEqual(r2.id, 12)

    def test_rectangle_negative_attributes(self):
        """Test validation of negative attribute values."""
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Rectangle(-10, 2)
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            Rectangle(10, -2)
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            Rectangle(10, 2, -1, 0)
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            Rectangle(10, 2, 0, -1)

    def test_rectangle_zero_x_y(self):
        """Test initialization with zero x and y coordinates."""
        r = Rectangle(10, 2, 0, 0)
        self.assertEqual(r.x, 0)
        self.assertEqual(r.y, 0)

    def test_rectangle_area(self):
        """Test area calculation method."""
        r1 = Rectangle(3, 2)
        self.assertEqual(r1.area(), 6)

    def test_rectangle_display(self):
        """Test string display representation."""
        r1 = Rectangle(2, 2)
        expected_output = "##\n##\n"
        with patch('sys.stdout', new=StringIO()) as fake_out:
            r1.display()
            self.assertEqual(fake_out.getvalue(), expected_output)

    def test_rectangle_str(self):
        """Test string representation of Rectangle."""
        r1 = Rectangle(4, 6, 2, 1, 12)
        expected = "[Rectangle] (12) 2/1 - 4/6"
        self.assertEqual(str(r1), expected)

    def test_rectangle_update(self):
        """Test update method with positional arguments."""
        r1 = Rectangle(10, 10, 10, 10)
        r1.update(89, 2, 3, 4, 5)
        self.assertEqual(str(r1), "[Rectangle] (89) 4/5 - 2/3")

    def test_rectangle_update_kwargs(self):
        """Test update method with keyword arguments."""
        r1 = Rectangle(10, 10, 10, 10)
        r1.update(id=89, width=3, height=4, x=5, y=6)
        self.assertEqual(str(r1), "[Rectangle] (89) 5/6 - 3/4")

    def test_rectangle_to_dictionary(self):
        """Test conversion to dictionary representation."""
        r1 = Rectangle(10, 2, 1, 9)
        r1_dict = r1.to_dictionary()
        expected = {'x': 1, 'y': 9, 'id': 1, 'height': 2, 'width': 10}
        self.assertEqual(r1_dict, expected)


class TestSquare(unittest.TestCase):
    """
    Test cases for Square class.

    Tests initialization, validation, area calculation, and updates.
    """

    def setUp(self):
        """Reset nb_objects counter before each test."""
        Base._Base__nb_objects = 0

    def test_square_module_docstring(self):
        """Verify presence and length of module docstring."""
        self.assertIsNotNone(Square.__doc__)
        self.assertGreater(len(Square.__doc__), 1)

    def test_square_init(self):
        """Test Square initialization with various parameters."""
        s1 = Square(5)
        s2 = Square(2, 2, 2, 12)
        self.assertEqual(s1.size, 5)
        self.assertEqual(s2.x, 2)
        self.assertEqual(s2.y, 2)
        self.assertEqual(s2.id, 12)

    def test_square_validation(self):
        """Test attribute validation for Square."""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square("10")
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Square(-10)

    def test_square_area(self):
        """Test area calculation method."""
        s1 = Square(5)
        self.assertEqual(s1.area(), 25)

    def test_square_display(self):
        """Test string display representation."""
        s1 = Square(2)
        expected_output = "##\n##\n"
        with patch('sys.stdout', new=StringIO()) as fake_out:
            s1.display()
            self.assertEqual(fake_out.getvalue(), expected_output)

    def test_square_str(self):
        """Test string representation of Square."""
        s1 = Square(2, 2, 2, 12)
        expected = "[Square] (12) 2/2 - 2"
        self.assertEqual(str(s1), expected)

    def test_square_update(self):
        """Test update method with positional arguments."""
        s1 = Square(5)
        s1.update(10, 2, 3, 4)
        self.assertEqual(str(s1), "[Square] (10) 3/4 - 2")

    def test_square_update_kwargs(self):
        """Test update method with keyword arguments."""
        s1 = Square(5)
        s1.update(id=10, size=2, x=3, y=4)
        self.assertEqual(str(s1), "[Square] (10) 3/4 - 2")

    def test_square_to_dictionary(self):
        """Test conversion to dictionary representation."""
        s1 = Square(10, 2, 1)
        s1_dict = s1.to_dictionary()
        expected = {'id': 1, 'size': 10, 'x': 2, 'y': 1}
        self.assertEqual(s1_dict, expected)


if __name__ == "__main__":
    unittest.main()
