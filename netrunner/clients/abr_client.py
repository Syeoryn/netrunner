from datetime import date
from dateutil import relativedelta
from requests import request

from .mock_data import Mocks
class AbrClient:
    """
    API Client class for calling the AlwaysBeRunning API: https://alwaysberunning.net/apidoc

    Base URL: https://alwaysberunning.net
    Supported API Endpoints:
        /api/tournaments/results  # should not call for more than 500 tournaments.
        /api/tournaments  # supports search filters

    Unsupported API Endpoints:
        /api/tournaments/entries
        /api/tournaments/upcoming
        /api/tournaments/videos

    Authentication: None.
    """
    TODAY = date.today()
    ONE_MONTH_AGO = date.today() - relativedelta.relativedelta(months=1)
    DEFAULT_LIMIT = 500

    def get_tournament_results(self, limit=DEFAULT_LIMIT):
        # Gets the last N tournament results from /api/tournaments/results, with a maximum of 500
        # TODO: replace mock_tournament with results from actual API call.
        return [Mocks.TOURNAMENT]

    def filter_tournaments(self, start_date=ONE_MONTH_AGO, end_date=TODAY):
        # Gets all tournaments within the given start and end dates using /api/tournaments
        # By default, gets all tournaments from the last month.
        # Available filters: https://alwaysberunning.net/apidoc#filters
        # TODO: implement tournament filter API.
        pass
