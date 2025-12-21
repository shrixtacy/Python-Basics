# Variables = A container which stores the value of ( string, interger, float, boolean)
#             A variable behaved as if it was the value it contains 

#Strings
first_name = "Shriyansh"
food ="Pizza"
email ="shriyanshdash12@gmail.com"

print(first_name) #variables are placed without quote in print statement
print(f"Hello {first_name}") #f string is easiest way to display a variable
print(f"I love {food}")
print(f"Hi {first_name}, Your email is {email} & you love eating {food}")


#integer
age = 25
weight = 64

print(f"Hey{first_name} your age is {age} and your weight is {weight}")


#float
price = 9.99
gpa = 8.9
print(f"Your amount is ${price}")


#boolean

ismale = True
print(f"Is he a male: {ismale}")

#if else statements

if ismale:
    print("You are a male")
else:
    print("You are not a male")