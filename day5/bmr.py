#pgrm to find bmr 

weight = int(input("enter the weight in kg : "))

height = int(input("Enter the height in cm : "))

age = int(input("Enter the age : "))

bmr = (10 * weight) + (6.25 * height) - (5 * age) - 161

print(f"BMR = {bmr}")