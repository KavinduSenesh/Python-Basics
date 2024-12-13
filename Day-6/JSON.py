# import json

# #specify the path of the json file
# json_file_path = 'D:\GDSE 68\Python\example_1.json'

# with open(json_file_path, 'r') as file:
#     data = json.load(file)
#     # print(data, type(data))

# for key, value in data.items():
#     #here f is used for string formatting
#     print(f'{key} : {value}')

# import json

# data = {
#     "name": "senesh",
#     "age": 24,
#     "city": "colombo"
# }

# with open('D:\GDSE 68\Python\my_json.json', 'w') as file:
#     jason_data = json.dumps(data, indent=4) #indent is used to format the json file
#     file.write(jason_data)



#you are given a jason file names 'student.json' which contains information about students and their grades. your task is to,

# 1. read the json file
# 2. display the names of all student who scored above 75
# 3. add a new student record to the file
# 4. save the updated data back to the json file

# data = [
#     {"name": "Alice", "grade": 85},
#     {"name": "Bob", "grade": 72},
#     {"name": "Charlie", "grade": 90},
#     {"name": "David", "grade": 65}
# ]


import json

json_file_path = 'D:\GDSE 68\Python\student.json'

with open(json_file_path, 'r') as file:
    data = json.load(file)
    print(data, type(data))

    for student in data:
        if student['grade'] > 75:
            print(student['name'])

student_data = {
        "name": "Eve",
        "grade": 80
}

data.append(student_data)

with open(json_file_path, 'w') as file:
    jason_data = json.dumps(data, indent=4)
    file.write(jason_data)
    


