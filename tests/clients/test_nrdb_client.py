import json

import unittest
from unittest.mock import call
from unittest.mock import patch

from netrunner.clients.nrdb_client import NrdbClient
from tests.clients.mock_data import Mocks
from tests.clients.mock_response import MockResponse



class TestNrdbClient(unittest.TestCase):
    def setUp(self):
        self.client = NrdbClient()

    @patch('requests.get')  # Mock the requests.get method
    def test_get_card(self, mock_get):
        mock_response_json = Mocks.CORP
        mock_response = unittest.mock.Mock()
        mock_response.text = json.dumps(mock_response_json)
        mock_get.return_value = mock_response

        card_code = "21054"
        result = self.client.get_card(card_code)

        assert result is not None
        mock_get.assert_called_once_with(
            f'https://netrunnerdb.com/api/2.0/public/card/{card_code}'
        )

    @patch('requests.get')
    def test_get_decklist(self, mock_get):
        mock_response_json = MockResponse.DECKLIST_RESPONSE

        mock_response = unittest.mock.Mock()
        mock_response.text = json.dumps(mock_response_json)
        mock_get.return_value = mock_response

        decklist_uuid = "1234-abcd-cd23-8ab2"
        result = self.client.get_decklist(decklist_uuid)

        assert result is not None
        mock_get.assert_called_once_with(
            f'https://netrunnerdb.com/api/2.0/public/decklist/{decklist_uuid}'
        )

    @patch('requests.get')
    def test_get_deck(self, mock_get):
        mock_response_json = MockResponse.DECK_RESPONSE

        mock_response = unittest.mock.Mock()
        mock_response.text = json.dumps(mock_response_json)
        mock_get.return_value = mock_response

        deck_uuid = "abcd-1234-5a3d-11ab"
        result = self.client.get_deck(deck_uuid)

        assert result is not None
        mock_get.assert_called_once_with(
            f'https://netrunnerdb.com/api/2.0/public/deck/{deck_uuid}'
        )

    @patch('requests.get')
    def test_get_faction(self, mock_get):
        mock_response_json = MockResponse.FACTION_RESPONSE

        mock_response = unittest.mock.Mock()
        mock_response.text = json.dumps(mock_response_json)
        mock_get.return_value = mock_response

        faction_code = "criminal"
        result = self.client.get_faction(faction_code)

        assert result is not None
        mock_get.assert_called_once_with(
            f'https://netrunnerdb.com/api/2.0/public/faction/{faction_code}'
        )

    @patch('requests.get')
    def test_get_factions(self, mock_get):
        mock_response_json = MockResponse.FACTIONS_RESPONSE

        mock_response = unittest.mock.Mock()
        mock_response.text = json.dumps(mock_response_json)
        mock_get.return_value = mock_response

        result = self.client.get_factions()

        assert result is not None
        mock_get.assert_called_once_with(
            'https://netrunnerdb.com/api/2.0/public/factions'
        )