class Mocks:
    """
    This class contains mocked data representing the data returned from the ABR and NRDB APIs.
    """
    RUNNER = {
        "imageUrlTemplate": "https://static.nrdbassets.com/v1/large/{code}.jpg",
        "data": [
            {
                "base_link": 0,
                "code": "26066",
                "deck_limit": 1,
                "faction_code": "anarch",
                "faction_cost": 0,
                "flavor": "Please, let me have this dream.\nFlip side:\nI'm going to be my own kind of hero.",
                "illustrator": "Luminita Pham",
                "influence_limit": 15,
                "keywords": "Natural",
                "minimum_deck_size": 45,
                "pack_code": "ur",
                "position": 66,
                "quantity": 3,
                "side_code": "runner",
                "stripped_text": "When your turn ends, if you accessed at least 1 card this turn, gain 2 credits and flip this identity. Flip side: When your turn begins, draw 1 card and lose 1 credit. When your turn ends, if you did not access at least 1 card this turn, flip this identity.",
                "stripped_title": "Hoshiko Shiro: Untold Protagonist",
                "text": "When your turn ends, if you accessed at least 1 card this turn, gain 2[credit] and flip this identity.\nFlip side:\nWhen your turn begins, draw 1 card and lose 1[credit].\nWhen your turn ends, if you did not access at least 1 card this turn, flip this identity.",
                "title": "Hoshiko Shiro: Untold Protagonist",
                "type_code": "identity",
                "uniqueness": False
            }
        ],
        "total": 1,
        "success": True,
        "version_number": "2.0",
        "last_updated": "2021-03-13T05:08:22+00:00"
    }

    CORP = {
        "imageUrlTemplate": "https://static.nrdbassets.com/v1/large/{code}.jpg",
        "data": [
            {
                "code": "21054",
                "deck_limit": 1,
                "faction_code": "nbn",
                "faction_cost": 0,
                "illustrator": "Emilio Rodriguez",
                "influence_limit": 15,
                "keywords": "Division",
                "minimum_deck_size": 40,
                "pack_code": "cotc",
                "position": 54,
                "quantity": 3,
                "side_code": "corp",
                "stripped_text": "When your turn ends, you may name a card type. Gain 2 credits the first time each turn the Runner plays or installs a card that has the type you last named this way.",
                "stripped_title": "Azmari EdTech: Shaping the Future",
                "text": "When your turn ends, you may name a card type. Gain 2[credit] the first time each turn the Runner plays or installs a card that has the type you last named this way.",
                "title": "Azmari EdTech: Shaping the Future",
                "type_code": "identity",
                "uniqueness": False
            }
        ],
        "total": 1,
        "success": True,
        "version_number": "2.0",
        "last_updated": "2021-03-13T05:08:22+00:00"
    }

    TOURNAMENT = {
        "id": 3789,
        "title": "Circuit Opener 2023 #2 in Brno",
        "creator_id": 15340,
        "creator_name": "Krasty",
        "creator_supporter": 1,
        "creator_class": "supporter",
        "created_at": "2023.05.31. 15:11:16",
        "location": "Czechia, Brno-střed",
        "location_lat": 49.178417,
        "location_lng": 16.595302,
        "location_country": "Czechia",
        "location_state": "",
        "address": "Vídeňská 80, 639 00 Brno-střed, Czechia",
        "store": "BLACK OIL – Gaming & Social Hub",
        "place_id": "ChIJnQu_9WmUEkcRtVnjhqAs4u0",
        "contact": "krasty23 (at) gmail.com or just Krasty everywhere else (Discord, Slack, etc.)",
        "approved": 1,
        "registration_count": 9,
        "photos": 0,
        "url": "https://alwaysberunning.net/tournaments/3789/circuit-opener-2023-2-in-brno",
        "link_facebook": "",
        "cardpool": "Parhelion",
        "date": "2023.06.29.",
        "type": "circuit opener",
        "format": "standard",
        "mwl": "Standard Ban List 23.03",
        "concluded": True,
        "charity": False,
        "players_count": 8,
        "top_count": 0,
        "claim_count": 3,
        "claim_conflict": False,
        "matchdata": True,
        "videos": 0,
        "winner_runner_identity": "26066",
        "winner_corp_identity": "21054",
        "rendered_in": 0.6298110485076904,
        "tournament_count": 2837
    }
