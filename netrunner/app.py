import pandas as pd

import streamlit as st

from clients.abr_client import AbrClient
from clients.nrdb_client import NrdbClient


st.set_page_config(page_title="Netrunner", page_icon="assets/NSG-Visual-Assets/SVG/Game Symbols/NISEI_AGENDA.png")

abr_client = AbrClient()
nrdb_client = NrdbClient()


def render_tournament(tournament):
    "Location: " + tournament.location_country
    "Date: " + tournament.date.strftime("%Y.%m.%d")
    "Format: " + tournament.format
    "Type: " + tournament.type

    col1, _, col2 = st.columns([2, 1, 2])

    runner_id = tournament.winner_runner_identity
    runner = nrdb_client.get_card(runner_id)
    col1.write("Winner Runner: [{}  ({})]({})".format(runner.title, runner.faction_code, runner.url))
    col1.image(runner.image_url)

    corp_id = tournament.winner_corp_identity
    corp = nrdb_client.get_card(corp_id)
    col2.write("Winner Corp: [{}  ({})]({})".format(corp.title, corp.faction_code, corp.url))
    col2.image(corp.image_url)


# def plot(df):
#     fig, ax = plt.subplots()
#     ax.hist(df)
#     st.pyplot(fig)


def get_tournaments():
    return abr_client.get_tournament_results(10)


if 'tournaments' not in st.session_state:
    st.session_state['tournaments'] = get_tournaments()

tournaments = st.session_state['tournaments']


"### Last Tournament"
render_tournament(tournaments[0])


"### Recent Tournaments"
t_frame = pd.DataFrame(tournaments)
locations = t_frame[["latitude", "longitude"]]
st.map(locations[t_frame.latitude.notnull()])
t_frame


"#### Winning Factions"
col_1, col_2 = st.columns(2)

col_1.write("##### Corp")
corp_winners = t_frame.groupby(['winner_corp_identity'])["winner_corp_identity"].count()#.reset_index()
# corp_winners.columns(['Values', 'Count'])
col_1.write(corp_winners.sort_values(ascending=False))

col_2.write("##### Runner")
runner_winners = t_frame.groupby(['winner_runner_identity'])["winner_runner_identity"].count()
col_2.write(runner_winners.sort_values(ascending=False))

"#### Entries"
if 'entries' not in st.session_state:
    tournament_ids = [t.id for t in tournaments]
    entries = []
    for t_id in tournament_ids:
        entries.extend(abr_client.get_tournament_entries(t_id))
    st.session_state['entries'] = entries

entries = st.session_state['entries']

e_frame = pd.DataFrame(entries)
total = len(e_frame)
claimed = len(e_frame[e_frame['user_id'] != 0])
unclaimed = total - claimed
percentage = round(claimed / total * 100)

total_col, claimed_col, unclaimed_col, percentage_col = st.columns(4)

total_col.metric("Total Entries", total)
claimed_col.metric("# claimed", claimed)
unclaimed_col.metric("# unclaimed", unclaimed)
percentage_col.metric("% claimed",  '{}%'.format(percentage))
e_frame


"#### Top Cut Factions"
top_cut_frame = e_frame[e_frame['rank_topcut'].notnull()]
"##### Corp"
top_corps = top_cut_frame.groupby(['corp_deck_identity_title'])["corp_deck_identity_title"].count().sort_values(ascending=False)
top_corps

"##### Runner"
played_runners = top_cut_frame.groupby(['runner_deck_identity_title'])["runner_deck_identity_title"].count().sort_values(ascending=False)
played_runners

"#### Played Factions"
"##### Corp"
played_corps = e_frame.groupby(['corp_deck_identity_title'])["corp_deck_identity_title"].count().sort_values(ascending=False)
played_corps

"##### Runner"
played_runners = e_frame.groupby(['runner_deck_identity_title'])["runner_deck_identity_title"].count().sort_values(ascending=False)
played_runners
