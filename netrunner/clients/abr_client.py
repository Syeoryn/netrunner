from datetime import date
from dateutil import relativedelta
import json
import requests

from netrunner.data.models import Tournament


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
    MAX_PAGE_SIZE = 500
    DEFAULT_LIMIT = 200

    BASE_URL = "https://alwaysberunning.net"
    RESULT_API = "/api/tournaments/results"

    def get_tournament_results(self, limit=DEFAULT_LIMIT, offset=0):
        # Gets the last N tournament results from /api/tournaments/results, with a maximum of 500
        params = {
            "limit": min(limit, self.MAX_PAGE_SIZE),
            "offset": offset
        }
        response = requests.get(self.BASE_URL + self.RESULT_API, params=params)
        json_response = json.loads(response.text)
        tournaments = [Tournament(t) for t in json_response]

        # check if response is not empty to prevent unnecessary requests
        if limit > self.MAX_PAGE_SIZE and len(json_response) > 0:
            next_page = self.get_tournament_results(
                limit=limit - self.MAX_PAGE_SIZE,
                offset=offset + self.MAX_PAGE_SIZE
            )
            tournaments += next_page

        return tournaments

    def filter_tournaments(self, start_date=ONE_MONTH_AGO, end_date=TODAY):
        # Gets all tournaments within the given start and end dates using /api/tournaments
        # By default, gets all tournaments from the last month.
        # Available filters: https://alwaysberunning.net/apidoc#filters
        # TODO: implement tournament filter API.
        pass
