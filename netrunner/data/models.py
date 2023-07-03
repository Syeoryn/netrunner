from dataclasses import dataclass
from datetime import date, datetime


@dataclass
class Tournament:
    id: int
    location_country: str
    date: date
    type: str
    format: str
    winner_runner_identity: str
    winner_corp_identity: str

    def __init__(self, json):
        self.id = json["id"]
        self.location_country = json["location_country"]
        self.date = datetime.strptime(json["date"], "%Y.%m.%d.").date()  # Format: YYYY.mm.dd
        self.type = json["type"]
        self.format = json["format"]
        self.winner_runner_identity = json["winner_runner_identity"]
        self.winner_corp_identity = json["winner_corp_identity"]


@dataclass
class Card:
    code: str
    title: str = ""
    faction_code: str = ""
    image_url: str = ""
    url: str = ""

    def __init__(self, json):
        self.code = json["data"][0]["code"]
        self.title = json["data"][0]["title"]
        self.faction_code = json["data"][0]["faction_code"]
        self.image_url = json["imageUrlTemplate"].format(code=self.code)
        self.url = "https://netrunnerdb.com/en/card/{code}".format(code=self.code)
