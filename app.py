import streamlit as st
import pandas as pd
import psycopg2
import matplotlib.pyplot as plt

# -------------------------------
# PAGE CONFIGURATION
# -------------------------------

st.set_page_config(
    page_title="Amazon India Sales Analytics",
    page_icon="🛒",
    layout="wide"
)

# -------------------------------
# DATABASE CONNECTION
# -------------------------------

@st.cache_data
def load_data():

    conn = psycopg2.connect(
        host="localhost",
        database="amazon_sales_db",
        user="postgres",
        password="naiim@2482",
        port="5432"
    )

    df = pd.read_sql_query(
        "SELECT * FROM amazon_sales;",
        conn
    )

    conn.close()

    return df


df = load_data()

# -------------------------------
# SIDEBAR
# -------------------------------

st.sidebar.title("Navigation")

page = st.sidebar.radio(
    "Go To",
    [
        "Home",
        "Data Loading & Cleaning",
        "EDA Analysis",
        "PostgreSQL",
        "SQL Analysis",
        "Power BI Dashboard",
        "About Project"
    ]
)

import psycopg2
import pandas as pd

@st.cache_resource
def get_connection():
    return psycopg2.connect(
        host="localhost",
        database="amazon_sales_db",
        user="postgres",
        password="naiim@2482",
        port="5432"
    )

conn = get_connection()

# ==========================================================
# HOME PAGE
# ==========================================================

if page == "Home":

    st.title("🛒 Amazon India Sales Analytics")

    st.write("---")

    st.header("Project Overview")

    st.write("""
This project analyzes Amazon India sales data using

• Python

• PostgreSQL

• SQL

• Power BI

• Streamlit
""")

    st.write("---")

    st.subheader("Dataset")

    st.write(f"Total Rows : {len(df):,}")

    st.write(f"Total Columns : {len(df.columns)}")

    st.dataframe(df.head())

    st.write("---")

    st.subheader("Column Names")

    st.write(df.columns.tolist())

# ==========================================================
# DATA LOADING & CLEANING
# ==========================================================

if page == "Data Loading & Cleaning":

    st.title("📂 Data Loading & Cleaning")

    st.write(
        """
The dataset was loaded using Pandas by combining
multiple yearly Amazon sales datasets into one dataset.
"""
    )

    st.subheader("Dataset Loading")

    st.code("""
import pandas as pd

df_2015 = pd.read_csv("../dataset/amazon_india_2015.csv")
df_2016 = pd.read_csv("../dataset/amazon_india_2016.csv")
...
df_2025 = pd.read_csv("../dataset/amazon_india_2025.csv")

merged_df = pd.concat([
    df_2015,
    df_2016,
    ...
    df_2025
], ignore_index=True)
""", language="python")

    st.write("---")

    st.subheader("Cleaning Steps Performed")

    st.write("✅ Standardized order_date column")
    st.write("✅ Cleaned original_price_inr column")
    st.write("✅ Standardized customer_rating")
    st.write("✅ Filled missing customer ratings")
    st.write("✅ Standardized customer_city names")
    st.write("✅ Standardized boolean columns")
    st.write("✅ Standardized category names")
    st.write("✅ Cleaned delivery_days")
    st.write("✅ Checked duplicate transactions")
    st.write("✅ Handled outlier prices")
    st.write("✅ Standardized payment methods")

    st.write("---")

    st.subheader("Sample Cleaning Code")

    st.code("""
# Convert order_date

merged_df["order_date"] = pd.to_datetime(
    merged_df["order_date"],
    format="mixed",
    dayfirst=True
)

# Clean customer ratings

merged_df["customer_rating"] = (
    merged_df["customer_rating"]
    .str.replace(" stars","")
    .str.split("/")
    .str[0]
)

merged_df["customer_rating"] = pd.to_numeric(
    merged_df["customer_rating"],
    errors="coerce"
)

merged_df["customer_rating"] = (
    merged_df["customer_rating"]
    .fillna(
        merged_df["customer_rating"].mean()
    )
)
""", language="python")

    st.write("---")

    st.subheader("Cleaned Dataset Preview")

    st.dataframe(df.head())

    st.write("Rows :", len(df))
    st.write("Columns :", len(df.columns))

