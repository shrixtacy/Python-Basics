# Python compund interest calculator
# The main formula of compund interest => A = P ( 1 + r/n )^t
# A = Final amount
# P = initial Principal balance
# r = interest rate
# t = number of time periods elapsed

principle = 0
rate = 0 
time = 0


while principle <= 0:
    principle = float(input("Enter the Principle Amount: "))
    if principle <= 0:
        print("Principle cannot be less than or equal to zero")

while rate <= 0:
    rate = float(input("Enter the rate of Interest: "))
    if rate <= 0:
        print("Interest Rate cannot be less than or equal to zero")

while time <= 0:
    time = float(input("Enter the Time elapsed in yrs: "))
    if time <= 0:
        print("Time Period can't be less than or equal to zero")


Total_Amount = principle * pow((1 + (rate/100)), time)

print(f"Balaance after {time} year/s: ${Total_Amount:.2f}")