#!/usr/bin/env python3
"""Testing utils.access_nested_map method"""

import unittest
from utils import access_nested_map, get_json, memoize
from parameterized import parameterized
from unittest.mock import Mock, patch


class TestAccessNestedMap(unittest.TestCase):
    """test access_nested_map()"""
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {'b': 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(self, map, path, expected):
        """method to test access_nested_map return value"""
        self.assertEqual(access_nested_map(map, path), expected)

    @parameterized.expand([
        ({}, ("a",), KeyError),
        ({"a": 1}, ("a", "b"), KeyError)
    ])
    def test_access_nested_map_exception(self, map, path, expected):
        """check for key error"""
        with self.assertRaises(KeyError) as e:
            self.assertEqual(access_nested_map(map, path), e.exception)


class TestGetJson(unittest.TestCase):
    """test get_json()"""
    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False})
    ])
    def test_get_json(self, test_url, test_payload):
        """test get_json()"""
        mock_resp = Mock()
        mock_resp.json.return_value = test_payload
        with patch('requests.get', return_value=mock_resp):
            real_resp = get_json(test_url)
            self.assertEqual(real_resp, test_payload)
            mock_resp.json.assert_called_once()
