CREATE TABLE IF NOT EXISTS hitters (
    player_id TEXT PRIMARY KEY,
    player_name TEXT,
    team TEXT,
    season INTEGER,
    position TEXT,
    pa INTEGER,
    obp REAL,
    slg REAL,
    ops REAL,
    bb_pct REAL,
    k_pct REAL,
    iso REAL,
    wrc_plus REAL,
    bsr REAL,
    hard_hit_pct REAL,
    war REAL,
    active_flag INTEGER
);

CREATE INDEX idx_team_season ON hitters(team, season);