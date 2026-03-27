# data [12, "hello123", 5, "WORLD", B, "pyTh0n9", 3]

# For Numbers:

#If number is greater than 10 convert it to string and append "High"

#Else square the number

#For Strings:

#If string contains digits remove digits

#If string is uppercase convert to lowercase

#Else capitalize the string

# ==================================




data = [12, "hello123", 5, "WORLD", 8 , "pyThOn9", 3]

for i in data:

    if type(i) == int and i > 10:

        data.insert(data.index(i),"High")
        data.remove(i)

    elif type(i) == int and i <= 10:

        data.insert(data.index(i),i ** 2)
        data.remove(i)

    elif type(i) == str and i.isalnum():

        new_str = ""

        for j in i:

            if j.isalpha() :

                new_str += j

            if new_str.isupper():

                new_str = new_str.lower()

            else:

                new_str = new_str.capitalize()

        data.insert(data.index(i),new_str)

        data.remove(i)


print(data)