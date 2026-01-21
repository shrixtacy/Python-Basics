# Collections = single "variable" used to store multiple values
# List = [] ordered and changeable. Duplicated OK
# Set = {} unordered and immutable/inchangable, but add/remove Ok. No duplicates
# Tuples = () ordered aND UUnchangeable.duplicates OK. faster

#Singular variable
fruit = "apple"
print(fruit)

#---------------------------

#List Collection
fruits = ["apple","Banana","Coconut"]
print(fruits)                            #this prints the list 
print(fruits[0])                         #accessing a particular index of the collection 
print(fruits[::2]) 
print(len(fruits))                       #this will print the lentgh of the list

fruit1 = "apple" in fruits               #this will print true if the given value "" is present in the list fruit
fruit2 = "pineapple" in fruits
print(fruit1)
print(fruit2)

fruits.append("pear")                    #Append is used to add a element to the end of the list 
fruits.remove("apple")                   #Remove is used to remove a element from the list
fruits.insert(2, "Jackfruit")            #Insert function basically adds a element to the list at required index number (index number , "Element to be added")


fruits.sort()                            #This basically sorts the elements based alphabatically or numerologically in a list
fruits.reverse()                         #this basically re-sorts the elements in the order we placed them at input before sort function
#fruits.clear()                           #this cleas the entire list
print(fruits.index("Jackfruit"))         #This clears the particular element from the list
print(fruits.count("banana"))

print(fruits)

for x in fruits:                         #for loop to print everything within the collection
    print(x)

#This print statement will print all the important methods that our list can perform
#print(dir(fruits))
#print(help(fruits))


#----------------------------

#Set Collections - they are not ordered and have multiple other sets of methods and functions that we can run on them apart from list

vegetables = {"tomoato" , "onion", "cabbage", "cucumber"}

print(vegetables)

vegetables.add("Potato")
print(vegetables)

vegetables.pop()
print(vegetables)

print(vegetables.add("tomato"))


#------------------------------


#Tuplees - it is a collection that that are ordered and unchangeable, duplicates are acceptable in tuple and it is much faster than list or sets.


things = ("duck", "dog", "cat", 9, 8, 7, 6.3, "table", "table")

print(things.index(6.3))

for i in things:
    print i