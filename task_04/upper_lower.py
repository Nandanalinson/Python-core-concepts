ch = input("Enter a character : ")

if ch.isupper():

    print(f"{ch} is an uppercase letter")

elif ch.islower():

    print(f"{ch} is a lowercase letter")

elif ch.isdigit():

    print(f"{ch} is a digit")

else :

    print(f"{ch} is neither a letter nor digit")
