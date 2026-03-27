# word = input("Enter a word : ")

# unique = set(word)

# for i in unique:

#     count = 0

#     for j in word:

#         if i == j :

#             count += 1

#     print(f"The frequency of {i} is {count}")



word = input("Enter a word : ")

unique = ""

for i in word :

    if i not in unique :

        print(f"The frequency of {i} is {word.count(i)}")

        unique += i