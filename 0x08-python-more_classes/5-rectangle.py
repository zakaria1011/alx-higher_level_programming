#!/usr/bin/python3

""" class define rectangle """


class Rectangle:
    """ class triangle """
    def __init__(self, width=0, height=0):
        """
        initiate a rectangle

        Args:
        width (int): first arg
        height(int): seconde arg
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """ getter """
        return self.__width

    @width.setter
    def width(self, value):
        """ setter """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """ getter """
        return self.__height

    @height.setter
    def height(self, value):
        """ setter """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """ return area of rectangle """
        return self.__height * self.__width

    def perimeter(self):
        """ return perimeter of rectangle """
        if self.__height == 0 or self.__width == 0:
            return 0
        return 2 * (self.__height + self.__width)

    def __str__(self):
        """ print rectangle with # """
        str = []
        for i in range(self.__height):
            for j in range(self.__width):
                str.append('#')
                if j == self.__width - 1 and i != self.__height - 1:
                    str.append('\n')
        result = ''.join(str)
        return result

    def __repr__(self):
        """eturn a string representation of the rectangle to be able
         to recreate a new instance by using eval()
         """
        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self):
        """ distroctor of rectangle) """
        print("Bye rectangle...")
