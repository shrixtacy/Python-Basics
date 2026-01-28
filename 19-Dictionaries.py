#Dictionary = a collectoon of {key:value} pairs
#             ordered & changeable. No duplicates

capitals = {"USA":"Washington D.C.",
            "INDIA": "New Delhi",
            "China": "Beijing",
            "Russia":"Moscow"}

#print(dir(capitals))
#print(help(capitals))


#Methods of dictionary

print(capitals.get("USA"))       #it gets the value of the key
print(capitals.get("Japan"))     #this will return none because Japan does not existis within keys

any_capital = input("Enter any country name: ")
if capitals.get(any_capital):
    print("That Capital Exists !")
else:
    print("It does not exists buddy !")  


capitals.update({"Germany":"Berlin"})   #this will add a new parameter at the last of the dictionary
capitals.update({"USA":"Detroit"})      #this will update the existing parameter USA

capitals.pop("China")                   #Pop is basically used to remove a specfic cell
capitals.popitem()                      #popitem is used to remove the last cell

print(capitals)


#capitals.clear()    this will clear all the key value pairs


Keys = capitals.keys()    #This only prints the keys of the dictionary
print(Keys)

for key_val in Keys:     #This prints all the  of the keys
    print(key_val)

Values = capitals.values()    #This prints only the values
print(Values)

for value in Values:
    print(value)

items = capitals.items()     #This fetches all the items in the dictonary
print(items)

for key, value in capitals.items():
    print(f"{key}: {value}")