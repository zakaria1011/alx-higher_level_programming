#!/usr/bin/python3
""" unittest for base """

import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestBase(unittest.TestCase):
    """ Test cases """

    def setUp(self):
        """set __nb_objects """
        Base._Base__nb_objects = 0

    def test_initial_id(self):
        """itiation empty """
        obj1 = Base()
        self.assertEqual(obj1.id, 1)

    def test_costum_id(self):
        """initiation with num"""
        obj2 = Base(7)
        self.assertEqual(obj2.id, 7)

    def test_increment_id(self):
        """incrementation"""
        obj3 = Base()
        obj4 = Base()
        obj5 = Base(12)
        self.assertEqual(obj3.id, 1)
        self.assertEqual(obj4.id, 2)
        self.assertEqual(obj5.id, 12)

    def test_doc_strings(self):
        """ test doc string """
        self.assertIsNotNone(Base.__doc__, True)
        self.assertIsNotNone(Base.__init__.__doc__, True)
        self.assertIsNotNone(Base.to_json_string.__doc__, True)
        self.assertIsNotNone(Base.save_to_file.__doc__, True)
        self.assertIsNotNone(Base.from_json_string.__doc__, True)
        self.assertIsNotNone(Base.create.__doc__, True)
        self.assertIsNotNone(Base.load_from_file.__doc__, True)

    def test_to_json_empty_list(self):
        """ test to_json_string with empty list"""
        json_str = Base.to_json_string([])
        self.assertEqual(json_str, "[]")

    def test_to_json_non_empty_list(self):
        """ test to_json_string with non empty list """
        json_str = ('[{"id": 1, "name": "Object 1"}, '
                    '{"id": 2, "name": "Object 2"}]')
        data = Base.from_json_string(json_str)
        self.assertEqual(data, [
            {'id': 1, 'name': 'Object 1'},
            {'id': 2, 'name': 'Object 2'}
        ])

    def test_save_to_file(self):
        """ test save to file """
        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(2, 4)
        Rectangle.save_to_file([r1, r2])
        with open("Rectangle.json", "r") as file:
            json_str = file.read()
        self.assertEqual(
            json_str,
            '[{"x": 2, "y": 8, "id": 1, "height": 7, "width": 10}, '
            '{"x": 0, "y": 0, "id": 2, "height": 4, "width": 2}]'
        )

    def test_from_json_string_empty_string(self):
        """ from json string empty string """
        data = Base.from_json_string("")
        self.assertEqual(data, [])

    def test_from_json_string_non_empty_string(self):
        """ from json string non empty """
        list_input = [
            {'id': 89, 'width': 10, 'height': 4},
            {'id': 7, 'width': 1, 'height': 7}
        ]
        json_list_input = Rectangle.to_json_string(list_input)
        list_output = Rectangle.from_json_string(json_list_input)
        self.assertEqual(
            list_output,
            [{'height': 4, 'width': 10, 'id': 89},
                {'height': 7, 'width': 1, 'id': 7}]
        )

    def test_create_square(self):
        data = {'id': 1, 'size': 5}
        obj = Square.create(**data)
        self.assertIsInstance(obj, Square)
        self.assertEqual(obj.id, 1)
        self.assertEqual(obj.size, 5)

    def test_load_from_file_non_exist_file(self):
        self.assertEqual(Base.load_from_file(), [])


if __name__ == '__main__':
    unittest.main()
