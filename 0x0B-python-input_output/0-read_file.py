#!/usr/bin/python3
"""Reads a text file in UTF8 format"""


def read_file(filename=""):
    """
    Function reads filename

    Args:
        filename: the name of the file

    Returns:
        prints it to the stdout
    """
    with open(filename, encode="utf-8") as file:
        for line in file:
            print(line, end='')
