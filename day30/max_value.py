items = {"A":50,"B":60,"C":40,"D":65,"E":54}

max_value = 0

element = ""

for i in items:

    if items[i] > max_value:

        max_value = items[i]

        element = i

print(f"The key containing maximum value is {element} having {max_value}")