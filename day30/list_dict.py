# list of dictionaries
#Find the student name who has the maximum mark


student_details = [{"name":"sneha","course":"Full stack","marks":80},
                   {"name":"rahul","course":"Full stack","marks":90},
                   {"name":"ram","course":"Datascience","marks":83},
                   {"name":"sarath","course":"Full stack","marks":70}]


max_marks = 0

name = ""

for item in student_details:

    if item["marks"] > max_marks:

        max_marks = item["marks"]

        name = item["name"]

print(f"The student having maximum mark is {name} and has {max_marks} marks")