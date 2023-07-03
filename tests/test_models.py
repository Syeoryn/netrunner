from datetime import date

from netrunner.clients.mock_data import Mocks
from netrunner.data.models import Card, Tournament

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

    def test_card(self):
        card_json = Mocks.RUNNER
        card = Card(card_json)

        assert card.code == "26066"
        assert card.title == "Hoshiko Shiro: Untold Protagonist"
        assert card.faction_code == "anarch"
        assert card.image_url == "https://static.nrdbassets.com/v1/large/26066.jpg"
        assert card.url == "https://netrunnerdb.com/en/card/26066"
