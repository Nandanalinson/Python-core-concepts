Age = int(input("Enter the age : "))

Test_passed = input("Did you pass the driving test ? (y/n) ")

if Age >= 18 and Test_passed == "y":

    print(f"The person is eligible for a driving license")

else:

    print(f"The person is not eligible for a driving license")