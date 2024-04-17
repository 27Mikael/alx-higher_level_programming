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

    def to_json(self):
        """ Get dictionary representation of the student"""
        return self.__dict__
