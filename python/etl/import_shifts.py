import os
import pandas as pd
import psycopg2

from dotenv import load_dotenv

load_dotenv()

shifts = pd.read_csv("data/generated/shifts.csv")


print(shifts.head())
print(shifts.info())
print(shifts.shape)



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
INSERT INTO shifts (
    employee_id,
    branch_id,
    shift_date,
    shift_start,
    shift_end,
    hours_worked,
    shift_type,
    work_area,
    overtime_hours,
    shift_status
)
VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
on conflict (employee_id, branch_id, shift_date, shift_start) do nothing
"""


for _, row in shifts.iterrows():
    cursor.execute(
        insert_query,
        (
            row["employee_id"],
            row["branch_id"],
            row["shift_date"],
            row["shift_start"],
            row["shift_end"],
            row["hours_worked"],
            row["shift_type"],
            row["work_area"],
            row["overtime_hours"],
            row["shift_status"]
        )
    )
    
connection.commit()

print(f"{len(shifts)} rows inserted successfully!")

cursor.close()
connection.close()

print("Database connection closed.")