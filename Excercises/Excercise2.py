# Make a shopping cart program

item = input("What item would you like to buy ?: ")
price = float(input("What is the Price?: "))         #Prices shall be in float as they might have decimals ( 9.99 )
quantity = int(input("How many would you like: "))   #quantity is always in the whole

total = price * quantity

print(f"You have bought {quantity} x {item}/s")
print(f"You total is ${total}")