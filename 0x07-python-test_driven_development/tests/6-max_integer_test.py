#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    def test_regular_list(self):
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)
        self.assertEqual(max_integer([1, 3, 4, 2]), 4)

    def test_negative_numbers(self):
        self.assertEqual(max_integer([-1, -2, -3, -4]), -1)

    def test_mixed_numbers(self):
        self.assertEqual(max_integer([-1, 2, -3, 4]), 4)

    def test_single_element_list(self):
        self.assertEqual(max_integer([5]), 5)

    def test_empty_list(self):
        self.assertIsNone(max_integer([]))

    def test_float_numbers(self):
        self.assertEqual(max_integer([1.5, 2.5, 3.5]), 3.5)

    def test_string_list(self):
        self.assertEqual(max_integer(['a', 'b', 'c']), 'c')

    def test_mixed_type_list(self):
        with self.assertRaises(TypeError):
            max_integer([1, 'two', 3])

if __name__ == '__main__':
    unittest.main()
