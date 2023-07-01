from requests import request

from .mock_data import Mocks


class NrdbClient:
    """
    API Client class for calling the NetrunnerDB API: https://netrunnerdb.com/api/2.0/doc
    API v2 Documentation: https://netrunnerdb.com/api/doc
    API v3-preview Documentation: https://api-preview.netrunnerdb.com/api/docs/

    v2 Base URL: https://netrunnerdb.com/
    Supported API Endpoints:
        /api/2.0/public/card/{card_code}
        /api/2.0/public/deck/{deck_id}  # might need to use /api/2.0/public/decklist/{decklist_id} instead
        /api/2.0/public/factions
        /api/2.0/public/faction/{faction_code}

    Unsupported API Endpoints:
        There are lots.  Check them all out here: https://netrunnerdb.com/api/doc

    Authentication: None, for public APIs.  This app does not use private APIs.
    """

    def get_card(self, code):
        # Gets a card from /api/2.0/public/card/{card_code} with the given card code
        # TODO: replace mocks with data from actual API call.
        if code == Mocks.RUNNER["data"][0]["code"]:
            return Mocks.RUNNER
        elif code == Mocks.CORP["data"][0]["code"]:
            return Mocks.CORP

    def get_deck(self, id):
        # Gets a deck from /api/2.0/public/deck/{deck_id} with the given deck id
        # TODO: implement API call
        pass

    def get_faction(self, code):
        # Gets a faction from /api/2.0/public/faction/{faction_code} with the given faction id
        # TODO: implement API call
        pass

    def get_factions(self):
        # Gets all factions from /api/2.0/public/factions
        # TODO: implement API call
        pass
