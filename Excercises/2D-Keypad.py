# Creating a 2d keypad that exists on the phone call dialer ( num pad )

numpad = ((1,2,3),(4,5,6),(7,8,9),("*",0,"#"))

for numbers in numpad:
    for num in numbers:
        print(num, end=" ")
    print()

