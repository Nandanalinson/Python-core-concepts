def simple_interest(principal_amt : int , rate : int , tenure : int):

    return principal_amt * rate * tenure / 100

print(f"The simple interest is {simple_interest(int(input("Enter the primcipal amount : ")),int(input("Enter the rate : ")),int(input("Enter the tenure : ")))}")