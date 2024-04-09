#!/usr/bin/python3
"""Defines a Rectangle class."""


class Rectangle():
    """Represent a rectangle.

    Attributes:
        number_of_instances (int): The number of Rectangle instances.
        print_symbol (any): The symbol used for string representation.
    """

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0) -> None:
        """Initialize a new Rectangle.

        Args:
            width (int): The width of the new rectangle
            height (int): The height of the new rectangle
        """
        type(self).number_of_instances += 1  # type: ignore
        self.height = height
        self.width = width

    @property
    def width(self) -> int:
        """Get/set the width of the rectanlge"""
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self) -> int:
        """get/set the height of the rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must integer")
        if value < 0:
            raise ValueError("height must >= 0")
        self.__height = value

    def perimeter(self) -> int:
        """Return the perimeter of the rectangle"""
        if self.__height == 0 or self.__width == 0:
            return (0)
        return ((self.__height * 2) + (self.__width))

    def area(self) -> int:
        """Return the area of the area of the rectangle"""
        return (self.__height * self.__width)

    def __str__(self) -> str:
        """Return the printable representaiton of the rectangle

        Represents the rectangle with the # character
        """
        if self.__width == 0 or self.__height == 0:
            return ("")
        return '\n'.join([self.print_symbol*self.__width]*self.__height)

    def __repr__(self) -> str:
        """Return the a representation that allows recreation."""
        return f"Rectangle({self.__width}, {self.__height})"

    def __del__(self):
        """ Prints "Bye Rectangle..." when instance is deleted"""
        type(self).number_of_instances -= 1
        print("Bye Rectangle...")

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """Return the Rectanlge with the bigger area.

        Args:
            rect_1 (Rectangle): first rectangle
            rect_2 (Rectangle): second rectangle
        Raises:
            TypeError: if neither rectangle is not Rectangle
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return (rect_1)
        return (rect_2)

    @classmethod
    def square(cls, size=0):
        """Create a squae REctangle with equal width and height"""
        return cls(size, size)