#!/usr/bin/python3
"""Defines class Student"""


class Student:
    """defines a student"""

    def __init__(self, first_name, last_name, age):
        """
        instantiates student object

        Args:
            first_name: student name
            last_name: students surname
            age: age of student
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        retrives attribute names in a list
        ""
        Args:
            attrs: list to retrive names from

        Returns:
            dict representation of the Student instance
        """
        if (isinstance(attrs, list)
                and all(isinstance(ele, str) for ele in attrs)):
            return {k: getattr(self, k) for k in attrs if hasattr(self, k)}
        return self.__dict__

    def reload_from_json(self, json):
        """Replace all attributes of the student

        Args:
            json (dict): the key/value pairs to replace attributes with.
        """
        for k, v in json.items():
            setattr(self, k, v)
