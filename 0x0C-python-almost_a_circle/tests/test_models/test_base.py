#!/usr/bin/python3
"""Defines unittests for base.py."""

import os
import unittest
from models.base import Base


class TestBaseInstantiation(unittest.TestCase):
    """Unittests for testing instantiation of the Base class."""

    def test_no_arg(self):
        b1 = Base()
        b2 = Base()
        self.assertEqual(b1.id, b2.id - 1)

    def test_three_bases(self):
        b1 = Base()
        b3 = Base()
        self.assertEqual(b1.id, b3.id - 2)

    def test_None_id(self):
        b1 = Base(None)
        b2 = Base(None)
        self.assertEqual(b1.id, b2.id - 1)

    def test_unique_id(self):
        self.assertEqual(12, Base(12).id)

    def test_nb_instances_after_unique_id(self):
        b1 = Base()
        b3 = Base()
        self.assertEqual(b1.id, b3.id - 1)

    def test_id_public(self):
        b = Base(12)
        b.id = 15
        self.assertEqual(15, b.id)

    def test_nb_instances_private(self):
        with self.assertRaises(AttributeError):
            print(Base(12).__nb_objects)

    def test_str_id(self):
        self.assertEqual("hello", Base("hello").id)

    def test_float_id(self):
        self.assertEqual(5.5, Base(5.5).id)

    def test_complex_id(self):
        self.assertEqual(complex(5), Base(complex(5)).id)

    def test_dict_id(self):
        self.assertEqual({"a": 1, "b": 2}, Base({"a": 1, "b": 2}).id)

    def test_bool_id(self):
        self.assertEqual(True, Base(True).id)

    def test_list_id(self):
        self.assertEqual([1, 2, 3], Base([1, 2, 3]).id)

    def test_tuple_id(self):
        self.assertEqual((1, 2), Base((1, 2)).id)

    def test_set_id(self):
        self.assertEqual({1, 2, 3}, Base({1, 2, 3}).id)

    def test_frozenset_id(self):
        self.assertEqual(frozenset({1, 2, 3}), Base(frozenset({1, 2, 3})).id)

    def test_range_id(self):
        self.assertEqual(range(5), Base(range(5)).id)

    def test_bytes_id(self):
        self.assertEqual(b'Python', Base(b'Python').id)

    def test_bytearray_id(self):
        self.assertEqual(bytearray(b'abcefg'), Base(bytearray(b'abcefg')).id)

    def test_memoryview_id(self):
        self.assertEqual(memoryview(b'abcefg'), Base(memoryview(b'abcefg')).id)

    def test_inf_id(self):
        self.assertEqual(float('inf'), Base(float('inf')).id)

    def test_NaN_id(self):
        self.assertNotEqual(float('nan'), Base(float('nan')).id)

    def test_two_args(self):
        with self.assertRaises(TypeError):
            Base(1, 2)


class TestBaseToJsonString(unittest.TestCase):
    """Unittests for testing to_json_string method of Base class."""

    def test_to_json_string_empty_list(self):
        self.assertEqual("[]", Base.to_json_string([]))

    def test_to_json_string_none(self):
        self.assertEqual("[]", Base.to_json_string(None))

    def test_to_json_string_no_args(self):
        with self.assertRaises(TypeError):
            Base.to_json_string()

    def test_to_json_string_more_than_one_arg(self):
        with self.assertRaises(TypeError):
            Base.to_json_string([], 1)


class TestBaseSaveToFile(unittest.TestCase):
    """Unittests for testing save_to_file method of Base class."""

    @classmethod
    def tearDownClass(cls):
        """Delete any created files."""
        for cls_name in ["Rectangle", "Square", "Base"]:
            filename = f"{cls_name}.json"
            if os.path.exists(filename):
                os.remove(filename)

    def test_save_to_file_none(self):
        Base.save_to_file(None)
        with open("Base.json", "r") as f:
            self.assertEqual("[]", f.read())

    def test_save_to_file_empty_list(self):
        Base.save_to_file([])
        with open("Base.json", "r") as f:
            self.assertEqual("[]", f.read())


class TestBaseFromJsonString(unittest.TestCase):
    """Unittests for testing from_json_string method of Base class."""

    def test_from_json_string_none(self):
        self.assertEqual([], Base.from_json_string(None))

    def test_from_json_string_empty_list(self):
        self.assertEqual([], Base.from_json_string("[]"))

    def test_from_json_string_no_args(self):
        with self.assertRaises(TypeError):
            Base.from_json_string()

    def test_from_json_string_more_than_one_arg(self):
        with self.assertRaises(TypeError):
            Base.from_json_string([], 1)


class TestBaseCreate(unittest.TestCase):
    """Unittests for testing create method of Base class."""

    def test_create_none(self):
        self.assertIsNone(Base.create())

    def test_create_empty_dict(self):
        self.assertIsNone(Base.create({}))


class TestBaseLoadFromFile(unittest.TestCase):
    """Unittests for testing load_from_file method of Base class."""

    def test_load_from_file_none(self):
        self.assertEqual([], Base.load_from_file())

    def test_load_from_file_no_file(self):
        self.assertEqual([], Base.load_from_file())


class TestBaseSaveToFileCSV(unittest.TestCase):
    """Unittests for testing save_to_file_csv method of Base class."""

    @classmethod
    def tearDownClass(cls):
        """Delete any created files."""
        for cls_name in ["Rectangle", "Square", "Base"]:
            filename = f"{cls_name}.csv"
            if os.path.exists(filename):
                os.remove(filename)

    def test_save_to_file_csv_none(self):
        Base.save_to_file_csv(None)
        with open("Base.csv", "r") as f:
            self.assertEqual("[]", f.read())

    def test_save_to_file_csv_empty_list(self):
        Base.save_to_file_csv([])
        with open("Base.csv", "r") as f:
            self.assertEqual("[]", f.read())


class TestBaseLoadFromFileCSV(unittest.TestCase):
    """Unittests for testing load_from_file_csv method of Base class."""

    def test_load_from_file_csv_none(self):
        self.assertEqual([], Base.load_from_file_csv())

    def test_load_from_file_csv_no_file(self):
        self.assertEqual([], Base.load_from_file_csv())


if __name__ == "__main__":
    unittest.main()
