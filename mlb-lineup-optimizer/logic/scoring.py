import pandas as pd

def compute_z_scores(df, cols):
    # Standardize columns using z-scores

    df_z = df.copy()

    for col in cols:
        mean = df[col].mean()
        std = df[col].std()

        if std == 0:
            df_z[col + "_z"] = 0
        else:
            df_z[col + "_z"] = (df[col] - mean) / std

    return df_z

def calculate_scores(df):

    # Calculate lineup role scores for each player

    cols_to_standardize = [
        "obp", "slg", "ops",
        "bb_pct", "k_pct",
        "iso", "wrc_plus",
        "bsr", "hard_hit_pct"
    ]

    df = compute_z_scores(df, cols_to_standardize)

    # Define scoring formula

    # Leadoff (1st)
    df["score_1"] = (
        .35 * df["obp_z"] +
        .20 * df["bb_pct_z"] -
        .15 * df["k_pct_z"] +
        .15 * df["bsr_z"] +
        .15 * df["wrc_plus_z"]
    )

    # Spot 2 (Balanced)
    df["score_2"] = (
        0.30 * df["obp_z"] +
        0.25 * df["slg_z"] +
        0.25 * df["wrc_plus_z"] -
        0.20 * df["k_pct_z"]
    )

    # Spot 3 (Best hitter)
    df["score_3"] = (
        0.40 * df["wrc_plus_z"] +
        0.30 * df["obp_z"] +
        0.30 * df["slg_z"]
    )

    # Cleanup (Spot 4)
    df["score_4"] = (
        0.35 * df["slg_z"] +
        0.30 * df["iso_z"] +
        0.15 * df["hard_hit_pct_z"] +
        0.10 * df["obp_z"] +
        0.10 * df["wrc_plus_z"]
    )

    # Spot 5
    df["score_5"] = (
        0.30 * df["slg_z"] +
        0.25 * df["iso_z"] +
        0.20 * df["obp_z"] +
        0.25 * df["wrc_plus_z"]
    )

    # Spots 6–8 (general hitters)
    for i in [6, 7, 8]:
        df[f"score_{i}"] = (
            0.40 * df["ops_z"] +
            0.40 * df["wrc_plus_z"] +
            0.20 * df["obp_z"]
        )

    # Spot 9
    df["score_9"] = (
        0.30 * df["obp_z"] +
        0.30 * df["bsr_z"] +
        0.20 * df["wrc_plus_z"] +
        0.20 * df["ops_z"]
    )

    return df