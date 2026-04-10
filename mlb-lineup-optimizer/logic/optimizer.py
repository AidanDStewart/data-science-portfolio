import pandas as pd

def build_lineup(df):

    # Build optimized lineup using greedy approach

    df = df.copy()

    lineup = []
    used_players = set()

    for spot in range(1, 10):
        score_col = f"score_{spot}"

        available = df[~df["player_id"].isin(used_players)]

        best_player = available.sort_values(score_col, ascending=False).iloc[0]

        lineup.append({
            "spot": spot,
            "player_id": best_player["player_id"],
            "player_name": best_player["player_name"],
            "team": best_player["team"],
            "score": best_player[score_col]
        })

        used_players.add(best_player["player_id"])

    return pd.DataFrame(lineup)