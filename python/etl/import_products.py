import os
import pandas as pd
import psycopg2

from dotenv import load_dotenv

load_dotenv()

products = pd.read_excel("data/raw/products.xlsx")

# print(products.head())
# print(products.info())
# print(products.shape)
# print(products.columns)


products = products.drop(columns=["Gross Profit", "Food Cost %"])

products = products.rename(columns={
    "SKU": "sku",
    "Product Name": "product_name",
    "Category": "category",
    "Subcategory": "subcategory",
    "Product Size": "product_size",
    "Serving Temperature": "serving_temperature",
    "Selling Price": "selling_price",
    "Food Cost": "food_cost",
    "Preparation Time (min)": "preparation_time",
    "Calories": "calories",
    "Menu Status": "menu_status",
    "Supplier": "supplier",
    "Created Date": "created_date"
})

# print(products["serving_temperature"].unique())

# print(products[products["selling_price"] <= 0])

# print(products[products["food_cost"] > products["selling_price"]])

# print(products.isnull().sum())

# print(products["sku"].duplicated().sum())

# print(sorted(products["subcategory"].unique()))

# print(products.head())
# print(products.columns)
# print(products.shape)
# print(products.info())




connection = psycopg2.connect(
    host=os.getenv("DB_HOST"),
    port=os.getenv("DB_PORT"),
    database=os.getenv("DB_NAME"),
    user=os.getenv("DB_USER"),
    password=os.getenv("DB_PASSWORD")
)

print("Connected successfully!")





cursor = connection.cursor()

insert_query = """
INSERT INTO products (
    sku,
    product_name,
    category,
    subcategory,
    product_size,
    serving_temperature,
    selling_price,
    food_cost,
    preparation_time,
    calories,
    menu_status,
    supplier,
    created_date
)
VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
on conflict (sku) do nothing
"""


for _, row in products.iterrows():
    cursor.execute(
        insert_query,
        (
            row["sku"],
            row["product_name"],
            row["category"],
            row["subcategory"],
            row["product_size"],
            row["serving_temperature"],
            row["selling_price"],
            row["food_cost"],
            row["preparation_time"],
            row["calories"],
            row["menu_status"],
            row["supplier"],
            row["created_date"]
        )
    )
    
    
connection.commit()

print(f"{len(products)} products inserted successfully!")

cursor.close()
connection.close()