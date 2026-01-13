#while loop = execute some code WHILE some condition remains true

name = input("Enter your name: ")          #first python will run this 

while name == "":                          #if the string is empty
    print("You did not enter your name")   #While loop will continue to execute this till the string is filled
    name = input("Enter your name: ")      # this will pop up till the string is empty / till condition is not fullfilled

print(f"Hello {name}")  

#Example 2

age = int(input("Enter your age: "))

while age < 18:
    print("Age can't be less than 18")
    age = int(input("Enter your age: "))

print(f"You are {age} year old")


#example 3

food = input("Enter a food you like (q to quit ): ")

while not food == "q":
    print(f"You like {food}")
    food = input("Enter another food item you like (q to quit ): ")

print("Byeeee")

#Example 4

num = int(input("Enter a number between 1-10: "))

while num < 1 or num > 10:
    print(f"{num} is not valid")
    num = int(input("Enter a number between 1-10: "))

print(f"Your number is {num}")