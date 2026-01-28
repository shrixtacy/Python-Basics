#Concession Stand Program

menu = {"pizza": 100.50,
        "burger":80.00,
        "lasagna": 75.50,
        "lemonade": 15.50,
        "chicken popcorn": 50.00,
        "butter popcorn": 30.50,
        "normal popcorn":20.00,
        "cheese meat balls":70.00}

cart =[]

total = 0

print("----------Menu----------")
for key, value in menu.items():
    print(f"{key:18}: ${value:.2f}")      #Here "key:18" means after keys 18 spaces are left empty
print("------------------------")

while True:
    food = input("Select an item (q to quit): ").lower()
    if food == "q":
        break
    elif menu.get(food) is not None:
        cart.append(food)

print("----------YOUR ORDER---------")
for food in cart:
    total += menu.get(food)
    print(food,end =" ")      


print()
print(f"Total is : ${total:.2f}")
