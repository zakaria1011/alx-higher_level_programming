#!/usr/bin/python3
""" class rectangle """
from models.base import Base


class Rectangle(Base):
    """ class rectangle """
    def __init__(self, width, height, x=0, y=0, id=None):
        """ constractore """
        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        if width <= 0:
            raise ValueError("width must be > 0")
        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        if height <= 0:
            raise ValueError("height must be > 0")
        if not isinstance(x, int):
            raise TypeError("x must be an integer")
        if x < 0:
            raise ValueError("x must be >= 0")
        if not isinstance(y, int):
            raise TypeError("y must be an integer")
        if y < 0:
            raise ValueError("y must be >= 0")
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y
        super().__init__(id)

    @property
    def width(self):
        """ retrieve width """
        return self.__width

    @width.setter
    def width(self, value):
        """ controle the type of value """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """ retrieve height """
        return self.__height

    @height.setter
    def height(self, value):
        """ controle the type of value """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """ retrieve x """
        return self.__x

    @x.setter
    def x(self, value):
        """ controle the type of value """
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """ retrieve y """
        return self.__y

    @y.setter
    def y(self, value):
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        """ controle the type of value """
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """ return area of rectangle"""
        return self.__height * self.__width

    def display(self):
        """ display rectangle """
        for _ in range(self.y):
            print()
        for _ in range(self.height):
            print(" " * self.x + "#" * self.width)

    def __str__(self):
        """ return a string discription for a rectangle """
        return (
            "[Rectangle] ({}) {}/{} - {}/{}"
            .format(self.id, self.x, self.y, self.width, self.height)
        )

    def update(self, *args, **kwargs):
        """ update attribute """
        if args:
            if len(args) >= 1:
                self.id = args[0]
            if len(args) >= 2:
                self.width = args[1]
            if len(args) >= 3:
                self.height = args[2]
            if len(args) >= 4:
                self.x = args[3]
            if len(args) >= 5:
                self.y = args[4]
        else:
            for key, value in kwargs.items():
                if key == 'id':
                    self.id = value
                elif key == 'width':
                    self.width = value
                elif key == 'height':
                    self.height = value
                elif key == 'x':
                    self.x = value
                elif key == 'y':
                    self.y = value

    def to_dictionary(self):
        """Return the dictionary representation of a Rectangle."""
        return {
            "x": self.x,
            "y": self.y,
            "id": self.id,
            "height": self.height,
            "width": self.width
        }
