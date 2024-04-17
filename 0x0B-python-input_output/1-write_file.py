#!/usr/bin/python3
"""Prints string to the file and returns number of characters printed"""


def write_file(filename="", text=""):
    """
    function prints string to a file

    Args:
        filename(string): file it writes to
        text (string): string it prints

    Returns:
        number of characters printed
    """
    with open(filename, mode='w', encoding='utf-8') as file:
        num_chars_written = file.write(text)
    return num_chars_written
