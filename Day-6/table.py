import csv

# with open("customers-100.csv", 'r', newline = '') as file:
#     csv_reader = csv.reader(file)

#     print(csv_reader, type(csv_reader))

#     for raw in csv_reader:
#         print(raw, type(raw))

# with open("customers-100.csv", 'r', newline = '') as file:
#     csv_reader = csv.DictReader(file)

#     print(csv_reader, type(csv_reader))

#     for raw in csv_reader:
#         print(raw, type(raw))


# import csv

# csv_file_path = "new_table.csv"

# data = [
#     {
#         "name": "John Doe",
#         "age": 30,
#         "city": "New York"
#     },
#     {
#         "name": "Jane Smith",
#         "age": 28,
#         "city": "Los Angeles"
#     },
#     {
#         "name": "Bob Johnson",
#         "age": 35,
#         "city": "Chicago"
#     }
# ]

# fieldnames = ["name", "age", "city"]

# #open the csv file for writing
# with open(csv_file_path, 'w', newline='') as csv_file:
#     #create a csv dict writer object
#     csv_writer = csv.DictWriter(csv_file, fieldnames = fieldnames)

#     #write the header (column names) to the csv file
#     csv_writer.writeheader()

#     #write the data rows to the csv file
#     for row in data:
#         csv_writer.writerow(row)

# print(f"CSV file has been created successfully at {csv_file_path}")




#You are tasked with creating a python programme to manage a companies employee records stored in csv file. The programme should read the 
#employee details from a csv file.fileter the records based on a condition and write the filtered record to a new csv file.

#files provided -
#                input file: employees.csv contains the following fields: EmployeeId, Name, Department, Salaray
#                                                                                   1, John, IT, 60000 
#                                                                                   2, Jane, HR, 55000
#                                                                                   3, Mike, Finance, 70000
#                                                                                   4, Linda, IT, 65000

#                output file: high_salary_employee.csv  you will create this file,
#                it should contain records of employees with salary greater than 60000.the field should remain the same

#Task 1: Read the employee details from the input file -> use scv.reader to read employees.csv and display all the records 
#Task 2: Filter the records based on the condition -> filter the records of employees with salary greater than 60000
#Task 3: Write the filtered records to a new csv file -> use csv.DictWriter to write the filtered records to high_salary_employee.csv

import csv

csv_file_path_1 = "employee.csv"

data = [
    {
        "EmployeeId": 1,
        "Name": "John",
        "Department": "IT",
        "Salary": 60000
    },
    {
        "EmployeeId": 2,
        "Name": "Jane",
        "Department": "HR",
        "Salary": 55000
    },
    {
        "EmployeeId": 3,
        "Name": "Mike",
        "Department": "Finance",
        "Salary": 70000
    },
    {
        "EmployeeId": 4,
        "Name": "Linda",
        "Department": "IT",
        "Salary": 65000
    }
]

fieldnames = ["EmployeeId", "Name", "Department", "Salary"]

with open(csv_file_path_1, 'w', newline='') as csv_file:
    csv_writer = csv.DictWriter(csv_file, fieldnames = fieldnames)

    csv_writer.writeheader()

    for row in data:
        csv_writer.writerow(row)

print(f"CSV file has been created successfully at {csv_file_path_1}")


with open(csv_file_path_1, 'r', newline='') as csv_file:
    csv_reader = csv.reader(csv_file)

    for row in csv_reader:
        print(row)

csv_file_path_2 = "high_salary_employee.csv"

with open(csv_file_path_1, 'r', newline='') as csv_file:
    csv_reader = csv.DictReader(csv_file)

    high_salary_employee = []
 
    for row in csv_reader:
        if int(row["Salary"]) > 60000:
            high_salary_employee.append(row)

with open(csv_file_path_2, 'w', newline='') as csv_file:
    csv_writer = csv.DictWriter(csv_file, fieldnames = fieldnames)

    csv_writer.writeheader()

    for row in high_salary_employee:
        csv_writer.writerow(row)

print(f"CSV file has been created successfully at {csv_file_path_2}")




