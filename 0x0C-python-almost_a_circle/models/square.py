#!/usr/bin/python3
""" class square """
from models.rectangle import Rectangle


class Square(Rectangle):
    """class Square inheret from Rectangle"""
    def __init__(self, size, x=0, y=0, id=None):
        """constractor for square"""
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """Get/set the size of the Square."""
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value
    def __str__(self):
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y, self.width)

    def update(self, *args, **kwargs):
        """ args and kwargs """
        if args:
            if len (args) >= 1:
                self.id = args[0]
            if len (args) >= 2:
                self.size = args[1]
            if len (args) >= 3:
                self.x = args[2]
            if len (args) >= 4:
                self.y = args[3]
            
        else:
            for key, value in kwargs.items():
                if key == 'id':
                    self.id = value
                elif key == 'size':
                    self.size = value
                elif key == 'x':
                    self.x = value
                elif key == 'y':
                    self.y = value
    def to_dictionary(self):
        """ representation of square"""
        return {
            'id': self.id,
            'x': self.x,
            'size': self.width,
            'y': self.y
        }
