items = {"A":50,"B":60,"C":40,"D":65,"E":54}

min_value = items["A"]

element = ""

for i in items:

    if items[i] < min_value:

        min_value = items[i]

        element = i

print(f"The key containing maximum value is {element} having {min_value}")