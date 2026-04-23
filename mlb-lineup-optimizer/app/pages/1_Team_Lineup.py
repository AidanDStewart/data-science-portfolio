import streamlit as st
import pandas as pd
import subprocess
import sqlite3
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))


# Load data
@st.cache_data
def load_data():
    conn = sqlite3.connect("data/lineup_tool.db")
    df = pd.read_sql("SELECT * FROM hitters", conn)
    conn.close()
    return df

df = load_data()

teams = sorted(df["team"].unique())



## App logic

from logic.scoring import calculate_scores
from logic.optimizer import build_lineup



# SIDEBAR FILTERS
st.sidebar.header("Filters")

refresh_data = st.sidebar.button("Refresh Data")

min_pa = st.sidebar.slider(
    "Minimum Plate Appearances",
    min_value = 0,
    max_value = 700,
    value = 100,
    step = 10
)
selected_team = st.sidebar.selectbox("Select Team", teams)
generate = st.sidebar.button("Generate Lineup")


# Filtered data based on user input
df_filtered = df[
    (df["pa"] >= min_pa) & 
    (df["team"] == selected_team)
]


if refresh_data:
    with st.spinner("Refreshing data..."):
        
        try:
            subprocess.run(["python", "pipeline/clean_data.py"], check=True)
            subprocess.run(["python", "pipeline/load_db.py"], check=True)

            st.success("Data refreshed successfully!")
            st.cache_data.clear()

        except subprocess.CalledProcessError as e:
            st.error(f"Data refresh failed: {e}")
            st.stop()
        

# When the user clicks the "Generate Lineup" button, calculate scores and build the lineup
if generate:

    if df_filtered.empty:
        st.warning("No players meet the minimum PA requirement.")
    else:
        df_scored = calculate_scores(df_filtered)
        lineup = build_lineup(df_scored)

        st.subheader("Recommended Lineup")
        display_cols = ["spot", "player_name", "team", "score"]

        st.dataframe(
            lineup[display_cols],
            use_container_width=True,
            hide_index=True
        )

