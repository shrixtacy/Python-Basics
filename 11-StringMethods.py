#In this Module we gonna play along with some string methods to understand them and use them better 

name = input("Enter Your full name: ")
num = input("Enter Your phone number: ")

result = len(name)         #this function finds the length of the entire string including the empty space
result1 = name.find("D")   #this function finds the first occurance of the given string within the set of string / array and gives the index number of the occurance
result2 = name.rfind("h")  #this is exactly like find function but it gives the index of the last occurance
name2 = name.capitalize()  #It captalizes the first letter of the entire string leaving / making rest small
Upper_case = name.upper()  #It converts the entire string into upper case
lower_case = name.lower()  #It converts the entire string into lower case
name_digit = name.isdigit() #If name contains number it returns false or true
name_alpha = name.isalpha() #It basically checks for the alphabets and return true or false based on it 

num_count = num.count("2")  #Counts the given number's occurances from the string / integer and gives the final value 
new_num = num.replace("2","8")

print(result)
print(result1)
print(result2)
print(name2)
print(Upper_case)
print(lower_case)
print(name_digit)
print( name_alpha)

print(num_count)
print(new_num)


#To know all the comprehensive string functions available

print(help(str))