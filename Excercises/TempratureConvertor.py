#Make a temprature convertor with logic of  celcius = F - 32 * 5/9 & Farenheit = C * 9/5 + 32



unit = input("What is the current unit of Temp F or C ?: ")
value = float(input("What is the current temprature ?: "))

if unit == "f":
    print("Converting to celsious....")
    celcius = (value - 32)*(5/9)
    print(f"The Temprature in Celcius is {celcius} degrees")

elif unit == "c":
    print("Converting to farenheit....")
    farenheit = (value * (9/5)) + 32
    print(f"The temprature in Farenheit is {round(farenheit,2)}")

else:
    print("Wrong Unit bruh !!")


