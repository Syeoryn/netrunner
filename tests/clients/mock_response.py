from tests.clients.mock_data import Mocks


class MockResponse:
    DECK_RESPONSE = {
        "data": [Mocks.DECK],
        "total": 1,
        "success": True,
        "version_number": "2.0",
        "last_updated": "2023-10-10T22:09:37+00:00"
    }

    DECKLIST_RESPONSE = {
        "data": [Mocks.DECKLIST],
        "total": 1,
        "success": True,
        "version_number": "2.0",
        "last_updated": "2023-10-09T10:47:13+00:00"
    }

    FACTION_RESPONSE = {
        "data": [Mocks.FACTIONS[0]],
        "total": 1,
        "success": True,
        "version_number": "2.0",
        "last_updated": "2016-07-07T07:57:36+00:00"
    }

    FACTIONS_RESPONSE = {
        "data": Mocks.FACTIONS,
        "total": 12,
        "success": True,
        "version_number": "2.0",
        "last_updated": "2022-07-12T14:55:15+00:00"
    }
