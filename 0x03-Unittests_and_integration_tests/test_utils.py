#!/usr/bin/env python3
"""Testing module for utils"""

import unittest
from utils import access_nested_map, get_json, memoize
from parameterized import parameterized
from unittest.mock import Mock, patch


class TestAccessNestedMap(unittest.TestCase):
    """test access_nested_map()"""
    @parameterized.expand([
        nested_map={"a": 1}, path=("a",)
        nested_map={"a": {"b": 2}}, path=("a",)
        nested_map={"a": {"b": 2}}, path=("a", "b")
    ])
    def test_access_nested_map(self, map, path, expected):
        """test access_nested_map return value"""
        self.assertEqual(access_nested_map(map, path), expected)
