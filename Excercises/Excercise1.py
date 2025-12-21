# Excercise 1 Rectangle area Calculatior
# We all know the area of recangle is l*w ( lenght x Width ) as simple as that

len = input("What is the len of rect: ")  #keepinh the value
wid = input("What is the width of rect: ")

print(f"The length of rect is {len}") 
print(f"The width of the rect is {wid}")

len = int(len)  #typecasting / converting datatype for arithmetic expression
wid = int(wid)

area = len * wid  #multiplication 
 
print(f"The area of the rectangle is {area}")


# what we can also do is

len1 = float(input("Lentgh of Rectangle: ")) #typecasting to float
wid1 = float(input("Width of Rectangle: "))

area1 = len1 * wid1

print(f"The new area is {area1}")
