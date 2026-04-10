import streamlit as st

st.title("Project Methodology")

st.markdown("""


## Data Collection
The data for this project was collected from the library pybaseball. I used the `batting_stats` function to collect batting statistics from the 2025 season. The `batting_stats` documentation can be found [here](https://github.com/jldbc/pybaseball/blob/master/docs/batting_stats.md).


            
## Future Improvements
There are limitless improvements that can be made to this project, but here are a few that I would like to implement in the future:

- *Pitcher Optimization*: This application currently only uses full season data. I would like to implement a way to add a pitcher matchup component. This would allow users to optimize their lineups based on the pitcher that is starting that day.


## Author
Aidan Stewart | Data Scientist | [LinkedIn](https://www.linkedin.com/in/aidan-stewart-3b1355288/) | [GitHub](https://github.com/AidanDStewart/data-science-portfolio) | Python | SQL
""")