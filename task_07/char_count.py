str_1 = input("Enter a string : ")

count = 0

for i in str_1 :
    
    count += 1

    if i == " ":

        count -= 1

print(f"The number of characters in the string is {count}")