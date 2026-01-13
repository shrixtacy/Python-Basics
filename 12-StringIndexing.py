# Indexing = Accesssing elements of a sequence using [] (indexing operator)
#   [start : end : step]  - format of string

credit_number = "1234-5678-9012-3456"

print(credit_number[0])   #this prints the value of 0th index of string ( it only gives the first value )
print(credit_number[0:8])  #this prints the value from 0th index to 8th index
print(credit_number[5:9]) 

print(credit_number[5:])  #in this it will print all the values starting from 5th index to last index
print(credit_number[:5])  #this will print all the values starting from 0th index till 5th index

print(credit_number[-1])  #this negative index will print the value of the last index of entire string


print(credit_number[::2]) #this basically print every second character of our string 
print(credit_number[::3]) #this basically prints every third character of our string


#Lets  create a program to get the last 4 digit of a credit_card number

credit = "1234-5678-9012-1223"

last_digit = credit[-4:]

print(f"This is your credit card XXXX-XXXX-XXXX-{last_digit}")