# ==========================================================
# EDA ANALYSIS
# ==========================================================

if page == "EDA Analysis":

    st.title("📊 Exploratory Data Analysis (EDA)")

    st.write("This section contains all 20 EDA questions performed during the project.")

    st.write("---")

    # ==========================================================
    # ==========================================================
    # QUESTION 1 : Yearly Revenue Trend
    # ==========================================================

    st.subheader("Question 1 : Yearly Revenue Trend")

    yearly = (
        df.groupby("order_year")["final_amount_inr"]
        .sum()
        .reset_index()
    )

    fig, ax = plt.subplots(figsize=(12,6))

    ax.plot(
        yearly["order_year"],
        yearly["final_amount_inr"],
        marker="o",
        linewidth=2
    )

    ax.set_title("Yearly Revenue Trend")
    ax.set_xlabel("Year")
    ax.set_ylabel("Revenue (INR)")

    ax.grid(True)

    st.pyplot(fig)

    plt.close(fig)

    st.info(
        "Insight: Shows how revenue changed from year to year."
    )

    st.write("---")


    # ==========================================================
    # QUESTION 2 : Monthly Revenue
    # ==========================================================

    st.subheader("Question 2 : Monthly Revenue")

    monthly = (
        df.groupby("order_month")["final_amount_inr"]
        .sum()
        .reset_index()
    )

    fig, ax = plt.subplots(figsize=(12,6))

    ax.bar(
        monthly["order_month"].astype(str),
        monthly["final_amount_inr"]
    )

    ax.set_title("Monthly Revenue")
    ax.set_xlabel("Month")
    ax.set_ylabel("Revenue (INR)")

    ax.grid(axis="y")

    st.pyplot(fig)

    plt.close(fig)

    st.info("Insight: Identifies the months with the highest revenue.")

    st.write("---")

    # ==========================================================
    # QUESTION 3 : Revenue by Customer Tier
    # ==========================================================

    st.subheader("Question 3 : Revenue by Customer Tier")

    tier = (
        df.groupby("customer_tier")["final_amount_inr"]
        .sum()
        .reset_index()
    )

    fig, ax = plt.subplots(figsize=(10,6))

    ax.bar(
        tier["customer_tier"],
        tier["final_amount_inr"]
    )

    ax.set_title("Revenue by Customer Tier")
    ax.set_xlabel("Customer Tier")
    ax.set_ylabel("Revenue (INR)")

    ax.grid(axis="y")

    st.pyplot(fig)

    plt.close(fig)

    st.info("Insight: Compares revenue generated by each customer tier.")

    st.write("---")

    # ==========================================================
    # QUESTION 4 : Revenue by Product Category
    # ==========================================================

    st.subheader("Question 4 : Revenue by Product Category")

    category = (
        df.groupby("category")["final_amount_inr"]
        .sum()
        .reset_index()
    )

    fig, ax = plt.subplots(figsize=(12,6))

    ax.bar(
        category["category"],
        category["final_amount_inr"]
    )

    ax.set_title("Revenue by Product Category")
    ax.set_xlabel("Category")
    ax.set_ylabel("Revenue (INR)")

    plt.xticks(rotation=45)

    ax.grid(axis="y")

    st.pyplot(fig)

    plt.close(fig)

    st.info("Insight: Shows which product categories generate the highest revenue.")

    st.write("---")

    # ==========================================================
    # QUESTION 5 : Revenue by Brand
    # ==========================================================

    st.subheader("Question 5 : Revenue by Brand")

    brand = (
        df.groupby("brand")["final_amount_inr"]
        .sum()
        .sort_values(ascending=False)
        .head(10)
        .reset_index()
    )

    fig, ax = plt.subplots(figsize=(12,6))

    ax.bar(
        brand["brand"],
        brand["final_amount_inr"]
    )

    ax.set_title("Top 10 Brands by Revenue")
    ax.set_xlabel("Brand")
    ax.set_ylabel("Revenue (INR)")

    plt.xticks(rotation=45)

    ax.grid(axis="y")

    st.pyplot(fig)

    plt.close(fig)

    st.info("Insight: Displays the top revenue-generating brands.")

    st.write("---")

    # ==========================================================
    # QUESTION 6 : Revenue by State
    # ==========================================================

    st.subheader("Question 6 : Revenue by State")

    state = (
        df.groupby("customer_state")["final_amount_inr"]
        .sum()
        .reset_index()
    )

    fig, ax = plt.subplots(figsize=(14,6))

    ax.bar(
        state["customer_state"],
        state["final_amount_inr"]
    )

    ax.set_title("Revenue by State")
    ax.set_xlabel("State")
    ax.set_ylabel("Revenue (INR)")

    plt.xticks(rotation=90)

    ax.grid(axis="y")

    st.pyplot(fig)

    plt.close(fig)

    st.info("Insight: Shows revenue generated by each state.")

    st.write("---")

    # ==========================================================
    # QUESTION 7 : Revenue by Payment Method
    # ==========================================================

    st.subheader("Question 7 : Revenue by Payment Method")

    payment = (
        df.groupby("payment_method")["final_amount_inr"]
        .sum()
        .reset_index()
    )

    fig, ax = plt.subplots(figsize=(8,8))

    ax.pie(
        payment["final_amount_inr"],
        labels=payment["payment_method"],
        autopct="%1.1f%%",
        startangle=90
    )

    ax.set_title("Revenue by Payment Method")

    st.pyplot(fig)

    plt.close(fig)

    st.info("Insight: Displays revenue contribution by payment method.")

    st.write("---")


    # ==========================================================
    # QUESTION 8 : Revenue by Prime Membership
    # ==========================================================

    st.subheader("Question 8 : Revenue by Prime Membership")

    prime = (
        df.groupby("is_prime_member")["final_amount_inr"]
        .sum()
        .reset_index()
    )

    fig, ax = plt.subplots(figsize=(8,6))

    ax.bar(
        prime["is_prime_member"].astype(str),
        prime["final_amount_inr"]
    )

    ax.set_title("Revenue by Prime Membership")
    ax.set_xlabel("Prime Member")
    ax.set_ylabel("Revenue (INR)")

    ax.grid(axis="y")

    st.pyplot(fig)

    plt.close(fig)

    st.info("Insight: Compares revenue generated by Prime and Non-Prime members.")

    st.write("---")


    # ==========================================================
    # QUESTION 9 : Revenue by Customer Age Group
    # ==========================================================

    st.subheader("Question 9 : Revenue by Customer Age Group")

    age = (
        df.groupby("customer_age_group")["final_amount_inr"]
        .sum()
        .reset_index()
    )

    fig, ax = plt.subplots(figsize=(10,6))

    ax.bar(
        age["customer_age_group"],
        age["final_amount_inr"]
    )

    ax.set_title("Revenue by Customer Age Group")
    ax.set_xlabel("Age Group")
    ax.set_ylabel("Revenue (INR)")

    ax.grid(axis="y")

    st.pyplot(fig)

    plt.close(fig)

    st.info("Insight: Shows revenue generated by different customer age groups.")

    st.write("---")

    # ==========================================================
    # QUESTION 10 : Revenue by Delivery Days
    # ==========================================================

    st.subheader("Question 10 : Revenue by Delivery Days")

    delivery = (
        df.groupby("delivery_days")["final_amount_inr"]
        .sum()
        .reset_index()
    )

    fig, ax = plt.subplots(figsize=(12,6))

    ax.bar(
        delivery["delivery_days"].astype(str),
        delivery["final_amount_inr"]
    )

    ax.set_title("Revenue by Delivery Days")
    ax.set_xlabel("Delivery Days")
    ax.set_ylabel("Revenue (INR)")

    ax.grid(axis="y")

    st.pyplot(fig)

    plt.close(fig)

    st.info("Insight: Shows how delivery duration affects revenue.")

    st.write("---")

    # ==========================================================
    # QUESTION 11 : Revenue by Customer City
    # ==========================================================

    st.subheader("Question 11 : Revenue by Customer City")

    city = (
        df.groupby("customer_city")["final_amount_inr"]
        .sum()
        .sort_values(ascending=False)
        .head(10)
        .reset_index()
    )

    fig, ax = plt.subplots(figsize=(12,6))

    ax.bar(
        city["customer_city"],
        city["final_amount_inr"]
    )

    ax.set_title("Top 10 Cities by Revenue")
    ax.set_xlabel("Customer City")
    ax.set_ylabel("Revenue (INR)")

    plt.xticks(rotation=45)

    ax.grid(axis="y")

    st.pyplot(fig)

    plt.close(fig)

    st.info("Insight: Displays the top 10 revenue-generating cities.")

    st.write("---")

    # ==========================================================
    # QUESTION 12 : Revenue by Product Rating
    # ==========================================================

    st.subheader("Question 12 : Revenue by Product Rating")

    rating = (
        df.groupby("product_rating")["final_amount_inr"]
        .sum()
        .reset_index()
    )

    fig, ax = plt.subplots(figsize=(10,6))

    ax.bar(
        rating["product_rating"].astype(str),
        rating["final_amount_inr"]
    )

    ax.set_title("Revenue by Product Rating")
    ax.set_xlabel("Product Rating")
    ax.set_ylabel("Revenue (INR)")

    ax.grid(axis="y")

    st.pyplot(fig)

    plt.close(fig)

    st.info("Insight: Shows how ratings influence revenue.")

    st.write("---")


    # ==========================================================
    # QUESTION 13 : Revenue by Customer Spending Tier
    # ==========================================================

    st.subheader("Question 13 : Revenue by Customer Spending Tier")

    spending = (
        df.groupby("customer_spending_tier")["final_amount_inr"]
        .sum()
        .reset_index()
    )

    fig, ax = plt.subplots(figsize=(10,6))

    ax.bar(
        spending["customer_spending_tier"],
        spending["final_amount_inr"]
    )

    ax.set_title("Revenue by Customer Spending Tier")
    ax.set_xlabel("Customer Spending Tier")
    ax.set_ylabel("Revenue (INR)")

    ax.grid(axis="y")

    st.pyplot(fig)

    plt.close(fig)

    st.info("Insight: Compares revenue across customer spending tiers.")

    st.write("---")

    # ==========================================================
    # QUESTION 14 : Revenue by Discount Percentage
    # ==========================================================

    st.subheader("Question 14 : Revenue by Discount Percentage")

    discount = (
        df.groupby("discount_percent")["final_amount_inr"]
        .sum()
        .sort_values(ascending=False)
        .head(10)
        .reset_index()
    )

    fig, ax = plt.subplots(figsize=(12,6))

    ax.bar(
        discount["discount_percent"].astype(str),
        discount["final_amount_inr"]
    )

    ax.set_title("Top 10 Discount Percentages by Revenue")
    ax.set_xlabel("Discount Percentage")
    ax.set_ylabel("Revenue (INR)")

    plt.xticks(rotation=45)

    ax.grid(axis="y")

    st.pyplot(fig)

    plt.close(fig)

    st.info("Insight: Shows which discount percentages generate the highest revenue.")

    st.write("---")

    # ==========================================================
    # QUESTION 15 : Revenue by Delivery Type
    # ==========================================================

    st.subheader("Question 15 : Revenue by Delivery Type")

    delivery_type = (
        df.groupby("delivery_type")["final_amount_inr"]
        .sum()
        .reset_index()
    )

    fig, ax = plt.subplots(figsize=(10,6))

    ax.bar(
        delivery_type["delivery_type"],
        delivery_type["final_amount_inr"]
    )

    ax.set_title("Revenue by Delivery Type")
    ax.set_xlabel("Delivery Type")
    ax.set_ylabel("Revenue (INR)")

    ax.grid(axis="y")

    st.pyplot(fig)

    plt.close(fig)

    st.info("Insight: Shows revenue generated by each delivery type.")

    st.write("---")

    # ==========================================================
    # QUESTION 16 : Revenue by Return Status
    # ==========================================================

    st.subheader("Question 16 : Revenue by Return Status")

    returns = (
        df.groupby("return_status")["final_amount_inr"]
        .sum()
        .reset_index()
    )

    fig, ax = plt.subplots(figsize=(8,6))

    ax.bar(
        returns["return_status"].astype(str),
        returns["final_amount_inr"]
    )

    ax.set_title("Revenue by Return Status")
    ax.set_xlabel("Return Status")
    ax.set_ylabel("Revenue (INR)")

    ax.grid(axis="y")

    st.pyplot(fig)

    plt.close(fig)

    st.info("Insight: Compares revenue from returned and non-returned orders.")

    st.write("---")


    # ==========================================================
    # QUESTION 17 : Revenue by Order Quarter
    # ==========================================================

    st.subheader("Question 17 : Revenue by Order Quarter")

    quarter = (
        df.groupby("order_quarter")["final_amount_inr"]
        .sum()
        .reset_index()
    )

    fig, ax = plt.subplots(figsize=(8,6))

    ax.bar(
        quarter["order_quarter"],
        quarter["final_amount_inr"]
    )

    ax.set_title("Revenue by Order Quarter")
    ax.set_xlabel("Quarter")
    ax.set_ylabel("Revenue (INR)")

    ax.grid(axis="y")

    st.pyplot(fig)

    plt.close(fig)

    st.info("Insight: Displays quarterly revenue.")

    st.write("---")

    # ==========================================================
    # QUESTION 18 : Revenue by Festival Sale
    # ==========================================================

    st.subheader("Question 18 : Revenue by Festival Sale")

    festival = (
        df.groupby("is_festival_sale")["final_amount_inr"]
        .sum()
        .reset_index()
    )

    fig, ax = plt.subplots(figsize=(8,6))

    ax.bar(
        festival["is_festival_sale"].astype(str),
        festival["final_amount_inr"]
    )

    ax.set_title("Festival Sale Revenue")
    ax.set_xlabel("Festival Sale")
    ax.set_ylabel("Revenue (INR)")

    ax.grid(axis="y")

    st.pyplot(fig)

    plt.close(fig)

    st.info("Insight: Compares revenue during festival and non-festival sales.")

    st.write("---")


    # ==========================================================
    # QUESTION 19 : Revenue by Product Weight
    # ==========================================================

    st.subheader("Question 19 : Top 10 Product Weights by Revenue")

    weight = (
        df.groupby("product_weight_kg")["final_amount_inr"]
        .sum()
        .sort_values(ascending=False)
        .head(10)
        .reset_index()
    )

    fig, ax = plt.subplots(figsize=(12,6))

    ax.bar(
        weight["product_weight_kg"].astype(str),
        weight["final_amount_inr"]
    )

    ax.set_title("Top 10 Product Weights by Revenue")
    ax.set_xlabel("Product Weight (kg)")
    ax.set_ylabel("Revenue (INR)")

    ax.grid(axis="y")

    plt.xticks(rotation=45)

    st.pyplot(fig)

    plt.close(fig)

    st.info("Insight: Displays the product weights generating the highest revenue.")

    st.write("---")


    # ==========================================================
    # QUESTION 20 : Executive Dashboard
    # ==========================================================

    st.subheader("Question 20 : Executive Sales Dashboard")

    col1, col2, col3 = st.columns(3)

    col1.metric("Total Revenue", f"₹ {df['final_amount_inr'].sum():,.2f}")
    col2.metric("Total Orders", f"{len(df):,}")
    col3.metric("Average Order Value", f"₹ {df['final_amount_inr'].mean():,.2f}")

    st.write("---")

    top5 = (
        df.groupby("brand")["final_amount_inr"]
        .sum()
        .sort_values(ascending=False)
        .head(5)
        .reset_index()
    )

    fig, ax = plt.subplots(figsize=(10,5))

    ax.bar(
        top5["brand"],
        top5["final_amount_inr"]
    )

    ax.set_title("Top 5 Brands by Revenue")
    ax.set_xlabel("Brand")
    ax.set_ylabel("Revenue (INR)")

    ax.grid(axis="y")

    plt.xticks(rotation=30)

    st.pyplot(fig)

    plt.close(fig)



    st.subheader("Question 21 : RFM Customer Segmentation")
    rfm = pd.read_csv("outputs/rfm_segments.csv")
    segment_counts = rfm["segment"].value_counts()
    fig, ax = plt.subplots()
    ax.bar(segment_counts.index, segment_counts.values, color="steelblue")
    ax.set_xlabel("Segment")
    ax.set_ylabel("Number of Customers")
    plt.xticks(rotation=15)
    st.pyplot(fig)
    st.write(segment_counts)
    
