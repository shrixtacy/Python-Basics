#Function = A block of re-usable code
#           Place () after the function name to invoke it


def happy_birthday():              #def is used for defining a function with a function name happy_birthday
 print("Happy Birthday to you !")
 print("May God Bless you")

happy_birthday()             #calling the function 




def happy_birthday(name, age):                                  #here we are basically adding parameter
 print(f"Happy Birthday to {name}. You are {age} years old !")  #using the parameter
 print("May God Bless you")

happy_birthday("Nigga", 30)                                     #calling the function with the parameter
happy_birthday(30, "Nigga")


#function to display a invoice

def invoice(username, amount, due_date):
 print(f"Hello {username}")
 print(f"Your Bill of ${amount:.2f} is due: {due_date}")

invoice("Shri", 100.3234, "1st Feb")


#return = statement used to end a function
#         and send a result back to the caller


def add_num(x,y):
 z = x + y
 return z

def sub_num(x,y):
 z = x - y
 return z

def multi_num(x,y):
 z = x * y
 return z

def div_num(x,y):
 z = x / y
 return z

print(add_num(1,2))
print(sub_num(9,6))
print(multi_num(293,344))
print(div_num(9,3))


## Another example

def Create_name(first, last):
 first = first.capitalize()
 last = last.capitalize()
 return first + " " + last

full_name = Create_name("Shriyansh", "Dash")

print(full_name)


#More examples

def whatsyour_age():
 age = input("Enter your age nigga: ")
 print(f"your age is {age}")

whatsyour_age()


