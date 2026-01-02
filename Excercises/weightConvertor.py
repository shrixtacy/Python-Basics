#Making a weight convertor for different weight value kg -> pounds 
# 1kg = 2.20 Pound

weight = float(input("Enter you weight: "))
unit = input("Choose a Unit ( Kg or lb ): ")

if unit == "kg":
    lbs = weight * 2.20
    print(f"You weight in pounds is {round(lbs,2)}lbs ")
elif unit == "lb":
    kg = weight / 2.20
    print(f"Your weight in kilogram is {round(kg,2)}kg ")
else:
    print(f"{unit}Please enter a valid unit")