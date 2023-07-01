import streamlit as st

from clients.abr_client import AbrClient
from clients.nrdb_client import NrdbClient

st.set_page_config(page_title="Netrunner", page_icon="assets/NSG-Visual-Assets/SVG/Game Symbols/NISEI_AGENDA.png")

abr_client = AbrClient()
nrdb_client = NrdbClient()

def render_tournament(tournament):
    "Event: " + tournament["title"]
    "Location: " + tournament["location"]
    "Date: " + tournament["date"]
    "Format: " + tournament["format"]
    "Cardpool: " + tournament["cardpool"]
    runner = tournament["winner_runner_identity"]
    corp = tournament["winner_corp_identity"]
    st.write(runner)
    st.write(nrdb_client.get_card(runner[0]))
    # "Winner Runner: " + nrdb_client.get_card(runner)
    # "Winner Corp: " + nrdb_client.get_card(corp)

"### Last Tournament"
last_tournament = abr_client.get_tournament_results(1)[0]
render_tournament(last_tournament)
