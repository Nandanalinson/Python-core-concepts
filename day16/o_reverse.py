name = input("Enter a word : ")

# i = name.index("o")

# print(name[0:i +1][::-1]+name[i+1:])

for i in name :

    if i == "o" :

        ind = name.index(i)

        break

print(name[0 : ind + 1][::-1] + name[ind + 1:])
 