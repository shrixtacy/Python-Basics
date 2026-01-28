import random

#random integer between given 2 interger limits
low = 1
high = 100
num = random.randint(low,high)
print(num)

#Random integer number between given parameters
dice = random.randint(1,20)
print(dice)

#Random Floating Number
float_num = random.random()
print(float_num)

#random options between any items in tuple
Option = ("Scisor","Paper","Rock")

option = random.choice(Option)
print(option)

#shuffeling the given ordered list

cards = ["A", "2","3","4","5","6","7","8","9","10","J","K","Q"]

random.shuffle(cards)
print(cards)