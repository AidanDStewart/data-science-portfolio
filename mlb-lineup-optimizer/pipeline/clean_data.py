import pandas as pd
import os

INPUT_PATH = "data/raw/batting_stats_2025.csv"
OUTPUT_PATH = "data/processed/hitters_2025.csv"

os.makedirs("data/processed", exist_ok=True)

print("Loading raw data from", INPUT_PATH)
df = pd.read_csv(INPUT_PATH)

print(f"Original data shape: {df.shape}")

# Select and rename columns
df = df[[
    "IDfg",
    "Name",
    "Team",
    "Season",
    "Pos",
    "PA",
    "OBP",
    "SLG",
    "OPS",
    "BB%",
    "K%",
    "ISO",
    "wRC+",
    "BsR",
    "HardHit%",
    "WAR"
]]

df = df.rename(columns={
    "IDfg": "player_id",
    "Name": "player_name",
    "Team": "team",
    "Season": "season",
    "Pos": "position",
    "PA": "pa",
    "OBP": "obp",
    "SLG": "slg",
    "OPS": "ops",
    "BB%": "bb_pct",
    "K%": "k_pct",
    "ISO": "iso",
    "wRC+": "wrc_plus",
    "BsR": "bsr",
    "HardHit%": "hard_hit_pct",
    "WAR": "war"
})



# Clean data

MIN_PA = 0
df = df[df["pa"] > MIN_PA]

# Fill missing values
df["bsr"] = df["bsr"].fillna(0)
df["hard_hit_pct"] = df["hard_hit_pct"].fillna(0)

df["active_flag"] = 1
df["position"] = "Unknown"

print(f"Cleaned data shape: {df.shape}")

# Save cleaned data
df.to_csv(OUTPUT_PATH, index=False)
print(f"Cleaned data saved to {OUTPUT_PATH}")