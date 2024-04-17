#!/usr/bin/python3
"""loads content from a json file"""
import json


def load_from_json_file(filename):
    """creates an object fom a JSON file"""
    with open(filename) as file:
        json.load(file)
