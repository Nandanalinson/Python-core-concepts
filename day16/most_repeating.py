word = input("Enter a word : ")

largest = 0

temp = ""

for i in word :

    if word.count(i) > largest :

        largest = word.count(i)

        temp = i

print(f"The most repeating character is {temp} and the count is {largest}")