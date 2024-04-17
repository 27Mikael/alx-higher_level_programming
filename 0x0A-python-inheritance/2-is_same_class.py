#!/usr/bin/python3
"""Checks if obj isinstance of a_class"""


def is_same_class(obj, a_class):
    """
    Checks if an obj is an instance of a class

    Args:
        obj: obj to check
        a_class: class to check

    Returns:
        bool: True if issubclass, False if not
    """
    return isinstance(obj, a_class)
