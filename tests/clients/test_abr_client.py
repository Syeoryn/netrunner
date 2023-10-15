import json

import unittest
from unittest.mock import call
from unittest.mock import patch

from netrunner.clients.abr_client import AbrClient
from tests.clients.mock_data import Mocks
from tests.clients.mock_response import MockResponse


class TestAbrClient(unittest.TestCase):
    def setUp(self):
        self.client = AbrClient()

    @patch('requests.get')  # Mock the requests.get method
    def test_get_tournament_results(self, mock_get):
        mock_response_json = [
            Mocks.LAST_5_TOURNAMENTS[0],
            Mocks.LAST_5_TOURNAMENTS[1]
        ]

        mock_response = unittest.mock.Mock()
        mock_response.text = json.dumps(mock_response_json)

        mock_get.return_value = mock_response

        result = self.client.get_tournament_results(limit=2)

        assert len(result) == 2
        assert result[0].payload == mock_response_json[0]
        assert result[1].payload == mock_response_json[1]
        mock_get.assert_called_once_with(
            'https://alwaysberunning.net/api/tournaments/results',
            params={"limit": 2, "offset": 0}
        )

    @patch('requests.get')
    def test_get_tournament_entry(self, mock_get):
        mock_response_json = MockResponse.ENTRY_RESPONSE

        mock_response = unittest.mock.Mock()
        mock_response.text = json.dumps(mock_response_json)

        mock_get.return_value = mock_response

        result = self.client.get_tournament_entries(1)

        assert len(result) == 2
        assert result[0].user_id == 42980
        mock_get.assert_called_once_with(
            'https://alwaysberunning.net/api/tournaments/entries',
            params={"id": 1}
        )

    @patch('requests.get')
    def test_get_paginated_tournament_results(self, mock_get):
        mock_response_json = [
            Mocks.TOURNAMENT
        ]
        mock_response = unittest.mock.Mock()
        mock_response.text = json.dumps(mock_response_json)
        mock_get.return_value = mock_response

        result = self.client.get_tournament_results(limit=501)  # requesting the max limit + 1

        assert len(result) == 2
        assert mock_get.call_count == 2

        calls = [
            call('https://alwaysberunning.net/api/tournaments/results', params={"limit": 500, "offset": 0}),
            call('https://alwaysberunning.net/api/tournaments/results', params={"limit": 1, "offset": 500})
        ]
        mock_get.assert_has_calls(calls)
