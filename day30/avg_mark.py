# list of dictionaries
#Find the avg mark of students in full stack

student_details = [{"name":"sneha","course":"Full stack","marks":80},
                   {"name":"rahul","course":"Full stack","marks":90},
                   {"name":"ram","course":"Datascience","marks":83},
                   {"name":"sarath","course":"Full stack","marks":70}]

# sum = 0

# count = 0

# for item in student_details:

#     if item["course"] == "Full stack":

#         sum += item["marks"]

#         count += 1

# print(f"The avg mark of student in Full stack is {sum/count}")

marks_new = [item["marks"] for item in student_details if item["course"] == "Full stack"]

print(f"The Average mark of student in Full stack is {sum(marks_new)/len(marks_new)}")