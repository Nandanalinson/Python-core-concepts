name = input("Enter name of person you want to invite : ")

print(f"{name} has been invited ")

count = 1

ch = input("Do you want to invite anybody else : ")

while(ch == 'y'):

    name = input("Enter the name : ")

    print(f"{name} has been invited ")

    count += 1

    ch = input("Do you want to invite anybody else : ")

print(f"{count} people has been invited")

