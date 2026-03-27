user_input = input("Enter the string : ")

# if user_input == user_input[::-1]:

#     print(f"{user_input} is a palindrome ")

# else :

#     print(f"{user_input} is not a palindrome ")


result = "Palindrome" if user_input == user_input[::-1] else "not palindrome"
print(result)
