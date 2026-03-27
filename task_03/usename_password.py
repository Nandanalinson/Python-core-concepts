Username = input("Enter your username : ")

Password = input("Enter your password : ")

if ((len(Username) > 5) and (len(Password) > 8)):

    print(f"Entered username and password is valid")

else:

    print(f"Entered username and password is not valid")