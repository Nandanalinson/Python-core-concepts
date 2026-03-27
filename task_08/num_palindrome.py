number = int(input("Enter a number : "))

print("palindrome" if str(number) == str(number)[::-1] else "not palindrome")