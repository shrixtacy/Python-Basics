#Logical operators = evaluate multiple condition ( or , and , not)
# or = at least one of the conditions must be true
# and = both the conditions must be true
# not = inverts the condition ( not false , not true )

#OR EXAMPLE

temp = 20
is_raining = True

if temp > 35 or temp < 0 or is_raining:
    print("The outdoor event is cancelled")
else:
    print("The outdoor event is scheduled")


#AND Example

temp2 = -2
is_sunny = False

if temp2 >= 28 and is_sunny:
    print("you'll be cooked bro 😭🙏")

elif temp2 <= 0 and is_sunny:
    print("Its so cold...Santa might need hot")

else:
    print("Get out now")
    

#Not operator

temp3 = 30
is_cloudy = True

if temp3 >= 25 and not is_cloudy:
    print("You can go to play buddy")

else:
    print("Sit and study")


#A joint example for better clarity


