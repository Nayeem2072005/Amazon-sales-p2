# Amazon India Sales Analytics

## Project Overview

This project is an end-to-end Data Analytics project developed using Python, PostgreSQL, SQL, Power BI, and Streamlit.

The objective of this project is to analyze Amazon India sales data, perform data cleaning, conduct exploratory data analysis (EDA), execute SQL-based business analysis, and visualize insights through an interactive dashboard.

---

## Technologies Used

- Python
- Pandas
- Matplotlib
- PostgreSQL
- SQL
- Streamlit
- Power BI

---

## Project Workflow

```
Raw Dataset
     │
     ▼
Data Loading
     │
     ▼
Data Cleaning
     │
     ▼
Exploratory Data Analysis
     │
     ▼
PostgreSQL Database
     │
     ▼
SQL Analysis
     │
     ▼
Power BI Dashboard
     │
     ▼
Streamlit Web Application
```

---

## Project Structure

```
Amazon-India-Sales-Analytics/
│
├── app.py
├── README.md
├── requirements.txt
│
├── cleaned_data/
├── dataset/
├── notebooks/
│   ├── 01_data_loading.ipynb
│   ├── data_cleaning.ipynb
│   └── eda.ipynb
│
├── plots/
├── powerbi/
├── scripts/
└── sql/
```

---

## Project Modules

### 1. Data Loading

- Imported yearly Amazon India sales datasets
- Merged multiple datasets into a single dataset
- Verified dataset structure

### 2. Data Cleaning

- Handled missing values
- Removed duplicate records
- Converted data types
- Standardized categorical columns
- Created derived columns for analysis
- Exported cleaned dataset

### 3. Exploratory Data Analysis

Performed business analysis using Matplotlib, including:

- Yearly Revenue Analysis
- Monthly Revenue Analysis
- Revenue by Customer Tier
- Revenue by Product Category
- Top Brands by Revenue
- Revenue by State
- Payment Method Analysis
- Prime vs Non-Prime Analysis
- Customer Age Group Analysis
- Delivery Analysis
- Customer City Analysis
- Product Rating Analysis
- Spending Tier Analysis
- Discount Analysis
- Delivery Type Analysis
- Return Status Analysis
- Quarterly Revenue Analysis
- Festival Sale Analysis
- Product Weight Analysis
- Executive Dashboard Summary

---

## PostgreSQL

- Created Amazon Sales database
- Created sales table
- Imported cleaned dataset
- Connected PostgreSQL with Python using psycopg2

---

## SQL Analysis

Performed SQL queries to analyze:

- Total Revenue
- Total Orders
- Revenue by Brand
- Revenue by State
- Monthly Revenue
- Payment Method Analysis
- Prime Member Analysis
- Product Category Analysis
- Customer Analysis
- Business Insights

---

## Power BI Dashboard

Created an interactive dashboard containing:

- KPI Cards
- Revenue Trend
- Top Brands
- State-wise Orders
- Prime vs Non-Prime Orders
- Festival Sales
- Payment Method Distribution
- Product Category Analysis

---

## Streamlit Application

The web application contains:

- Home
- Data Loading & Cleaning
- EDA Analysis
- SQL Analysis
- Power BI Dashboard
- About Project

---

## How to Run

### Install the required libraries

```bash
pip install -r requirements.txt
```

### Run the Streamlit application

```bash
streamlit run app.py
```

---

## Libraries Used

- streamlit
- pandas
- matplotlib
- psycopg2-binary

---

## Author

Nayeem Mohammed
