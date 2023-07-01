
from netrunner.clients.mock_data import Mocks

class TestMocks:
    def test_runner(self):
        runner = Mocks.RUNNER
        assert runner["data"][0]["code"] == '26066'

    def test_corp(self):
        corp = Mocks.CORP
        assert corp.get("data")[0]["code"] == '21054'

    def test_tournament(self):
        tournament = Mocks.TOURNAMENT
        assert tournament["id"] == 3789
