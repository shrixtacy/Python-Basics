#input() = A function that prompts the user to enter data 
#          returns the entered data as a string

name = input("What is Your name?: ")
age = int(input("What is your age>:")) #Typecasting / converting input to different datatype while taking input

age += 1 #Increment 

print(f"Hello {name}")
print("Happy Birthday")
print(f"Lmao you are {age} years old. So old !!")