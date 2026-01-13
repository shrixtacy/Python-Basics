#For Loops = execute a block of code a dixed numvber of times.
#             you can iterate over a range , string , sequence , etc

credit_card = "1234-5678-9012-3456"

for x in credit_card: 
    print(x)

#another example

for y in range(1,100):      #this will print all the numbers within given range
    print(y)

for i in range(1,100,2):    #this will print only the 2 number skipped values within given range
    print(i)

for m in reversed(range(1,10)):  #this will print all the reversed values within ranges
    print(m)
