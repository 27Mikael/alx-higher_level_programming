#!/usr/bin/python3
"""Appends string at the end of the function."""


def append_write(filename="", text=""):
    """
    function append string to the file

    Args:
        filename (str): name of file
        text (str): string to append

    Returns:
        Number of characters added.
    """
    with open(filename, mode='a', encoding='utf-8') as file:
        num_of_chars_written = file.write(text)
    return num_of_chars_written