# ==========================================================
# SQL ANALYSIS
# ==========================================================

if page == "SQL Analysis":

    st.title("💻 SQL Analysis")

    st.write("The following SQL queries were executed in PostgreSQL.")

    st.write("---")

    # Query 1
    st.subheader("Query 1 - Total Revenue")
    st.code("SELECT SUM(final_amount_inr) FROM amazon_sales;", language="sql")
    result = pd.read_sql_query("SELECT SUM(final_amount_inr) AS total FROM amazon_sales;", conn)
    st.success(f"Total Revenue : ₹ {result['total'][0]:,.2f}")

    revenue = df["final_amount_inr"].sum()

    st.success(f"Result : ₹ {revenue:,.2f}")

    st.write("---")

    # Query 2
    st.subheader("Query 2 - Total Orders")

    st.code("""
SELECT COUNT(transaction_id)
FROM amazon_sales;
""", language="sql")

    orders = df["transaction_id"].count()

    st.success(f"Result : {orders:,}")

    st.write("---")

    # Query 3
    st.subheader("Query 3 - Top 10 Brands")

    st.code("""
SELECT brand,
SUM(final_amount_inr)
FROM amazon_sales
GROUP BY brand
ORDER BY SUM(final_amount_inr) DESC
LIMIT 10;
""", language="sql")

    top_brand = (
        df.groupby("brand")["final_amount_inr"]
        .sum()
        .sort_values(ascending=False)
        .head(10)
    )

    st.dataframe(top_brand)

    st.write("---")

    # Query 4
    st.subheader("Query 4 - Orders by State")

    st.code("""
SELECT customer_state,
COUNT(transaction_id)
FROM amazon_sales
GROUP BY customer_state;
""", language="sql")

    state = (
        df.groupby("customer_state")["transaction_id"]
        .count()
        .sort_values(ascending=False)
    )

    st.dataframe(state)

    st.write("---")

    # Query 5
    st.subheader("Query 5 - Payment Methods")

    st.code("""
SELECT payment_method,
COUNT(*)
FROM amazon_sales
GROUP BY payment_method;
""", language="sql")

    payment = df["payment_method"].value_counts()

    st.dataframe(payment)

    st.write("---")

    # Query 6
    st.subheader("Query 6 - Prime Orders")

    st.code("""
SELECT is_prime_member,
COUNT(*)
FROM amazon_sales
GROUP BY is_prime_member;
""", language="sql")

    prime = df["is_prime_member"].value_counts()

    st.dataframe(prime)

    st.write("---")

    # Query 7
    st.subheader("Query 7 - Festival Sales")

    st.code("""
SELECT is_festival_sale,
SUM(final_amount_inr)
FROM amazon_sales
GROUP BY is_festival_sale;
""", language="sql")

    festival = (
        df.groupby("is_festival_sale")["final_amount_inr"]
        .sum()
    )

    st.dataframe(festival)

    st.write("---")

    # Query 8
    st.subheader("Query 8 - Revenue by Category")

    st.code("""
SELECT category,
SUM(final_amount_inr)
FROM amazon_sales
GROUP BY category;
""", language="sql")

    category = (
        df.groupby("category")["final_amount_inr"]
        .sum()
    )

    st.dataframe(category)

    st.write("---")

    # Query 9
    st.subheader("Query 9 - Revenue by Subcategory")

    st.code("""
SELECT subcategory,
SUM(final_amount_inr)
FROM amazon_sales
GROUP BY subcategory;
""", language="sql")

    subcategory = (
        df.groupby("subcategory")["final_amount_inr"]
        .sum()
    )

    st.dataframe(subcategory)

    st.write("---")

    # Query 10
    st.subheader("Query 10 - Average Order Value")

    st.code("""
SELECT AVG(final_amount_inr)
FROM amazon_sales;
""", language="sql")

    avg = df["final_amount_inr"].mean()

    st.success(f"Average Order Value : ₹ {avg:,.2f}")

    st.write("---")

    # Query 11
    st.subheader("Query 11 - Top Customer States by Revenue (via JOIN)")

    st.code("""
SELECT c.customer_state, SUM(a.final_amount_inr) AS total_revenue
FROM amazon_sales a
JOIN customers c ON a.customer_id = c.customer_id
GROUP BY c.customer_state
ORDER BY total_revenue DESC
LIMIT 10;
""", language="sql")

    customers_lookup = df[["customer_id", "customer_state"]].drop_duplicates()
    joined = df[["customer_id", "final_amount_inr"]].merge(customers_lookup, on="customer_id")
    top_states = (
        joined.groupby("customer_state")["final_amount_inr"]
        .sum()
        .sort_values(ascending=False)
        .head(10)
    )

    st.dataframe(top_states)


