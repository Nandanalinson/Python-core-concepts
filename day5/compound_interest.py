p = int(input("Enter the principal amount : "))

r = float(input("Enter the rate : "))

n = int(input("Enter the no. of times interest compounded : "))

t = int(input("Enter the tenure : "))

a = p * (1 + r / n) ** (n*t)

compound_interest = a - p

print(f"Compound interest is {compound_interest}")