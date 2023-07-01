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


def render_tournament(tournament):
    "Event: " + tournament["title"]
    "Location: " + tournament["location"]
    "Date: " + tournament["date"]
    "Format: " + tournament["format"]
    "Cardpool: " + tournament["cardpool"]

    runner_id = tournament["winner_runner_identity"]
    runner = nrdb_client.get_card(runner_id)["data"][0]
    st.write("Winner Runner: {}  ({})".format(runner["title"], runner["faction_code"]))

    corp_id = tournament["winner_corp_identity"]
    corp = nrdb_client.get_card(corp_id)["data"][0]
    st.write("Winner Corp: {}  ({})".format(corp["title"], corp["faction_code"]))


"### Last Tournament"
last_tournament = abr_client.get_tournament_results(1)[0]
render_tournament(last_tournament)
