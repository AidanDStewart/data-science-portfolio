import streamlit as st

st.set_page_config(page_title="MLB Lineup Optimizer", layout="wide")

st.title("MLB Lineup Optimization Tool")

st.markdown("""
This project builds optimized MLB batting lineups using role-based scoring.
            
### How it works:
- Select a team and season
- Players are scored based on lineup role
- The optimizer builds the best batting order
            
Click the button below to get started!
""")

if st.button("Go to Optimizer"):
    st.switch_page("pages/1_Team_Lineup.py")