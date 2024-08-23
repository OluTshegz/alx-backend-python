#!/usr/bin/env python3
"""
Unit tests for the GithubOrgClient class.
"""

import unittest
from typing import Dict
from unittest.mock import patch, MagicMock, PropertyMock
from parameterized import parameterized, parameterized_class
from requests import HTTPError
from client import GithubOrgClient
from fixtures import TEST_PAYLOAD


class TestGithubOrgClient(unittest.TestCase):
    """
    Tests for the GithubOrgClient class.
    """

    @parameterized.expand([
        ("google", {'login': "google"}),
        ("abc", {'login': "abc"})
    ])
    @patch('client.get_json', return_value={'payload': True})
    def test_org(self, org: str, expected_response: Dict,
                 mock_get_json: MagicMock) -> None:
        """
        Tests that GithubOrgClient.org returns the correct value.

        Args:
            org (str): Organization name.
            expected_response (Dict): Expected response.
            mock_get_json (MagicMock): Mocked get_json function.
        """
        mock_get_json.return_value = expected_response
        client = GithubOrgClient(org)
        self.assertEqual(client.org(), expected_response)
        mock_get_json.assert_called_once()

    def test_public_repos_url(self) -> None:
        """
        Tests that GithubOrgClient._public_repos_url returns
        the correct URL based on the mocked org property.
        """
        with patch('client.GithubOrgClient.org',
                   new_callable=PropertyMock) as mock_org:
            mock_org.return_value = {'repos_url':
                                     """https://api.github.com/
                                     users/google/repos"""}
            client = GithubOrgClient("google")
            self.assertEqual(client._public_repos_url,
                             "https://api.github.com/users/google/repos")
            mock_org.assert_called_once()

    @patch('client.get_json')
    def test_public_repos(self, mock_get_json: MagicMock) -> None:
        """
        Tests that GithubOrgClient.public_repos returns
        the correct list of repo names.

        Args:
            mock_get_json (MagicMock): Mocked get_json function.
        """
        payload = {
            'repos_url': "https://api.github.com/users/google/repos",
            'repos': [
                {"name": "episodes.dart"},
                {"name": "kratu"},
            ]
        }
        mock_get_json.return_value = payload['repos']
        with patch('client.GithubOrgClient._public_repos_url',
                   new_callable=PropertyMock) as mock_url:
            mock_url.return_value = payload['repos_url']
            client = GithubOrgClient("google")
            self.assertEqual(client.public_repos(), ["episodes.dart", "kratu"])
            mock_url.assert_called_once()
        mock_get_json.assert_called_once()

    @parameterized.expand([
        ({"license": {"key": "bsd-3-clause"}}, "bsd-3-clause", True),
        ({"license": {"key": "bsl-1.0"}}, "bsd-3-clause", False),
    ])
    def test_has_license(self, repo: Dict,
                         key: str, expected: bool) -> None:
        """
        Tests that GithubOrgClient.has_license returns
        the correct boolean for license presence.

        Args:
            repo (Dict): Repository dictionary.
            key (str): License key.
            expected (bool): Expected result.
        """
        client = GithubOrgClient("google")
        self.assertEqual(client.has_license(repo, key), expected)


@parameterized_class([
    {
        'org_payload': TEST_PAYLOAD[0][0],
        'repos_payload': TEST_PAYLOAD[0][1],
        'expected_repos': TEST_PAYLOAD[0][2],
        'apache2_repos': TEST_PAYLOAD[0][3],
    },
])
class TestIntegrationGithubOrgClient(unittest.TestCase):
    """
    Integration tests for GithubOrgClient using fixtures.
    """

    org_payload = TEST_PAYLOAD[0][0]
    repos_payload = TEST_PAYLOAD[0][1]
    expected_repos = TEST_PAYLOAD[0][2]
    apache2_repos = TEST_PAYLOAD[0][3]

    @classmethod
    def setUpClass(cls) -> None:
        """
        Sets up the patcher for requests.get and initializes the client.
        """
        def requests_get(url):
            if url == "https://api.github.com/orgs/google":
                return MockResponse(cls.org_payload)
            elif url == cls.org_payload['repos_url']:
                return MockResponse(cls.repos_payload)
            raise HTTPError(f"Unexpected URL: {url}")

        class MockResponse:
            def __init__(self, json_data):
                self._json_data = json_data

            def json(self):
                return self._json_data

        cls.get_patcher = patch('requests.get', side_effect=requests_get)
        cls.get_patcher.start()
        cls.client = GithubOrgClient('google')

    @classmethod
    def tearDownClass(cls) -> None:
        """
        Stops the patcher.
        """
        cls.get_patcher.stop()

    def test_public_repos(self) -> None:
        """
        Tests public_repos method with the expected results from fixtures.
        """
        self.assertEqual(self.client.public_repos(), self.expected_repos)

    def test_public_repos_with_license(self) -> None:
        """
        Tests public_repos method with the license filter using fixtures.
        """
        self.assertEqual(
            self.client.public_repos(license="apache-2.0"),
            self.apache2_repos,
        )
