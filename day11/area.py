print("1.Square \n2.Triangle ")

num = int(input("Enter a input either 1 or 2 : "))

if num == 1 :

    side = int(input("Enter the side of the square : "))
    area = side * side
    print(f"The area of a square is {area}")

elif num == 2 :

    base = int(input("Enter the base of the triangle : "))
    height = int(input("Enter the height of the triangle : "))
    area = 1/2 * (base * height)
    print(f"The area of the triangle is {area}")

else :

    print("Invalid input")