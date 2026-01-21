#Dictionary = a collectoon of {key:value} pairs
#             ordered & changeable. No duplicates

capitals = {"USA":"Washington D.C.",
            "INDIA": "New Delhi",
            "China": "Beijing",
            "Russia":"Moscow"}

#print(dir(capitals))
#print(help(capitals))

print(capitals.get("USA"))
print(capitals.get("Japan"))

any_capital = input("Enter any country name: ")
if capitals.get(any_capital):
    print("That Capital Exists !")
else:
    print("It does not exists buddy !")  