items = {"A":50,"B":60,"C":40,"D":65,"E":54}

largest = 0

second_largest = 0

element = ""

for i in items:

    if items[i] > largest:

        second_largest = largest

        largest = items[i]

        element = i

    elif largest < items[i]:

        second_largest = items[i]

        element = i

print(f"The key containing second maximum value is {element} having {second_largest}")