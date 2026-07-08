import psycopg2
import pandas as pd

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

print(df.head())

conn.close()