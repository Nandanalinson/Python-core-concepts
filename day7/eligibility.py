# Eligibility rules:
# Age between 21 and 35
# Degree is "BTech" or "MCA"
# Experience ≥ 2 years
# BUT
# If the candidate has experience ≥ 5 years, age limit does not matter

Age = int(input("Enter the age :"))

Degree = input("Enter the degree : ")

Exp = int(input("Enter the no. of years of experience : "))

if (Exp >= 5) and (Degree == "MCA" or Degree == "BTech"):

    print("eligible")
 
elif (Age > 21 and Age < 35) and (Exp >= 2) and (Degree == "MCA" or Degree == "BTech"):

    print("eligible")

else:

    print("not eligible")