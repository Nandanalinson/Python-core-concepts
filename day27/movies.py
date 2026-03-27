# Each user has watched movies (nested list)
# Find the users who watched the same movie more than once

users = [
    ["inception","avatar","inception","hero","hero"],
    ["titanic","avatar"],
    ["joker","joker","joker"]
]

print(users[0][1::]) # to get last two elements of the first elemet 

for i in users:

    for movies in i:

        if i.count(movies) > 1 :

            print(i)                    # To print the users history not a single movie

            break