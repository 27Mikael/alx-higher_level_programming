#!/usr/bin/python3
"""save to json"""
import json


def save_to_json_file(my_obj, filename):
    """
    save my_obj to filename

    Args:
        my_obj: obj to save
        filename: file to write in
    """
    with open(filename, mode='w', encoding='utf-8') as file:
        json.dump(my_obj, file)
