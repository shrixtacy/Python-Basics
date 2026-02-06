# *args = Allow you to pass multiple non-key arguments
# **kwargs = allow you to pass multiple keywords-arguments
# * = Unpacking Operator
#     1. positional , 2. default, 3.keywords, 4. ARBITRARY


# *args

def add(*nums):       
    total = 0
    for num in nums:
        total += num
    return total

print(add(1,2,3,4,5))


#another example

def display_name(*names):
    for name in names:
        print(name, end=" ")

display_name("Spongebob", "Marrrie Currie", "Van Gough")
print()
print()


def display(*name):
    for name in name:
        print(name,end=" ")

display("Bihari", "Chor")
print()
print()

# **kwargs

def print_address(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_address(street="Pandav Nagar", city="Bhubaneswar", state="Odisha", zip="251002")
print()
print()


#Shipping label

def shipping_label(*args, **kwargs):
    for arg in args:
        print(arg, end=" ")
    print()
    for value in kwargs.values():
        print(value, end=" ")
        print()
#or
    if "city" in kwargs:
        print(f"{kwargs.get('hospital')} {kwargs.get("city")}")
    else:
        print(f"{kwargs.get("hospital")}")


shipping_label("Dr. ", "Mulchand" , "Bhosdiwala", hospital="KIIMS", city="Bhubaneswar")