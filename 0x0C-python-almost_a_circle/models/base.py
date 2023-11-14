#!/usr/bin/python3

"""class base"""
import json


class Base:
    """ class base """
    __nb_objects = 0

    def __init__(self, id=None):
        """ constractor """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """ from dic to json"""
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """save to file  """
        if list_objs is None:
            list_objs = []

        filename = "{}.json".format(cls.__name__)
        data_list = [obj.to_dictionary() for obj in list_objs]
        json_str = cls.to_json_string(data_list)
        with open(filename, 'w') as file:
            file.write(json_str)

    @staticmethod
    def from_json_string(json_string):
        """from json string"""
        if json_string is None or json_string == "":
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """creat dic"""
        dummy = None
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)
        elif cls.__name__ == "Square":
            dummy = cls(1)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """load from file"""
        filename = "{}.json".format(cls.__name__)
        try:
            with open(filename, 'r') as file:
                json_str = file.read()
                data = cls.from_json_string(json_str)
                instances = [cls.create(**entry) for entry in data]
                return instances
        except FileNotFoundError:
            return []
