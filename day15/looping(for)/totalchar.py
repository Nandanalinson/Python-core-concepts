# wap to get the total number of characters in the string entered by user without using builtin function 

word = input("Enter the word : ")

count = 0

for i in word :

    count += 1

print(f"The number of characters is {count}")