#2d Lists = a 2d list is just a list made up of lists mainly used for grid or matrix of data


fruits = ["strawberry", "banana", "cherry", "grapes", "mango"]
vegetables = ["tomato", "potato", "cabbage", "eggplant", "letuce"]
meats = ["chicken", "pig", "fish"]

groceries = [fruits, vegetables, meats]
print(groceries)

print(groceries[0][0])   #two indices represents row & column respectively
print(groceries[1][2])

groceries2 = [ ["strawberry", "banana", "cherry", "grapes", "mango"], 
              ["tomato", "potato", "cabbage", "eggplant", "letuce"],
                ["chicken", "pig", "fish"]  ]

for collection in groceries2:
    for food in collection:
        print(food, end=" ")
    print()