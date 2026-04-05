marks = [97,65,78,94,99,34,56]

passed = []

failed = []

for i in marks:

    if i > 75:

        passed.append(i)

        print(f"Student {marks.index(i) + 1} has passed")
    
    else:

        failed.append(i)

        print(f"Student {marks.index(i)+1} has failed")

print(f"Passed marks are {passed} \nFailed marks are {failed}")