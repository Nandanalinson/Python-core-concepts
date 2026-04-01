a = 10

def display():

    global a

    a = 5

    print(f"Value of a inside the function {a}")

print(f"Value of a before the function {a}")

display()

print(f"Value of a after the function call {a}")