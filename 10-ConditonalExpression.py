# Condtional expression = A one-line shortcut for the if-else statement ( ternary operator)
#                         print or assign one of two values based on a condition
#                         X if conditoon else Y

num = 5

print("Positve" if num > 0 else "Nageative")
result = "EVEN" if num % 2 == 0 else "ODD"

print(result)

# Another example

a = 6
b = 7
age = 14
temp = 24

max_num = a if a > b else b     #uses a & b input
min_num = a if a < b else b
print(max_num)
print(min_num)

status = "Adult" if age>= 18 else "child"  # uses the age input
print(status)


weather = "Hot" if temp > 20 else "Cold"  # uses the temp input 
print(weather)

#User role example - how user roles are decided / divided 

user_role = "Admin"

access_level = "Full Access" if user_role == "Admin" else "Limited Access"

print(access_level)