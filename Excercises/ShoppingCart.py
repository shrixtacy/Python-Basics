#Shopping cart program using collections ( list , set , tuple )

items = []
prices = []
total = 0

while True:
    item = input("Enter your items ( q to Quit ): ")
    if item.lower() == "q":
        break
    else:
        price = float(input(f"Enter the price of {item}:$ "))
        items.append(item)
        prices.append(price)

print("----- YOUR CART -----")

for item in items:
    print(item, end=",")

for price in prices:
    total += price



print()
print(f"Your total is ${total}")