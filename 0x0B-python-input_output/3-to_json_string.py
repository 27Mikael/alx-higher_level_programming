#!/usr/bin/python3
"""Returns the json representation of a string"""
import json


def to_json_string(my_obj):
    """
    function returns the JSON representation of a string

    Args:
        my_obj: the objct whose JSON rep will be returned

    Returns:
        objects JSON rep
    """
    return json.dumps(my_obj)
