import sqlite3
import pandas as pd

# File paths
DB_PATH = "data/lineup_tool.db"
DATA_PATH = "data/processed/hitters_2025.csv"
SCHEMA_PATH = "sql/schema.sql"

print("Loading cleaned data...")
df = pd.read_csv(DATA_PATH)

# Connect to SQLite DB (creates file if it doesn't exist)
conn = sqlite3.connect(DB_PATH)
cursor = conn.cursor()

print("Creating table...")

# Run schema.sql
with open(SCHEMA_PATH, "r") as f:
    schema_sql = f.read()
    cursor.executescript(schema_sql)

# Optional: clear existing data (so you don’t duplicate rows)
cursor.execute("DELETE FROM hitters")

print("Inserting data into database...")
df.to_sql("hitters", conn, if_exists="append", index=False)

conn.commit()
conn.close()

print("Database successfully populated!")