import json
import requests

from .models import Card, Deck, Decklist, Faction


class NrdbClient:
    """
    API Client class for calling the NetrunnerDB API: https://netrunnerdb.com/api/2.0/doc
    API v2 Documentation: https://netrunnerdb.com/api/doc
    API v3-preview Documentation: https://api-preview.netrunnerdb.com/api/docs/

    v2 Base URL: https://netrunnerdb.com/
    Supported API Endpoints:
        /api/2.0/public/card/{card_code}
        /api/2.0/public/deck/{deck_id}
        /api/2.0/public/decklist/{decklist_id}
        /api/2.0/public/factions
        /api/2.0/public/faction/{faction_code}

    Unsupported API Endpoints:
        There are lots.  Check them all out here: https://netrunnerdb.com/api/doc

    Authentication: None, for public APIs.  This app does not use private APIs.
    """

    BASE_URL = "https://netrunnerdb.com"
    CARD_API = '/api/2.0/public/card/{card_code}'
    DECK_API = '/api/2.0/public/deck/{deck_id}'
    DECKLIST_API = '/api/2.0/public/decklist/{decklist_id}'
    FACTION_API = '/api/2.0/public/faction/{faction_code}'
    FACTIONS_API = "/api/2.0/public/factions"

    def get_card(self, code):
        # Gets a card from /api/2.0/public/card/{card_code} with the given card code
        response = requests.get(self.BASE_URL + self.CARD_API.format(card_code=code))
        return Card(json.loads(response.text))

    def get_decklist(self, decklist_uuid):
        # Gets a decklist from /api/2.0/public/decklist/{decklist_id} with the given deck id
        response = requests.get(self.BASE_URL + self.DECKLIST_API.format(decklist_id=decklist_uuid))
        return Decklist(json.loads(response.text)["data"][0])

    def get_deck(self, deck_uuid):
        # Gets a deck from /api/2.0/public/deck/{deck_id} with the given deck id
        response = requests.get(self.BASE_URL + self.DECK_API.format(deck_id=deck_uuid))
        return Deck(json.loads(response.text)["data"][0])

    def get_faction(self, code):
        # Gets a faction from /api/2.0/public/faction/{faction_code} with the given faction id
        response = requests.get(self.BASE_URL + self.FACTION_API.format(faction_code=code))
        return Faction(json.loads(response.text)["data"][0])

    def get_factions(self):
        # Gets all factions from /api/2.0/public/factions
        response = requests.get(self.BASE_URL + self.FACTIONS_API)
        response_json = json.loads(response.text)
        return [Faction(f) for f in response_json["data"]]
