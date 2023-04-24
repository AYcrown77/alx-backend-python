#!/usr/bin/env python3
"""Unittesting """

import unittest
from unittest.mock import patch, PropertyMock
from client import GithubOrgClient
from parameterized import parameterized, parameterized_class
from fixtures import TEST_PAYLOAD
import requests


class TestGithubOrgClient(unittest.TestCase):
    """testing GithubOrgClient """

    @parameterized.expand([
        ("google"),
        ("abc"),
    ])
    @patch('client.get_json')
    def test_org(self, org_name, mock_json):
        """check the GithubClient org method """
        result = 'https://api.github.com/orgs/{}'.format(org_name)
        prop = GithubOrgClient(org_name)
        prop.org()
        mock_json.assert_called_once_with(result)
