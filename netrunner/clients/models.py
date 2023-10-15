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
    latitude: float
    longitude: float
    payload: str

    def __init__(self, json):
        self.id = json["id"]
        self.location_country = json["location_country"]
        self.date = datetime.strptime(json["date"], "%Y.%m.%d.").date()  # Format: YYYY.mm.dd
        self.type = json["type"]
        self.format = json["format"]
        self.winner_runner_identity = json.get("winner_runner_identity")
        self.winner_corp_identity = json.get("winner_corp_identity")
        self.latitude = json.get("location_lat")
        self.longitude = json.get("location_lng")
        self.payload = json


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


@dataclass
class Faction:
    code: str
    color: str
    is_mini: bool
    name: str
    side_code: str

    def __init__(self, json):
        self.code = json["code"]
        self.color = json["color"]
        self.is_mini = json["is_mini"]
        self.name = json["name"]
        self.side_code = json["side_code"]


@dataclass
class Decklist:
    id: int
    uuid: str
    created_at: datetime
    updated_at: datetime
    name: str
    description: str
    user_id: int
    user_name: str
    tournament_badge: bool
    cards: dict
    mwl_code: str

    def __init__(self, json):
        self.id = json["id"]
        self.uuid = json["uuid"]
        self.created_at = json["date_creation"]
        self.updated_at = json["date_update"]
        self.name = json["name"]
        self.description = json["description"]
        self.user_id = json["user_id"]
        self.user_name = json["user_name"]
        self.tournament_badge = json["tournament_badge"]
        self.cards = json["cards"]
        self.mwl_code = json["mwl_code"]


@dataclass
class Deck:
    id: int
    uuid: str
    created_at: datetime
    updated_at: datetime
    name: str
    description: str
    cards: dict

    def __init__(self, json):
        self.id = json["id"]
        self.uuid = json["uuid"]
        self.created_at = json["date_creation"]
        self.updated_at = json["date_update"]
        self.name = json["name"]
        self.description = json["description"]
        self.cards = json["cards"]