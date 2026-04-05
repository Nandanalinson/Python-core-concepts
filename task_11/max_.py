result = lambda num1 , num2 : f"{num1} is largest" if num1 > num2 else f"{num2} is largest"

print(result(int(input("Enter the first number : ")) , int(input("Enter the second number : "))))