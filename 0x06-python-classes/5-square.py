#!/usr/bin/python3

""" Define a square"""


class Square:
    def __init__(self, size=0) -> None:
        """Initialise a new square.

        Args:
            size (int): The size of the new square.
        """
        self.size = size

    @property
    def size(self):
        """get the current size of Square."""
        return (self.__size)

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an interger")
        if value < 0:
            raise ValueError("size must be >=0")
        self.__size = value

    def area(self):
        """" Return the area of the Square"""
        return (self.__size*self.__size)

    def my_print(self):
        """Print the Square with the # character."""
        if (self.__size == 0):
            print("")
            return
        for i in range(0, self.__size):
            print("#"*self.__size)
