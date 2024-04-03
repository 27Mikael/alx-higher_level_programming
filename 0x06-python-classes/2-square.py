#!/usr/bin/python3

""" Define a square"""


class Square:
    """Repressent a Square"""
    def __init__(self, size=0) -> None:
        """Initialise a new square

        Args:
            size (int): The size of the new square
        """
        if not isinstance(size, int):
            raise TypeError("size must be an interger")
        if size < 0:
            raise ValueError("size must be >=0")
        self.__size = size
