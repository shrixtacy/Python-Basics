#Default Arguments = A default value for certain parameters
#                    Default is used when that argument is omitted
#                    make your function more flexible, reduces number of arguments
#                    1. Positional, 2. DEFAULT, 3.Keywords, 4.Arbitrary


def net_price(list_price, discount=0, tax=0.05):  #We set the default values for the arguments so they don't need to rpeat them....
    return list_price * (1-discount) * (1+tax)

print(net_price(500))
print(net_price(500, 0.1, 0))


#Count up Timer
import time

def count(start,end):
    for x in range(start,end+1):
        print(x)
        time.sleep(2)
    print("Done!")
          
count(15,30)