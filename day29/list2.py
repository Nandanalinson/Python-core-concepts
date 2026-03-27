
#  data [15, "hello", 22, "world", 9, "python", 4]

#  Create a new list:

# Only include:

# Numbers greater than 10 square them

# Strings containing letter 'o' convert to uppercase

data = [15, "hello",22, "world", 9, "python", 4 , "nandana"]

new_data = []

for i in data:

    if type(i) == int and i > 10:

        new_data.append(i**2)

    elif type(i) == str and [j for j in i if j == 'o']:

        new_data.append(i.upper())

    else:

        new_data.append(i)

print(new_data)