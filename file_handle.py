file = open("file_1.txt","r")

total_list = []

for i in file:

    total = 0

    values = i.strip().split(",")

    marks = list(map(lambda i:int(i),values[1:]))

    total = sum(marks)

    total_list.append(values[0])

    total_list.append(total)

    average = total / len(marks)

    print(values[0],total,average)

print(max(total_list[1:]))