#!/usr/bin/python3
"""Unittest module for Rectangle class"""

import unittest
from unittest.mock import patch
from io import StringIO
from models.rectangle import Rectangle


class TestRectangleClass(unittest.TestCase):
    """TestRectangleClass class to test the Rectangle class"""

    def test_attr_rect(self):
        rect_inst_1 = Rectangle(10, 2)
        rect_inst_2 = Rectangle(10, 2, 0, 0, 12)
        rect_inst_3 = Rectangle(11, 3, 0, 0, None)
        self.assertEqual(rect_inst_1.width, 10)
        self.assertEqual(rect_inst_1.height, 2)
        self.assertEqual(rect_inst_2.width, 10)
        self.assertEqual(rect_inst_2.height, 2)
        self.assertEqual(rect_inst_2.x, 0)
        self.assertEqual(rect_inst_2.y, 0)
        self.assertEqual(rect_inst_2.id, 12)
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
        self.assertEqual(rect_inst_1.area(), 20)

    def test_er_argum_rect(self):
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
        with self.assertRaises(TypeError):
            r1 = Rectangle(2, 2, 2, 2)
            r1.to_dictionary(10)

    def test_er_type_rect_width(self):
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

    def test_er_val_rect_width(self):
        with self.assertRaises(ValueError):
            r1 = Rectangle(-10, 10)
        with self.assertRaises(ValueError):
            r1 = Rectangle(0, 10)

    def test_er_type_rect_height(self):
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

    def test_er_val_rect_height(self):
        with self.assertRaises(ValueError):
            r1 = Rectangle(10, -10)
        with self.assertRaises(ValueError):
            r1 = Rectangle(10, 0)

    def test_er_type_rect_x(self):
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

    def test_er_val_rect_x(self):
        with self.assertRaises(ValueError):
            r1 = Rectangle(10, 10, -1)

    def test_er_type_rect_y(self):
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

    def test_er_val_rect_y(self):
        with self.assertRaises(ValueError):
            r1 = Rectangle(10, 10, 1, -1)

    def test_display(self):
        r1 = Rectangle(2, 2)
        with patch('sys.stdout', new=StringIO()) as output:
            r1.display()
            self.assertEqual(output.getvalue().strip(), '##\n##')
        r2 = Rectangle(3, 2)
        with patch('sys.stdout', new=StringIO()) as output:
            r2.display()
            self.assertEqual(output.getvalue().strip(), '###\n###')
        r3 = Rectangle(2, 3, 2, 2)
        with patch('sys.stdout', new=StringIO()) as output:
            r3.display()
            self.assertEqual(output.getvalue(), '\n\n  ##\n  ##\n  ##\n')
        r4 = Rectangle(3, 2, 1)
        with patch('sys.stdout', new=StringIO()) as output:
            r4.display()
            self.assertEqual(output.getvalue(), ' ###\n ###\n')
        r4 = Rectangle(3, 2, 0, 2)
        with patch('sys.stdout', new=StringIO()) as output:
            r4.display()
            self.assertEqual(output.getvalue(), '\n\n###\n###\n')

    def test_str(self):
        r1 = Rectangle(4, 6, 2, 1, 12)
        self.assertEqual(str(r1), "[Rectangle] (12) 2/1 - 4/6")
        r2 = Rectangle(5, 5, 1, 0, 1)
        self.assertEqual(str(r2), "[Rectangle] (1) 1/0 - 5/5")

    def test_update(self):
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

    def test_to_dict_rect(self):
        r45 = Rectangle(10, 2, 1, 9, 1)
        r46 = Rectangle(11, 10, 10, 10, 10)
        r45_dictionary = r45.to_dictionary()
        self.assertTrue(type(r45_dictionary) is dict)
        self.assertIn('id', r45_dictionary)
        self.assertIn('width', r45_dictionary)
        self.assertIn('height', r45_dictionary)
        self.assertIn('x', r45_dictionary)
        self.assertIn('y', r45_dictionary)
        self.assertEqual(r45_dictionary['id'], 1)
        self.assertEqual(r45_dictionary['width'], 10)
        self.assertEqual(r45_dictionary['height'], 2)
        self.assertEqual(r45_dictionary['x'], 1)
        self.assertEqual(r45_dictionary['y'], 9)
        self.assertEqual(len(r45_dictionary), 5)
        r46.update(**r45_dictionary)
        self.assertEqual(str(r46), "[Rectangle] (1) 1/9 - 10/2")
        r46_dictionary = r46.to_dictionary()
        self.assertEqual(r45_dictionary, r46_dictionary)

if __name__ == '__main__':
    unittest.main()
