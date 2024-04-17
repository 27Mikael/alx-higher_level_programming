#!/usr/bin/python3
"""Defines a function that returns a list of attribute methods"""


def lookup(obj):
    """Function looks up attributes of obj"""
    print(dir(obj))
