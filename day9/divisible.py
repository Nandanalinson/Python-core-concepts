number = int(input("Enter a number :"))

result = "divisible by 3 and 5" if number % 5 == 0 and number % 3 == 0 else "not divisible"

print(result)
