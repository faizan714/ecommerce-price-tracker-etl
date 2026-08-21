import pandas as pd

df = pd.read_csv("data/books_raw.csv")

print(df.head())
print(df.shape)
print(df.info())
print(df.isnull().sum())
print(df.duplicated().sum())


import pandas as pd
from datetime import date


# 1. Load raw data
df = pd.read_csv("data/books_raw.csv")


# 2. Rename columns
df = df.rename(columns={
    "title": "product_name"
})


# 3. Clean price
df["price"] = (
    df["price"]
    .str.replace("£", "", regex=False)
)


# 4. Convert rating
rating_map = {
    "One": 1,
    "Two": 2,
    "Three": 3,
    "Four": 4,
    "Five": 5
}

df["rating"] = df["rating"].map(rating_map)


# 5. Clean availability
df["availability"] = (
    df["availability"]
    .str.strip()
    .str.title()
)


# 6. Add scrape date
df["scrape_date"] = date.today()


# 7. Remove duplicates
df = df.drop_duplicates()


# 8. Reorder columns
df = df[
    [
        "product_name",
        "price",
        "rating",
        "availability",
        "image_url",
        "scrape_date"
    ]
]


# 9. Data validation
print("Shape:", df.shape)

print("\nMissing values:")
print(df.isnull().sum())

print("\nDuplicate rows:")
print(df.duplicated().sum())

print("\nPrice statistics:")
print(df["price"].describe())

print("\nRating distribution:")
print(df["rating"].value_counts().sort_index())


# 10. Save processed data
df.to_csv(
    "data/books_cleaned.csv",
    index=False
)

print("\nCleaned data saved successfully!")

df.head()