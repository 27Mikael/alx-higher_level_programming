#!/usr/bin/python3
"""determines whether the object is an instance of
    a class inherited from a specified class otherwise false
"""


def is_kind_of_class(obj, a_class):
    """
    determines if is kind of class

    Args:
        obj: object we are checking
        a_class: class we are checking against

    Returns:
        True if object isinstance, false if not
    """
    if isinstance(obj, a_class):
        return True
    return False
