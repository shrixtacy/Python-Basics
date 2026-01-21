# If = Execute some code only IF some condition is true 
# Else do something else.
# elif = else if - it is basically the middle statement between if & else 
# We can add as many as elif statement as we waant between if & else. 

Age = int(input("Enter your age: "))

if Age >= 18:
    print(f"Your age is {Age},  so you are eligible for Credit card")
elif Age <= 12:
    print("Get the fuck out of here. ")
else:
    print("You are not eligible, Looser.")


#Another example

Response = input("Would you like food ? ( Y/N ): ")

if Response == "Y":
    print("Have some Food")
else:
    print("No food for you...Boooo")


#Another example

name = input("Enter your name: ")

if name=="":
    print("Did yiu just leave it blank ?...You stupid lmao")
else:
    print(f"Welcome {name}")
