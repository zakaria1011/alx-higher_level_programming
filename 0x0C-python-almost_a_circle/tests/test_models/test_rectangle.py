#!/usr/bin/python3
""" unittest for rectangle """

import unittest
from models.rectangle import Rectangle
from io import StringIO
import sys


class TestRectangle(unittest.TestCase):

    def setUp(self):
        """set __nb_objects """
        Rectangle._Rectangle__nb_objects = 0

    def test_constructor(self):
        r = Rectangle(5, 10, 0, 0, 1)
        self.assertEqual(r.width, 5)
        self.assertEqual(r.height, 10)
        self.assertEqual(r.x, 0)
        self.assertEqual(r.y, 0)
        self.assertEqual(r.id, 1)

    def test_width_property(self):
        """ test width attribute """
        r = Rectangle(5, 10)
        r.width = 20
        self.assertEqual(r.width, 20)
        with self.assertRaises(TypeError):
            r.width = "string"
        with self.assertRaises(ValueError):
            r.width = -5

    def test_height_property(self):
        """ test height attributs """
        r = Rectangle(5, 10)
        r.height = 20
        self.assertEqual(r.height, 20)

        with self.assertRaises(TypeError):
            r.height = "string"
        with self.assertRaises(ValueError):
            r.height = -5

    def test_x_property(self):
        """ test x attributs """
        r = Rectangle(5, 10)
        r.x = 20
        self.assertEqual(r.x, 20)

        with self.assertRaises(TypeError):
            r.x = "string"
        with self.assertRaises(ValueError):
            r.x = -5

    def test_y_property(self):
        """ test y attribute """
        r = Rectangle(5, 10)
        r.y = 20
        self.assertEqual(r.y, 20)

        with self.assertRaises(TypeError):
            r.y = "string"
        with self.assertRaises(ValueError):
            r.y = -5

    def test_area(self):
        """ test area methode """
        r = Rectangle(5, 5)
        A = r.area()
        self.assertEqual(A, 25)

    def test_display(self):
        """ test display methode """
        captured_output = StringIO()
        sys.stdout = captured_output
        rect = Rectangle(2, 3, 1, 1)
        rect.display()
        sys.stdout = sys.__stdout__
        output = captured_output.getvalue()
        expected_output = "\n ##\n ##\n ##\n"
        self.assertEqual(output, expected_output)

    def test_str(self):
        """ test str methode """
        r = Rectangle(5, 10, 2, 2, 7)
        self.assertEqual(str(r), "[Rectangle] (7) 2/2 - 5/10")

    def test_update(self):
        """test update methode """
        r = Rectangle(1, 2, 3, 4, 5)
        r.update(5, 4, 3, 2, 1)
        self.assertEqual(r.id, 5)
        self.assertEqual(r.width, 4)
        self.assertEqual(r.height, 3)
        self.assertEqual(r.x, 2)
        self.assertEqual(r.y, 1)

        r.update(height=10, y=7)
        self.assertEqual(r.height, 10)
        self.assertEqual(r.y, 7)

    def test_to_dictionary(self):
        """ test methode to dictionary """
        r = Rectangle(1, 2, 3, 4, 5)
        dic = r.to_dictionary()
        self.assertEqual(dic, {
            'x': 3,
            'y': 4,
            'id': 5,
            'width': 1,
            'height': 2
        })

    def test_doc_strings(self):
        """ test doc string """
        self.assertIsNotNone(Rectangle.__doc__, True)
        self.assertIsNotNone(Rectangle.__init__.__doc__, True)
        self.assertIsNotNone(Rectangle.width.__doc__, True)
        self.assertIsNotNone(Rectangle.height.__doc__, True)
        self.assertIsNotNone(Rectangle.x.__doc__, True)
        self.assertIsNotNone(Rectangle.y.__doc__, True)
        self.assertIsNotNone(Rectangle.area.__doc__, True)
        self.assertIsNotNone(Rectangle.display.__doc__, True)
        self.assertIsNotNone(Rectangle.__str__.__doc__, True)
        self.assertIsNotNone(Rectangle.update.__doc__, True)
        self.assertIsNotNone(Rectangle.to_dictionary.__doc__, True)


if __name__ == '__main__':
    unittest.main()
