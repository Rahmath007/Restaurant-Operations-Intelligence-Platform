# import os
# import pandas as pd
# import psycopg2
# import random

# from dotenv import load_dotenv

# load_dotenv()


# connection = psycopg2.connect(
#     host=os.getenv("DB_HOST"),
#     port=os.getenv("DB_PORT"),
#     database=os.getenv("DB_NAME"),
#     user=os.getenv("DB_USER"),
#     password=os.getenv("DB_PASSWORD")
# )

# print("Connected successfully!")



# query = """
# SELECT
#     employee_id,
#     branch_id,
#     job_role,
#     employment_type,
#     employment_status
# FROM employees;
# """

# employees = pd.read_sql(query, connection)


# # print(employees.head())
# # print(employees.shape)
# # employees["job_role"]
# # employees["branch_id"].unique()
# # print(employees[employees["employment_status"] == "Active"])

# random.seed(42)

# active_employees = employees[
#     employees["employment_status"] == "Active"
# ].copy()


# # print(active_employees.shape)
# # print(active_employees["branch_id"].value_counts())


# start_date = "2026-02-01"
# end_date = "2026-07-31"

# dates = pd.date_range(
#     start=start_date,
#     end=end_date,
#     freq="D"
# )

# # print(len(dates))
# # print(dates[:5])


# shift_times = {
#     "Opening": ("09:00", "17:00"),
#     "Mid": ("12:00", "20:00"),
#     "Closing": ("14:00", "22:00")
# }



# foh_roles = [
#     'General Manager',
#     'Assistant Manager FOH',
#     'Team Leader FOH',
#     'Front of House Team Member'
# ]

# boh_roles = [
#     'Assistant Manager BOH',
#     'Head Chef',
#     'Team Leader BOH',
#     'Kitchen Team Member',
#     'Kitchen Porter'
# ]

# shifts = []
# branch_ids = [1,2,3,4]

# for date in dates:
#     for branch_id in branch_ids:
#         day_name = date.day_name()
#         branch_employees = active_employees[active_employees["branch_id"] == branch_id]
#         if day_name in ["Monday", "Tuesday", "Wednesday", "Thursday"]:
#             staffing_ratio = 0.45
#         elif day_name == "Friday":
#             staffing_ratio = 0.60
#         elif day_name == "Saturday":
#             staffing_ratio = 0.70
#         else:
#             staffing_ratio = 0.60

#         staff_needed = round(len(branch_employees) * staffing_ratio)
#         selected_staff = branch_employees.sample(
#             n=staff_needed
#         )
        
#         for _, employee in selected_staff.iterrows():
#             job_role = employee["job_role"]

#             # 1. Assign normal work area first
#             if job_role in foh_roles:
#                 work_area = "FOH"
#             elif job_role in boh_roles:
#                 work_area = "BOH"

#             # 2. Then occasionally swap eligible roles
#             if job_role in [
#                 "Assistant Manager FOH",
#                 "Assistant Manager BOH",
#                 "Team Leader FOH",
#                 "Team Leader BOH"
#             ]:
#                 if random.random() < 0.05:
#                     work_area = "BOH" if work_area == "FOH" else "FOH"


#             shift_type = random.choice(["Opening", "Mid", "Closing"])

#             shift_start, shift_end = shift_times[shift_type]


            
#             hours_worked = 8.0
            
#             if random.random() < 0.10:
#                 overtime_hours = random.choice([0.5, 1.0, 1.5, 2.0])
#             else:
#                 overtime_hours = 0.0
                
#             hours_worked = 8.0 + overtime_hours
            
#             status_roll = random.random()

#             if status_roll < 0.02:
#                 shift_status = "Sick"
#             elif status_roll < 0.03:
#                 shift_status = "Absent"
#             elif status_roll < 0.05:
#                 shift_status = "Holiday"
#             else:
#                 shift_status = "Completed"
                
                            
#             if shift_status != "Completed":
#                 hours_worked = 0.0
#                 overtime_hours = 0.0
                
            
#             shifts.append({
#                 "employee_id": employee["employee_id"],
#                 "branch_id": branch_id,
#                 "shift_date": date.date(),
#                 "shift_start": shift_start,
#                 "shift_end": shift_end,
#                 "hours_worked": hours_worked,
#                 "shift_type": shift_type,
#                 "work_area": work_area,
#                 "overtime_hours": overtime_hours,
#                 "shift_status": shift_status
#         })    
            
# shifts_df = pd.DataFrame(shifts)
            
# print(shifts_df.head())
# print(shifts_df.shape)    

# connection.close()        
            
            


# # Validation checks

# print("Validation checks:")

# print(shifts_df["shift_status"].value_counts())

# print(
#     shifts_df[
#         (shifts_df["shift_status"] != "Completed")
#         & (shifts_df["hours_worked"] != 0)
#     ]
# )

# print(
#     shifts_df[
#         (shifts_df["overtime_hours"] > 0)
#         & (shifts_df["shift_status"] != "Completed")
#     ]
# )


# print(shifts_df["work_area"].unique())
# print(shifts_df["shift_type"].unique())
# print(shifts_df["branch_id"].unique())


# print(shifts_df["shift_date"].min())
# print(shifts_df["shift_date"].max())


# print("Duplicate shifts check:")

# duplicate_shifts = shifts_df[
#     shifts_df.duplicated(
#         subset=["employee_id", "shift_date"],
#         keep=False
#     )
# ]

# print(duplicate_shifts)


# print(shifts_df["hours_worked"].value_counts().sort_index())

# print(shifts_df["overtime_hours"].value_counts().sort_index())

# print(
#     shifts_df[
#         (shifts_df["shift_status"] == "Completed")
#         & (shifts_df["hours_worked"] == 0)
#     ]
# )

# # Saving the generated shifts data to a CSV file

# shifts_df.to_csv("data/generated/shifts.csv", index=False)
# print("Shifts data saved to 'data/generated/shifts.csv'")


import pandas as pd

saved_shifts_df = pd.read_csv("data/generated/shifts.csv")

print("Loaded saved shifts data:")
print(saved_shifts_df.head())
print("Checking the shape and columns of the loaded DataFrame:")
print(saved_shifts_df.shape)
print("Columns in the loaded DataFrame:")
print(saved_shifts_df.columns)