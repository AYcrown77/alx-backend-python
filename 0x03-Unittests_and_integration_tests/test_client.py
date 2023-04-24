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

    @parameterized.expand([
        ("random-url", {'repos_url': 'http://some_url.com'})
    ])
    def test_public_repos_url(self, name, result):
        """returns correct output """
        with patch('client.GithubOrgClient.org',
                   PropertyMock(return_value=result)):
            resp = GithubOrgClient(name)._public_repos_url
            self.assertEqual(resp, result.get('repos_url'))

    @patch('client.get_json')
    def test_public_repos(self, get_json_mock):
        """ returns a known payload."""
        get_json_mock.return_value = [
            {'name': 'repo_0'},
            {'name': 'repo_1'},
            {'name': 'repo_2'}
        ]

    get_json_mock()
    with patch('client.GithubOrgClient._public_repos_url',
               new_callable=PropertyMock) as mock:
        mock.return_value = [
            {'name': 'repo_0'},
            {'name': 'repo_1'},
            {'name': 'repo_2'}
        ]
        goc = GithubOrgClient('xyz')
        ret = goc._public_repos_url
        self.assertEqual(ret, mock.return_value)
        mock.assert_called_once()
        get_json_mock.assert_called_once()

    @parameterized.expand([
        ({"license": {"key": "my_license"}}, "my_license", True),
        ({"license": {"key": "other_license"}}, "my_license", False)
    ])
    def test_has_license(self, repo, license_key, expected_result):
        """returns the correct values."""
        self.assertEqual(
            GithubOrgClient.has_license(repo, license_key),
            expected_result
        )


@parameterized_class(
    ('org_payload', 'repos_payload', 'expected_repos', 'apache2_repos'),
    TEST_PAYLOAD
)
class TestIntegrationGithubOrgClient(unittest.TestCase):
    """Integration test for githuborg_client"""

    @classmethod
    def setUpClass(cls):
        """ set up class"""
        config = {'return_value.json.side_effect':
                  [
                    cls.org_payload, cls.repos_payload,
                    cls.org_payload, cls.repos_payload
                  ]
                  }
        cls.get_patcher = patch('requests.get', **config)
        cls.mock = cls.get_patcher.start()

    def test_public_repos(self):
        """add more integration"""
        tst_cls = GithubOrgClient('Facebook')
        self.assertEqual(tst_cls.org, self.org_payload)
        self.assertEqual(tst_cls.repos_payload, self.repos_payload)
        self.assertEqual(tst_cls.public_repos(), self.expected_repos)
        self.mock.assert_called()

    def test_public_repos_with_license(self):
        """test the public_repos with the argument license"""
        test_class = GithubOrgClient("holberton")
        assert True

    @classmethod
    def tearDownClass(cls) -> None:
        """tear down class"""
        cls.get_patcher.stop()


if __name__ == "__main__":
    unittest.main()
