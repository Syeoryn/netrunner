import base64
import textwrap

import streamlit as st
from clients.abr_client import AbrClient
from clients.nrdb_client import NrdbClient
from data import mappings


st.set_page_config(page_title="Netrunner", page_icon="assets/NSG-Visual-Assets/SVG/Game Symbols/NISEI_AGENDA.png")

abr_client = AbrClient()
nrdb_client = NrdbClient()

def get_faction_glyph(faction_code):
    mapping = mappings.FACTION_ASSETS.get(faction_code)
    if mapping is not None:
        return mappings.BASE_FACTION_GLYPH_PATH.format(mapping["glyph_path"])


def render_tournament(tournament: Tournament):
    "Location: " + tournament.location_country
    "Date: " + tournament.date.strftime("%Y.%m.%d")
    "Format: " + tournament.format
    "Type: " + tournament.type

    col1, _, col2 = st.columns([2, 1, 2])

    runner_id = tournament.winner_runner_identity
    runner = Card(nrdb_client.get_card(runner_id))
    col1.write("Winner Runner: [{}  ({})]({})".format(runner.title, runner.faction_code, runner.url))
    col1.image(runner.image_url)

    corp_id = tournament.winner_corp_identity
    corp = Card(nrdb_client.get_card(corp_id))
    col2.write("Winner Corp: [{}  ({})]({})".format(corp.title, corp.faction_code, corp.url))
    col2.image(corp.image_url)


"### Last Tournament"
last_tournament = Tournament(abr_client.get_tournament_results(1)[0])
render_tournament(last_tournament)
