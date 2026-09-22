import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
# Load the employee dataset
data = pd.read_csv("employee_data.csv")

# Display the first 5 rows
print(data.head())

# Display the number of rows and columns
print(data.shape)

# Display basic information about the dataset
print(data.info())

# Display basic statistical information
print(data.describe())

# Count the total number of employees
total_employees = data["Employee_ID"].count()

# Calculate the average salary
average_salary = data["Salary"].mean()

# Find the highest salary
highest_salary = data["Salary"].max()

# Find the lowest salary
lowest_salary = data["Salary"].min()

# Display the salary analysis
print("Total Employees:", total_employees)
print("Average Salary:", average_salary)
print("Highest Salary:", highest_salary)
print("Lowest Salary:", lowest_salary)

# Count the number of employees in each department
department_count = data["Department"].value_counts()

# Display department-wise employee count
print("Employees by Department:")
print(department_count)

# Create a bar chart for employees by department
plt.figure(figsize=(8, 5))

department_count.plot(kind="bar")

# Add chart title and axis labels
plt.title("Employees by Department")
plt.xlabel("Department")
plt.ylabel("Number of Employees")

# Save the chart as an image
plt.savefig("employees_by_department.png")

# Display the chart
plt.show()

# Calculate the average salary for each department
department_salary = data.groupby("Department")["Salary"].mean()

# Display department-wise average salary
print("Average Salary by Department:")
print(department_salary)


# Create a bar chart for average salary by department
plt.figure(figsize=(8, 5))

department_salary.plot(kind="bar")

# Add chart title and axis labels
plt.title("Average Salary by Department")
plt.xlabel("Department")
plt.ylabel("Average Salary")

# Save the chart as an image
plt.savefig("salary_by_department.png")

# Display the chart
plt.show()