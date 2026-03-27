items = ["django","java","python","curl"]

for i in range(len(items)):

    last_value = items.pop()

    items.insert(i,last_value)

print(items)                    # ['curl', 'python', 'java', 'django']