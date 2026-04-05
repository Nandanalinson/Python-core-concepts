credentials = {"Nandana" : "hjkdkld@345","Arya" : "jrguv#457","Fathima" : "gyrvdb&234","Afna" : "wyervbf*632"}

username = input("Enter username : ")

password = input("Enter your password : ")

for i, j in credentials.items():

    if i == username:

        if j == password:

            print("Login Successfull")

        else:

            print("Password incorrect")

        break

else:

    print("invalid username")