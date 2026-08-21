E-Commerce Price Tracker ETL Pipeline

An end-to-end ETL (Extract, Transform, Load) pipeline that collects e-commerce product data through web scraping, cleans and transforms the extracted data, and stores the processed information in a structured database for analysis.

This project demonstrates practical **Data Engineering concepts**, including web scraping, data extraction, data cleaning, transformation, database loading, and pipeline automation.

Project Overview

The E-Commerce Price Tracker ETL Pipeline is designed to collect product information from e-commerce websites and transform it into a structured dataset that can be used to monitor product prices and analyze pricing trends.

The pipeline follows the standard ETL workflow:


E-Commerce Website
       │
       ▼
   Extraction
       │
       ▼
 Data Cleaning
       │
       ▼
 Transformation
       │
       ▼
 Database Loading
       │
       ▼
 Structured Product Data


Objectives

* Extract product information from e-commerce websites.
* Automate the collection of product prices.
* Clean and standardize raw scraped data.
* Transform the data into a structured format.
* Store processed data in a database.
* Build a reusable ETL pipeline.
* Create a foundation for future price-tracking and analytics features.

 Key Features

* Web scraping for product data extraction
* Automated ETL workflow
* Data cleaning and preprocessing
* Price extraction and standardization
* Duplicate data handling
* Structured database storage
* Timestamped price records
* Error handling during extraction
* Modular Python-based architecture
* Ready for future scheduling and analytics

Technologies Used

| Technology    | Purpose                          |
| ------------- | -------------------------------- |
| Python        | Core programming language        |
| Requests      | Sending HTTP requests            |
| BeautifulSoup | HTML parsing and web scraping    |
| Pandas        | Data cleaning and transformation |
| PostgreSQL    | Structured data storage          |
| SQLAlchemy    | Database connection and ORM      |
| Git           | Version control                  |
| GitHub        | Project hosting                  |

ETL Pipeline

1. Extract

The extraction stage sends HTTP requests to the target e-commerce website and retrieves the required HTML content.

BeautifulSoup is then used to parse the HTML and extract relevant product information such as:

* Product name
* Product price
* Product URL
* Product category
* Availability
* Scraping timestamp

Example raw data:

```text
Product Name: Wireless Headphones
Price: Rs. 5,999
Category: Electronics
Availability: In Stock
```

2. Transform

The raw scraped data is cleaned and transformed before being stored.

Transformation operations include:

* Removing unnecessary characters
* Cleaning product names
* Converting prices into numeric values
* Handling missing values
* Removing duplicate records
* Standardizing data formats
* Creating timestamps
* Validating product records

Example:

```text
Raw Price:
"Rs. 5,999"

        ↓

Cleaned Price:
5999
```

 3. Load

The transformed data is loaded into a PostgreSQL database using SQLAlchemy.

A typical product record contains:

```text
product_id
product_name
price
category
availability
product_url
scraped_at
```

The database allows historical product prices to be stored and analyzed over time.

 Project Architecture

```text
                    ┌──────────────────────┐
                    │   E-Commerce Website │
                    └──────────┬───────────┘
                               │
                               ▼
                    ┌──────────────────────┐
                    │   Web Scraper        │
                    │ Requests + BeautifulSoup
                    └──────────┬───────────┘
                               │
                               ▼
                    ┌──────────────────────┐
                    │   Raw Product Data  │
                    └──────────┬───────────┘
                               │
                               ▼
                    ┌──────────────────────┐
                    │ Data Transformation  │
                    │      Pandas          │
                    └──────────┬───────────┘
                               │
                               ▼
                    ┌──────────────────────┐
                    │   Data Validation    │
                    └──────────┬───────────┘
                               │
                               ▼
                    ┌──────────────────────┐
                    │     PostgreSQL       │
                    │      Database       │
                    └──────────┬───────────┘
                               │
                               ▼
                    ┌──────────────────────┐
                    │ Price Analysis / BI  │
                    └──────────────────────┘
```

 Project Structure

```text
ecommerce-price-tracker-etl/
│
├── src/
│   ├── scraper.py
│   ├── transform.py
│   ├── database.py
│   └── pipeline.py
│
├── data/
│   └── .gitkeep
│
├── requirements.txt
├── README.md
├── .gitignore
└── main.py
```

> The exact structure may vary depending on the implementation.

Installation

### 1. Clone the Repository

```bash
git clone https://github.com/YOUR_USERNAME/ecommerce-price-tracker-etl.git
```

### 2. Navigate to the Project

```bash
cd ecommerce-price-tracker-etl
```

### 3. Create a Virtual Environment

Windows:

```bash
python -m venv venv
```

Activate it:

```bash
venv\Scripts\activate
```

### 4. Install Dependencies

```bash
pip install -r requirements.txt
```

## Database Configuration

Create a PostgreSQL database and configure the database connection using environment variables.

Create a `.env` file:

```env
DATABASE_URL=postgresql://username:password@localhost:5432/ecommerce_tracker
```

**Do not commit your `.env` file to GitHub.**

Add it to `.gitignore`:

```text
.env
venv/
.venv/
__pycache__/
*.pyc
```

## Sample Dataset

Example processed records:

| Product             | Price | Category    | Availability |
| ------------------- | ----: | ----------- | ------------ |
| Wireless Headphones |  5999 | Electronics | In Stock     |
| Gaming Mouse        |  3499 | Electronics | In Stock     |
| Mechanical Keyboard |  8499 | Electronics | Out of Stock |
| USB-C Hub           |  2799 | Accessories | In Stock     |

## Database Design

The project stores product information in a structured relational database.

Example table:

```sql
CREATE TABLE products (
    product_id SERIAL PRIMARY KEY,
    product_name VARCHAR(255),
    price DECIMAL(10,2),
    category VARCHAR(100),
    availability VARCHAR(50),
    product_url TEXT,
    scraped_at TIMESTAMP
);
```

Historical price records can be used to identify:

* Price increases
* Price decreases
* Product availability changes
* Cheapest products
* Price trends over time

## Data Quality

The pipeline applies basic data-quality checks such as:

* Missing-value handling
* Duplicate detection
* Price validation
* Data-type validation
* URL validation
* Product-name cleaning

This helps ensure that only usable and consistent records are loaded into the database.


Through this project, I practiced:

* Web scraping
* Python programming
* HTML parsing
* Data extraction
* Data cleaning
* Data transformation
* ETL pipeline development
* PostgreSQL database management
* SQLAlchemy
* Data validation
* Git and GitHub
* Data Engineering workflow design

## Challenges

Some challenges addressed during development include:

* Handling inconsistent HTML structures
* Cleaning price values from scraped text
* Managing missing product information
* Avoiding duplicate records
* Handling HTTP request failures
* Designing a reliable database schema
* Separating extraction, transformation, and loading logic

Author
Faizan

Aspiring Data Engineer | Data Analyst | Python Developer

Skills Demonstrated

`Python` · `Web Scraping` · `BeautifulSoup` · `Pandas` · `SQL` · `PostgreSQL` · `SQLAlchemy` · `ETL` · `Data Engineering` · `Git` · `GitHub`

---

⭐ If you find this project useful, consider giving the repository a star.
