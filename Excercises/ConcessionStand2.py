Store =  {"shoes": 23.00,
          "sandles": 24.00,
          "tops": 45.50,
          "cargos": 32.75,
          "undies": 15.73}

Cart = []

total = 0

print("------------STORE ITEMS-----------")
for keys, values in Store.items():
    print(f"{keys:15}: ${values:.2f}")
print("----------------------------------")

while True:
    items = input("Enter the items (q to quit ): ").lower()
    if items == "q":
        break
    elif Store.get(items) is not None:
        Cart.append(items)

print("--------YOUR CART---------")
for items in Cart:
    total += Store.get(items)
    print(items,end = ",")

print()
print(f"Your total is ${total:.2f}")

