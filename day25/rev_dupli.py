text = "python is a programming language"

word = ""

for i in text.split():

    unique = ""

    for j in i:

        if j not in unique:

            unique += j

    word = word + unique[::-1] + " "
    
print(word)