b = 15      # global variable

def display(* args):

    a = 10          # local variable (can only br accessed inside the function)

    print(a)

    print(b)

display()

print(b)

# print(a)            # can't be accessed