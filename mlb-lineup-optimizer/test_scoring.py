import pandas as pd
from logic.scoring import calculate_scores
from logic.optimizer import build_lineup

df = pd.read_csv("data/processed/hitters_2025.csv")

df_scored = calculate_scores(df)

lineup = build_lineup(df_scored)

print(lineup)