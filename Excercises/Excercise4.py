#calculate the circumference of the circle ( Circumference = 2.pi.r )

import math

radius = float(input("Enter the Radius of Circle: "))

Circumference = 2 * math.pi * radius

print(f"The circumference of the circle is {round(Circumference, 2)}cm")


# Calculate the area of the circle ( Area = pi.r^2 )

radius2 = float(input("Enter the radius of Circle: "))

area = math.pi * pow(radius2, 2)

print(f"The area of the circle is {round(area, 2)}")

#Finding hypotenous of triangle C = root a^2 + b^2

a = float(input("Length of side a: "))
b = float(input("Length of side b: "))

c = math.sqrt( pow(a, 2) + pow(b, 2))

print(f"The hypotenous of the triangle is {c}")