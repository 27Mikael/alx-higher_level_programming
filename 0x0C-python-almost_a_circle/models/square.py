#!/usr/bin/python3
from models.rectangle import Rectangle
"""Defines a rectangle"""


class Square(Rectangle):
    """Represents a square"""

    def __init__(self, size, x=0, y=0, id=None):
        """
        Initializes the rectangle

        Args:
            size (int): The size of the new Square.
            x (int): The x coordinate of the new Square.
            y (int): The y coordinate of the new Square.
            id (int): The identity of the new Square.

        """
        super.__init__(size, size, x, y, id)

    @property
    def size(self):
        """ Get/set the size of the Square"""
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """Update the Square

        Args:
            *args (int): new attribute values.
                - 1st argument represents id attribute
                - 2nd argument represents size attribute
                - 3th argument represents x attribute
                - 4th argument represents y attribute
            **kwargs (dict): New key/value pairs of attributes.
        """
        if args:
            attributes = ['id', 'size', 'x', 'y']
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
            "size": self.width,
            "x": self.x,
            "y": self.y
        }

    def __str__(self):
        """Overrides default string to return string rep class"""
        return "[Square] ({}) {}/{} - {}".format(
            self.id, self.x, self.y, self.width)
