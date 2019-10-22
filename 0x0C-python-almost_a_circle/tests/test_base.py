#!/usr/bin/python3
"""Unittest module for Base class"""
import unittest
from models.base import Base


class TestBaseClass(unittest.TestCase):
    """TestBaseClass class to test the Base class"""

    def test_id_base(self):
        """test id creation"""
        base_inst_1 = Base()
        base_inst_2 = Base()
        base_inst_3 = Base()
        base_inst_4 = Base(12)
        base_inst_5 = Base(None)
        self.assertEqual(base_inst_1.id, 1)
        self.assertEqual(base_inst_2.id, 2)
        self.assertEqual(base_inst_3.id, 3)
        self.assertEqual(base_inst_4.id, 12)
        self.assertEqual(base_inst_5.id, 4)

    def test_er_type_base(self):
        """Test Error arguments"""
        with self.assertRaises(TypeError):
            b1 = Base(10, 2)

if __name__ == '__main__':
    unittest.main()
