#!/usr/bin/python3

""" Define a square"""


class Square:
    """Repressent a Square"""
    def __init__(self, size) -> None:
        """Initialise a new square

        Args:
            size (int): The size of the new square
        """
        self.__size = size
