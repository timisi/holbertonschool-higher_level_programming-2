#!/usr/bin/python3
"""Unittest module for Rectangle class"""
import unittest
from unittest.mock import patch
from io import StringIO
from models.rectangle import Rectangle


class TestRectangleClass(unittest.TestCase):
    """TestRectangleClass class to test the Rectangle class"""

    def test_attr_rect(self):
        """test id creation"""
        rect_inst_1 = Rectangle(10, 2)
        rect_inst_2 = Rectangle(10, 2, 0, 0, 12)
        rect_inst_3 = Rectangle(11, 3, 0, 0, None)
        # getters
        self.assertEqual(rect_inst_1.width, 10)
        self.assertEqual(rect_inst_1.height, 2)
        self.assertEqual(rect_inst_2.width, 10)
        self.assertEqual(rect_inst_2.height, 2)
        self.assertEqual(rect_inst_2.x, 0)
        self.assertEqual(rect_inst_2.y, 0)
        self.assertEqual(rect_inst_2.id, 12)
        # setters
        rect_inst_3.width = 20
        self.assertEqual(rect_inst_3.width, 20)
        rect_inst_3.height = 20
        self.assertEqual(rect_inst_3.height, 20)
        rect_inst_3.x = 20
        self.assertEqual(rect_inst_3.x, 20)
        rect_inst_3.y = 20
        self.assertEqual(rect_inst_3.y, 20)
        rect_inst_3.id = 20
        self.assertEqual(rect_inst_3.id, 20)
        # Area method
        self.assertEqual(rect_inst_1.area(), 20)

    # Argument number errors
    def test_er_argum_rect(self):
        """Test Error + arguments"""
        with self.assertRaises(TypeError):
            r1 = Rectangle(10, 2, 0, 0, 12, 12)
        with self.assertRaises(TypeError):
            r1 = Rectangle()
        with self.assertRaises(TypeError):
            r1 = Rectangle(10)
        with self.assertRaises(TypeError):
            r1 = Rectangle(10, 2)
            r1.area(20)
        with self.assertRaises(TypeError):
            r1 = Rectangle(2, 2, 2, 2)
            r1.display(10)

    # width type
    def test_er_type_rect_width(self):
        """Test validator type width"""
        with self.assertRaises(TypeError):
            r1 = Rectangle('h', 10)
        with self.assertRaises(TypeError):
            r1 = Rectangle([1, 1], 10)
        with self.assertRaises(TypeError):
            r1 = Rectangle((1, 1), 10)
        with self.assertRaises(TypeError):
            r1 = Rectangle({'k': 10}, 10)
        with self.assertRaises(TypeError):
            r1 = Rectangle(10.5, 10)
        with self.assertRaises(TypeError):
            r1 = Rectangle(True, 10)

    # width value
    def test_er_val_rect_width(self):
        """Test validator value width"""
        with self.assertRaises(ValueError):
            r1 = Rectangle(-10, 10)
        with self.assertRaises(ValueError):
            r1 = Rectangle(0, 10)

    # height type
    def test_er_type_rect_height(self):
        """Test validator type height"""
        with self.assertRaises(TypeError):
            r1 = Rectangle(10, 'h')
        with self.assertRaises(TypeError):
            r1 = Rectangle(10, [1, 1])
        with self.assertRaises(TypeError):
            r1 = Rectangle(10, (1, 1))
        with self.assertRaises(TypeError):
            r1 = Rectangle(10, {'k': 10})
        with self.assertRaises(TypeError):
            r1 = Rectangle(10, 10.5)
        with self.assertRaises(TypeError):
            r1 = Rectangle(10, True)

    # height value
    def test_er_val_rect_height(self):
        """Test validator value height"""
        with self.assertRaises(ValueError):
            r1 = Rectangle(10, -10)
        with self.assertRaises(ValueError):
            r1 = Rectangle(10, 0)

    # x type
    def test_er_type_rect_x(self):
        """Test validator type x"""
        with self.assertRaises(TypeError):
            r1 = Rectangle(10, 10, 'h')
        with self.assertRaises(TypeError):
            r1 = Rectangle(10, 10, [1])
        with self.assertRaises(TypeError):
            r1 = Rectangle(10, 10, (1, 1))
        with self.assertRaises(TypeError):
            r1 = Rectangle(10, 10, {'k': 10})
        with self.assertRaises(TypeError):
            r1 = Rectangle(10, 10, 10.5)
        with self.assertRaises(TypeError):
            r1 = Rectangle(10, 10, True)

    # x value
    def test_er_val_rect_x(self):
        """Test validator value x"""
        with self.assertRaises(ValueError):
            r1 = Rectangle(10, 10, -1)

    # y type
    def test_er_type_rect_y(self):
        """Test validator type y"""
        with self.assertRaises(TypeError):
            r1 = Rectangle(10, 10, 1, 'h')
        with self.assertRaises(TypeError):
            r1 = Rectangle(10, 10, 1, [1, 1])
        with self.assertRaises(TypeError):
            r1 = Rectangle(10, 10, 1, (1, 1))
        with self.assertRaises(TypeError):
            r1 = Rectangle(10, 10, 1, {'k': 10})
        with self.assertRaises(TypeError):
            r1 = Rectangle(10, 10, 1, 10.5)
        with self.assertRaises(TypeError):
            r1 = Rectangle(10, 10, 1, True)

    # y value
    def test_er_val_rect_y(self):
        """Test validator value y"""
        with self.assertRaises(ValueError):
            r1 = Rectangle(10, 10, 1, -1)

    # display
    def test_display(self):
        """Test display method"""
        r1 = Rectangle(2, 2)
        with patch ('sys.stdout', new=StringIO()) as output:
            r1.display()
            self.assertEqual(output.getvalue().strip(), '##\n##')
        r2 = Rectangle(3, 2)
        with patch ('sys.stdout', new=StringIO()) as output:
            r2.display()
            self.assertEqual(output.getvalue().strip(), '###\n###')
        r3 = Rectangle(2, 3, 2, 2)
        with patch ('sys.stdout', new=StringIO()) as output:
            r3.display()
            self.assertEqual(output.getvalue(), '\n\n  ##\n  ##\n  ##\n')
        r4 = Rectangle(3, 2, 1)
        with patch ('sys.stdout', new=StringIO()) as output:
            r4.display()
            self.assertEqual(output.getvalue(), ' ###\n ###\n')
        r4 = Rectangle(3, 2, 0, 2)
        with patch ('sys.stdout', new=StringIO()) as output:
            r4.display()
            self.assertEqual(output.getvalue(), '\n\n###\n###\n')

    # __str__
    def test_str(self):
        """test __str__ method"""
        r1 = Rectangle(4, 6, 2, 1, 12)
        self.assertEqual(str(r1), "[Rectangle] (12) 2/1 - 4/6")
        r2 = Rectangle(5, 5, 1, 0, 1)
        self.assertEqual(str(r2), "[Rectangle] (1) 1/0 - 5/5")

    # update
    def test_update(self):
        """test update() method"""
        r44 = Rectangle(10, 10, 10, 10, 1)
        self.assertEqual(str(r44), "[Rectangle] (1) 10/10 - 10/10")
        r44.update(89)
        self.assertEqual(str(r44), "[Rectangle] (89) 10/10 - 10/10")
        r44.update(89, 2)
        self.assertEqual(str(r44), "[Rectangle] (89) 10/10 - 2/10")
        r44.update(89, 2, 3)
        self.assertEqual(str(r44), "[Rectangle] (89) 10/10 - 2/3")
        r44.update(89, 2, 3, 4)
        self.assertEqual(str(r44), "[Rectangle] (89) 4/10 - 2/3")
        r44.update(89, 2, 3, 4, 5)
        self.assertEqual(str(r44), "[Rectangle] (89) 4/5 - 2/3")
        r44.update(height=1)
        self.assertEqual(str(r44), "[Rectangle] (89) 4/5 - 2/1")
        r44.update(width=1, x=2)
        self.assertEqual(str(r44), "[Rectangle] (89) 2/5 - 1/1")
        r44.update(y=1, width=2, x=3, id=44)
        self.assertEqual(str(r44), "[Rectangle] (44) 3/1 - 2/1")
        r44.update(45, 10, y=0, width=10, x=4, id=89)
        self.assertEqual(str(r44), "[Rectangle] (45) 3/1 - 10/1")

        with self.assertRaises(TypeError):
            r44.update(89, 2, 3, 'h', 5)
        with self.assertRaises(TypeError):
            r44.update(89, 'h', 3, 2, 5)
        with self.assertRaises(TypeError):
            r44.update(y=1, width='h', x=3, id=44)

    # to dictionary
    def test_to_dict_rect(self):
        """test to_dictionary() method"""
        r45 = Rectangle(10, 2, 1, 9, 1)
        r45_dictionary = r45.to_dictionary()
        self.assertTrue(type(r45_dictionary) is dict)

if __name__ == '__main__':
    unittest.main()
