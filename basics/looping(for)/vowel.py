str1 = input("Enter a string : ")

count = 0

for i in str1:

    if i in "aeiouAEIOU":

        count += 1

print(f"The number of vowels is {count}")