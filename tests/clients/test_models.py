from datetime import date

from tests.clients.mock_data import Mocks
from netrunner.clients.models import Card, Deck, Faction, Tournament, Entry


class TestModels:
    def test_tournament(self):
        tournament_json = Mocks.TOURNAMENT
        tournament = Tournament(tournament_json)

        assert tournament.id == 3789
        assert tournament.location_country == "Czechia"
        assert tournament.date == date(2023, 6, 29)
        assert tournament.type == "circuit opener"
        assert tournament.format == "standard"
        assert tournament.winner_runner_identity == "26066"
        assert tournament.winner_corp_identity == "21054"

    def test_entry(self):
        entry_json = Mocks.ENTRY
        entry = Entry(entry_json)

        assert entry.user_id == 42980
        assert entry.rank_swiss == 2
        assert entry.rank_topcut == 3
        assert entry.runner_deck_identity_id == "34020"
        assert entry.runner_deck_identity_title == "Arissana Rocha Nahu: Street Artist"
        assert entry.runner_deck_identity_faction == "shaper"
        assert entry.corp_deck_identity_id == "34039"
        assert entry.corp_deck_identity_title == "A Teia: IP Recovery"
        assert entry.corp_deck_identity_faction == "jinteki"

    def test_card(self):
        card_json = Mocks.RUNNER
        card = Card(card_json)

        assert card.code == "26066"
        assert card.title == "Hoshiko Shiro: Untold Protagonist"
        assert card.faction_code == "anarch"
        assert card.image_url == "https://static.nrdbassets.com/v1/large/26066.jpg"
        assert card.url == "https://netrunnerdb.com/en/card/26066"

    def test_faction(self):
        faction_json = Mocks.FACTIONS[0]
        faction = Faction(faction_json)

        assert faction.code == "anarch"
        assert faction.color == "FF4500"
        assert not faction.is_mini
        assert faction.name == "Anarch"
        assert faction.side_code == "runner"

    def test_deck(self):
        deck_json = Mocks.DECK
        deck = Deck(deck_json)

        assert deck.id == 1580775
        assert deck.uuid == "a80f818b-70a5-42bb-ad1a-557e4c88b0e2"
        assert deck.created_at is not None
        assert deck.updated_at is not None
        assert deck.name == "A Glacial Teia (3rd @ West Coast Nats)"
        assert deck.description == "deck description"
        assert len(deck.cards) == 21
