# find the largest word from the string having no duplicate characters

text = "python is a programming language"

unique = []

for i in text.split():

    for j in i:

        if i.count(j) > 1:

            break

    else:

        unique.append(i)

print(max(unique))









# new = []

# for i in text.split():

#     unique = ""

#     for j in i:

#         if j not in unique:

#             unique += j

#     if len(i) == len(unique):

#         new.append(unique)

# print(max(new))