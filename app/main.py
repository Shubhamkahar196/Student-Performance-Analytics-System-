import pandas as pd
import numpy as np
from function import calculate_grade,check_result

# load student dataset

df = pd.read_csv("students.csv")

# display first 5 student records
print("Student Performance Analytics System")
print("-" * 40)
print("\nFirst 5 Student Records:")
print(df.head())

# Display dataset information

print("\nDataset Information: ")
print("Total Students: ", len(df))
print("Columns: ",df.columns.tolist())

# define subject columns

subjects = ["Python","Mathematics","Data_Science","English"]

# Calculate Total Marks
df["Total_Marks"] = df[subjects].sum(axis=1)

# calculate average Marks

df ["Average_Marks"]=df[subjects].mean(axis=1).round(2)

# calculate grades

df["Grade"] = df["Average_Marks"].apply(calculate_grade)

# calculate pass or fail
df["Result"] = df[subjects].apply(
    lambda row: check_result(row.tolist()), axis=1
)

# Display student performance
print("\n Student Performance Report: ")
print(
    df [["Student_ID", "Name","Total_Marks","Average_Marks","Grade","Result"]].head(10)
)


# Class Performance Summary

print("\n" + "=" * 40)
print("CLASS PERFORMANCE SUMMARY")
print("=" * 40)

# total number of students

total_students = len(df)

# overall class average

class_avg = np.mean(df["Average_Marks"])

# Highest performing student
top_student = df.loc[df["Average_Marks"].idxmax()]

# Lowest performing student
low_student =df.loc[df["Average_Marks"].idxmin()]

# Count pass and fail students

passed_students = (df["Result"]=="Pass").sum()
failed_students = (df["Result"]=="Fail").sum()

# Calculate pass percentage

pass_percentage=(passed_students/total_students) * 100

# Display summary
print("Total Students:", total_students)
print("Class Average:", round(class_avg, 2))
print(
    "Top Student:",
    top_student["Name"],
    "-",
    top_student["Average_Marks"]
)
print(
    "Lowest Student:",
    low_student["Name"],
    "-",
    low_student["Average_Marks"]
)
print("Passed Students:", passed_students)
print("Failed Students:", failed_students)
print("Pass Percentage:", round(pass_percentage, 2), "%")

# subject-wise Performance Analysis

print("\n SUBJECT-WISE PERFORMANCE")

subject_averages = df[subjects].mean().round(2)

for subject,average in subject_averages.items():
    print(f"{subject}: {average}")


# Top 5 performing students

print("\n" + "=" * 40)
print("TOP 5 PERFORMANCE STUDENTS")
print("=" * 40)

top_5_students = df.sort_values(
    by="Average_Marks",
    ascending=False
).head(5)

print(
    top_5_students[
        ["Student_ID","Name","Average_Marks","Grade"]
    ].to_string(index=False)
)

# Attendance Analysis

# Attendance Analysis

print("\n" + "=" * 40)
print("ATTENDANCE ANALYSIS")
print("=" * 40)

average_attendance = df["Attendance"].mean().round(2)

low_attendance = df[df["Attendance"] < 75]

print("Average Attendance:", average_attendance, "%")

print(
    "Students with Attendance Below 75%:",
    len(low_attendance)
)

print("\nStudents with Low Attendance:")

print(
    low_attendance[
        ["Student_ID", "Name", "Attendance"]
    ].to_string(index=False)
)




# Department-wise Performance Analysis

print("\n" + "=" * 40)
print("DEPARTMENT-WISE PERFORMANCE")
print("=" * 40)

department_averages = (
    df.groupby("Department")["Average_Marks"]
    .mean()
    .round(2)
    .sort_values(ascending=False)
)

for department, average in department_averages.items():
    print(f"{department}: {average}")



output_file = "student_results.csv"

df.to_csv(output_file, index=False)

print("\n" + "=" * 40)
print("RESULTS SAVED SUCCESSFULLY")
print("=" * 40)

print("Output file:", output_file)
print("Total records saved:", len(df))

