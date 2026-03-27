word = input("Enter a word : ")

unique = ""

for i in word :

    if i not in unique :

        print(f"The frequency of {i} is {word.count(i)}")

        unique += i