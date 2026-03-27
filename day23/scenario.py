#Scenario:
#A teacher is checking student attendance. The attendance list for 10 days is stored as:
#attendance [1, 1, 0, 1, 0, 1, 1, 1, 0, 1)
# (1 Present, 0 = Absent)
 #Question: Write a Python program using a for loop to:
 #Count total number of days the student was present
 #Print "Eligible" if attendance is 75% or more, otherwise print "Not Eligible ...

#''Scenario:
#An eCommerce store stores product prices in a list:
 #prices [ 1200, 499, 2500, 799, 3000, 150]
 #Question: Write a Python program to:
#Create a new list of products costing more than 1000
 #Apply a 10% discount on all products and store the updated prices in another list
 #Find the highest priced product after discount/'..

# attendance = [1, 1, 0, 1, 0, 1, 1, 1, 0, 1]

# count = 0

# for  i in attendance:

#     if i == 1:

#         count += 1

# percentage = count * 10 

# print("Eligible" if percentage >= 75 else "Not Eligible")


prices =  [ 1200, 499, 2500, 799, 3000, 150 ]

new_list = []

updated_price = []

highest = 0

for i in prices:

    if i > 1000 :

        new_list.append(i)

    updated_price.append(i - (i * 10 /100))

for i in updated_price:

    if i > highest:

        highest = i

print(new_list)

print(updated_price)

print(highest)

