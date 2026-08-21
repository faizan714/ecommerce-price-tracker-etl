import requests
from bs4 import BeautifulSoup
import pandas as pd
import os
URL = "https://books.toscrape.com/"

response = requests.get(URL)
soup = BeautifulSoup(response.text, 'html.parser')

books = soup.find_all("article", class_="product_pod")
print("Number of books:", len(books))


books_data = []

for book in books:

    title = book.h3.a["title"]

    price = book.find(
        "p",
        class_="price_color"
    ).text.strip()

    availability = book.find(
        "p",
        class_="instock availability"
    ).text.strip()

    rating = book.find("p")["class"][1]

    image_url = book.find("img")["src"]


    book_data = {
        "title": title,
        "price": price,
        "rating": rating,
        "availability": availability,
        "image_url": image_url
    }

    books_data.append(book_data)


df = pd.DataFrame(books_data)

df.to_csv(
    "data/books_raw.csv",
    index=False
)

