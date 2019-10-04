#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """TestMaxInteger class to try different cases

    """
    def test_empty_list(self):
        self.assertFalse(max_integer([]))

    def test_simple_list(self):
        self.assertEqual(max_integer([1, 2, 3]), 3)
        self.assertEqual(max_integer([-1, -2, -3]), -1)

    def test_simple_tuple(self):
        self.assertEqual(max_integer((1, 2, 3)), 3)

    def test_list_list(self):
        self.assertEqual(max_integer([[1, 2, 3], [4, 5, 6]]), [4, 5, 6])

    def test_list_tuples(self):
        self.assertEqual(max_integer([(1, 2, 3), (4, 5, 6)]), (4, 5, 6))

    def test_float_list(self):
        self.assertEqual(max_integer([1.3, 2.5, 3.8]), 3.8)

    def test_int_float_list(self):
        self.assertEqual(max_integer([1, 3.5, 6, 9.5]), 9.5)

    def test_string(self):
        self.assertEqual(max_integer("string"), "t")

    def test_one_elem(self):
        self.assertEqual(max_integer(["string"]), "string")
        self.assertEqual(max_integer([100]), 100)
        self.assertEqual(max_integer([20.5]), 20.5)
        self.assertEqual(max_integer("Z"), "Z")

    def test_err_type(self):
        with self.assertRaises(TypeError):
            max_integer(20.5)
        with self.assertRaises(TypeError):
            max_integer([(1, 2, 3), [4, 5, 6]])
        with self.assertRaises(TypeError):
            max_integer(["z", ("a", "b")])
        with self.assertRaises(TypeError):
            max_integer([1, 2], [3, 4])

if __name__ == '__main__':
    unittest.main()
