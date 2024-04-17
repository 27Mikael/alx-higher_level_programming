#!/usr/bin/python3
"""Code that returns an object represented by a JSON string"""
import json


def from_json_string(my_str):
    """
    returns a string object from a json file

    Args:
        my_str: string to return

    Returns:
        string from json
    """
    return json.loads(my_str)
