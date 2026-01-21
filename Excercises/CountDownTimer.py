# Lets create a countdown timer in python

import time            #importing time module to our code
time.sleep(3)          #sleep function basically waits till the number of seconds within sleep is up then it further executes
print("Lessgoooo")


# countdown timer
countdown_timer = 10   #setting up number

for i in range(countdown_timer, 0 , -1):
    time.sleep(1)      #setting up delay by 1 seconds
    print(i)

print("Time's Up")


#Countdown timer

my_time = int(input("Set the timer number: "))

for x in range(my_time, 0, -1):  #step is negative to count backwards from my_time to 0 
    seconds = x % 60
    minutes = int(x / 60) % 60
    hours = int(x/3600)
    print(f"{hours:02}:{minutes:02}:{seconds:02}")
    time.sleep(1)


