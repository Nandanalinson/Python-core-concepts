weight = int(input("Enter the weight in kg : "))

height = int(input("Enter the height in cm : "))

height_m = height / 100

bmi = weight / (height_m) ** 2

print(f"Your bmi is {bmi}")

