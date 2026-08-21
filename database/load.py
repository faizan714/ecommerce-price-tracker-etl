from pathlib import Path
import pandas as pd
from database import engine

# Resolve path to root directory (price_tracker_etl)
BASE_DIR = Path(__file__).resolve().parent.parent

# Read CSV directly from the data folder
df = pd.read_csv(BASE_DIR / "data" / "books_cleaned.csv")

# Load data into PostgreSQL table
df.to_sql(
    "books_cleaned",
    engine,
    if_exists="append",
    index=False
)

print("Data loaded successfully!")