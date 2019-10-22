#!/usr/bin/python3
"""Unittest module for Square class"""

import unittest
from unittest.mock import patch
from io import StringIO
from models.square import Square


class TestSquareClass(unittest.TestCase):
    """TestSquareClass class to test the Square class"""

    def test_attr_squa(self):
        squa_inst_1 = Square(10)
        squa_inst_2 = Square(10, 0, 0, 12)
        squa_inst_3 = Square(3, 0, 0, None)
        self.assertEqual(squa_inst_1.size, 10)
        self.assertEqual(squa_inst_2.size, 10)
        self.assertEqual(squa_inst_2.x, 0)
        self.assertEqual(squa_inst_2.y, 0)
        self.assertEqual(squa_inst_2.id, 12)
        squa_inst_3.size = 20
        self.assertEqual(squa_inst_3.size, 20)
        squa_inst_3.x = 20
        self.assertEqual(squa_inst_3.x, 20)
        squa_inst_3.y = 20
        self.assertEqual(squa_inst_3.y, 20)
        squa_inst_3.id = 20
        self.assertEqual(squa_inst_3.id, 20)
        self.assertEqual(squa_inst_1.area(), 100)

    def test_er_argum_rect(self):
        with self.assertRaises(TypeError):
            s4 = Square(10, 2, 0, 0, 12, 12)
        with self.assertRaises(TypeError):
            s5 = Square()
        with self.assertRaises(TypeError):
            s6 = Square(10)
            s6.area(100)
        with self.assertRaises(TypeError):
            s7 = Square(2, 2, 2)
            s7.display(10)
        with self.assertRaises(TypeError):
            s1 = Square(2, 2, 2)
            s1.to_dictionary(10)

    def test_er_type_squa_size(self):
        with self.assertRaises(TypeError):
            s8 = Square('h')
        with self.assertRaises(TypeError):
            s9 = Square([1, 1])
        with self.assertRaises(TypeError):
            s10 = Square((1, 1))
        with self.assertRaises(TypeError):
            s11 = Square({'k': 10})
        with self.assertRaises(TypeError):
            s12 = Square(10.5)
        with self.assertRaises(TypeError):
            s13 = Square(True)

    def test_er_val_squa_size(self):
        with self.assertRaises(ValueError):
            s14 = Square(-10)
        with self.assertRaises(ValueError):
            s15 = Square(0)

    def test_er_type_squa_x(self):
        with self.assertRaises(TypeError):
            s16 = Square(10, 'h')
        with self.assertRaises(TypeError):
            s17 = Square(10, [1])
        with self.assertRaises(TypeError):
            s18 = Square(10, (1, 1))
        with self.assertRaises(TypeError):
            s19 = Square(10, {'k': 10})
        with self.assertRaises(TypeError):
            s20 = Square(10, 10.5)
        with self.assertRaises(TypeError):
            s21 = Square(10, True)

    def test_er_val_squa_x(self):
        """Test validator value x"""
        with self.assertRaises(ValueError):
            s22 = Square(10, -1)

    def test_er_type_squa_y(self):
        with self.assertRaises(TypeError):
            s1 = Square(10, 1, 'h')
        with self.assertRaises(TypeError):
            s1 = Square(10, 1, [1, 1])
        with self.assertRaises(TypeError):
            s1 = Square(10, 1, (1, 1))
        with self.assertRaises(TypeError):
            s1 = Square(10, 1, {'k': 10})
        with self.assertRaises(TypeError):
            s1 = Square(10, 1, 10.5)
        with self.assertRaises(TypeError):
            s1 = Square(10, 1, True)

    def test_er_val_squa_y(self):
        with self.assertRaises(ValueError):
            s1 = Square(10, 1, -1)

    def test_display_squa(self):
        s1 = Square(2)
        with patch('sys.stdout', new=StringIO()) as output:
            s1.display()
            self.assertEqual(output.getvalue().strip(), '##\n##')
        s2 = Square(3)
        with patch('sys.stdout', new=StringIO()) as output:
            s2.display()
            self.assertEqual(output.getvalue().strip(), '###\n###\n###')
        s3 = Square(2, 2, 2)
        with patch('sys.stdout', new=StringIO()) as output:
            s3.display()
            self.assertEqual(output.getvalue(), '\n\n  ##\n  ##\n')
        s4 = Square(3, 1)
        with patch('sys.stdout', new=StringIO()) as output:
            s4.display()
            self.assertEqual(output.getvalue(), ' ###\n ###\n ###\n')
        s5 = Square(3, 0, 2)
        with patch('sys.stdout', new=StringIO()) as output:
            s5.display()
            self.assertEqual(output.getvalue(), '\n\n###\n###\n###\n')

    def test_str_squa(self):
        """test __str__ method"""
        s1 = Square(4, 2, 1, 12)
        self.assertEqual(str(s1), "[Square] (12) 2/1 - 4")
        s2 = Square(5, 1, 0, 1)
        self.assertEqual(str(s2), "[Square] (1) 1/0 - 5")

    def test_update(self):
        s44 = Square(10, 10, 10, 1)
        s44.update(89)
        self.assertEqual(str(s44), "[Square] (89) 10/10 - 10")
        s44.update(89, 2)
        self.assertEqual(str(s44), "[Square] (89) 10/10 - 2")
        s44.update(89, 2, 4)
        self.assertEqual(str(s44), "[Square] (89) 4/10 - 2")
        s44.update(89, 2, 4, 5)
        self.assertEqual(str(s44), "[Square] (89) 4/5 - 2")
        s44.update(size=1)
        self.assertEqual(str(s44), "[Square] (89) 4/5 - 1")
        s44.update(size=1, x=2)
        self.assertEqual(str(s44), "[Square] (89) 2/5 - 1")
        s44.update(y=1, size=2, x=3, id=44)
        self.assertEqual(str(s44), "[Square] (44) 3/1 - 2")
        s44.update(45, 10, y=0, width=10, x=4, id=89)
        self.assertEqual(str(s44), "[Square] (45) 3/1 - 10")

        with self.assertRaises(TypeError):
            s44.update(89, 2, 'h', 5)
        with self.assertRaises(TypeError):
            s44.update(y=1, size='h', x=3, id=44)

    def test_to_dict_squa(self):
        s45 = Square(10, 2, 9, 1)
        s46 = Square(10, 10, 10, 10)
        s45_dictionary = s45.to_dictionary()
        self.assertTrue(type(s45_dictionary) is dict)
        self.assertIn('id', s45_dictionary)
        self.assertIn('size', s45_dictionary)
        self.assertIn('x', s45_dictionary)
        self.assertIn('y', s45_dictionary)
        self.assertEqual(s45_dictionary['id'], 1)
        self.assertEqual(s45_dictionary['size'], 10)
        self.assertEqual(s45_dictionary['x'], 2)
        self.assertEqual(s45_dictionary['y'], 9)
        self.assertEqual(len(s45_dictionary), 4)
        s46.update(**s45_dictionary)
        self.assertEqual(str(s46), "[Square] (1) 2/9 - 10")
        s46_dictionary = s46.to_dictionary()
        self.assertEqual(s45_dictionary, s46_dictionary)

if __name__ == '__main__':
    unittest.main()
