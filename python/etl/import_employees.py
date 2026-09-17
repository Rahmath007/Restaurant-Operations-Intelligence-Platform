import os
import pandas as pd
import psycopg2

from dotenv import load_dotenv

load_dotenv()

employees = pd.read_excel("data/raw/employees.xlsx")




employees = employees.rename(columns={
    "Branch ID": "branch_id",
    "Branch Name": "branch_name",
    "Manager Email": "manager_email",
    "First Name": "first_name",
    "Last Name": "last_name",
    "Job Role": "job_role",
    "Phone Number": "phone_number",
    "Email": "email",
    "Address": "address",
    "Date of Birth": "date_of_birth",
    "Hire Date": "hire_date",
    "Hourly Rate": "hourly_rate",
    "Employment Type": "employment_type",
    "Employment Status": "employment_status"
})


# print(employees)
# # print(employees[employees["hourly_rate"] <= 0])

# # print(employees["branch_id"].unique())

# invalid_managers = employees[
#     employees["manager_email"].notna()
#     & ~employees["manager_email"].isin(employees["email"])
# ]

# print(invalid_managers)



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
INSERT INTO employees (
    branch_id,
    first_name,
    last_name,
    job_role,
    phone_number,
    email,
    address,
    date_of_birth,
    hire_date,
    hourly_rate,
    employment_type,
    employment_status
)
VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
ON CONFLICT (email) DO NOTHING
"""


for _, row in employees.iterrows():
    cursor.execute(
        insert_query,
        (
            row["branch_id"],
            row["first_name"],
            row["last_name"],
            row["job_role"],
            row["phone_number"],
            row["email"],
            row["address"],
            row["date_of_birth"],
            row["hire_date"],
            row["hourly_rate"],
            row["employment_type"],
            row["employment_status"]
        )
    )
    
connection.commit()

print(f"{len(employees)} employee rows processed.")



cursor.execute("""
    SELECT employee_id, email
    FROM employees
""")

employee_records = cursor.fetchall()


email_to_id = {
    email: employee_id
    for employee_id, email in employee_records
}

# # print(email_to_id)


update_manager_query = """
UPDATE employees
SET manager_id = %s
WHERE email = %s
"""

#Then loop through your DataFrame:

for _, row in employees.iterrows():

    if pd.notna(row["manager_email"]):

        manager_id = email_to_id[row["manager_email"]]

        cursor.execute(
            update_manager_query,
            (
                manager_id,
                row["email"]
            )
        )
connection.commit()

print("Manager IDs updated successfully!")


cursor.close()
connection.close()