#!/usr/bin/python3
"""Sorts lists in ascending order."""


class MyList(list):
    """A subclass of list """

    def __init__(self):
        """initializes the object"""
        super().__init__()

    def print_sorted(self):
        """prints sorted lists in ascending order."""
        print(sorted(self))