# ==========================================================
# POWER BI DASHBOARD
# ==========================================================

if page == "Power BI Dashboard":

    st.title("📊 Power BI Dashboard")

    st.write("""
The Power BI Dashboard was created separately using Microsoft Power BI Desktop.

The dashboard contains:

- KPI Cards

- Monthly Revenue Trend

- Top 10 Brands

- Revenue by State

- Revenue by Subcategory

- Payment Method Analysis

- Prime vs Non Prime Orders

- Festival Sales Analysis
""")

    st.image("powerbi/amazon_dashboard.png", caption="Amazon India Sales Dashboard (Power BI)", use_column_width=True)

    st.info("Open the Power BI (.pbix) file in this repository to view and interact with the full dashboard, including cross-filtering between charts.")

# ==========================================================
# ABOUT PROJECT
# ==========================================================

if page == "About Project":

    st.title("ℹ️ About Project")

    st.header("Project Name")

    st.write("Amazon India Sales Analytics")

    st.header("Technologies Used")

    st.write("""
- Python
- Pandas
- PostgreSQL
- SQL
- Power BI
- Streamlit
""")

    st.header("Project Workflow")

    st.write("""
1. Data Collection

2. Data Cleaning

3. Exploratory Data Analysis

4. PostgreSQL Database

5. SQL Analysis

6. Power BI Dashboard

7. Streamlit Web Application
""")

    st.header("Dataset Information")

    st.write(f"Rows : {len(df):,}")
    st.write(f"Columns : {len(df.columns)}")

    st.header("Developer")

    st.write("Developed as a Data Analytics Project.")