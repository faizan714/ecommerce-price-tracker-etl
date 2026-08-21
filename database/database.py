from sqlalchemy import create_engine

DATABASE_URL = (
    "postgresql+psycopg2://postgres:1234@localhost:5432/ecommerce_tracker"
)

engine = create_engine(DATABASE_URL)

print("Database connection created!")