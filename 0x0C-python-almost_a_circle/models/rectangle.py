#!/usr/bin/python3
from models.base import Base
"""Defines a rectangle"""


class Rectangle(Base):
    """Represents a rectangle"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Initializes the Rectangle

        Args:
            width: width of rectangle
            height: height of rectangle
            x: x-coordinate of the rectangle
            y: y-coordinate of the rectangle

        Raises:
            TypeError: if width or length are not intergers
            ValueError: if width or length are <= 0
            TypeError: if x or y are not intergers
            ValueError: if x or y are <= 0
        """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super.__init__(id)

    @property
    def width(self):
        """set/get rectangle width"""
        return self.__width

    @width.setter
    def width(self, value):
        if value is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")

    @property
    def height(self):
        """set/get rectangle height"""
        return self.__height

    @height.setter
    def height(self, value):
        if value is not int:
            raise TypeError("height must be an interger")
        if value <= 0:
            raise ValueError("height must be > 0")

    @property
    def x(self):
        """set/get the x-coordinate"""
        return self.__x

    @x.setter
    def x(self, value):
        if value is not int:
            raise TypeError("x must be an interger")
        if value < 0:
            raise ValueError("x must be >= 0")

    @property
    def y(self):
        """set/get the y-coordinate"""
        return self.__y

    @y.setter
    def y(self, value):
        if value is not int:
            raise TypeError("y must be an interger")
        if value < 0:
            raise ValueError("y must be >= 0")

    def area(self):
        """Returns the area of the rectangle"""
        return self.width * self.height

    def display(self):
        """Displays the rectangle"""
        if self.width == 0 or self.height == 0:
            print("")

        for _ in range(self.y):
            for _ in range(self.height):
                print(" " * self.x, end="")
                print("#" * self.width)

    def update(self, *args, **kwargs):
        """Update the Rectangle

        Args:
            *args (int): new attribute values.
                - 1st argument represents id attribute
                - 2nd argument represents width attribute
                - 3rd argument represent height attribute
                - 4th argument represents x attribute
                - 5th argument represents y attribute
            **kwargs (dict): New key/value pairs of attributes.
        """
        if args:
            attributes = ['id', 'width', 'height', 'x', 'y']
            for i, arg in enumerate(args):
                if i < len(attributes):
                    setattr(self, attributes[i], arg)

        elif kwargs:
            for key, value in kwargs.items():
                setattr(self, key, value)

        else:
            print("No arguments provided")

    def to_dictionary(self):
        """ Returns a dict representation of rectangle"""
        return {
            "id": self.id,
            "width": self.width,
            "height": self.height,
            "x": self.x,
            "y": self.y
        }

    def __str__(self):
        """Overrides default string to return string rep class"""
        return "[Rectangle] ({}) {}/{} - {}{}".format(
            self.id, self.x, self.y, self.width, self.height)
