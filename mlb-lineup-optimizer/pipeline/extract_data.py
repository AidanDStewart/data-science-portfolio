## THIS PROGRAM DOES NOT WORK
## THE BATTING STATS FUNCTION IN PYBASEBALL DOES NOT WORK
## THE WEBSITE THAT IT CALLS NEEDS "HUMAN INTERACTION" TO WORK, AND PYBASEBALL CANNOT PROVIDE THAT
## https://www.fangraphs.com/leaders-legacy.aspx


""" from pybaseball import batting_stats
import os

os.makedirs("data/raw", exist_ok=True)

SEASON = 2025

print("Extracting data for season", SEASON)

df = batting_stats(SEASON, qual=0)

print(f"Data shape: {df.shape}")

file_path = f"data/raw/batting_stats_{SEASON}.csv"
df.to_csv(file_path, index=False)

print(f"Raw data saved to {file_path}") """