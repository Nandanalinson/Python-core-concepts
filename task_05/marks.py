marks = int(input("Enter the total mark :"))

if marks >= 90:

    print(f"Your grade is A")

elif (marks >= 75) and (marks < 90):

    print(f"Your grade is B")

elif (marks >= 50) and (marks < 75):

    print(f"Your grade is C")

else:

    print(f"Failed")