# Nested Loops = A loop within another loop ( outer , inner )
#   outer Loop:
#       inner Loop:
#          inner loop:....

# Nested loops are basically multi loop structure in which multiple functions run synchronously one after another
# the outer loop executes its first iteration, then triggers the following entire inner loop to run from start to finish 
# in each new iterations the nested loops is started and from beggainin hence executing the loop multiple times till the outer loop satisfies/does not satisfy the condition

# Example 1

for m in range(3):
   for n in range(1,20,2):
      print(n, end=" ")       #the end="" is basically to stop the line and continue down we can add any symbol that adds up at the end of the line after execution
   print()

#Example 2

rows = int(input("Enter the number of Rows: "))
columns = int(input("Enter the number of Columns: "))
symbol = input("Enter your symbol to use: ")

for x in range(rows):        #Outer Loop
    for y in range(columns): #inner Loop
      print(symbol,end="")     #Inner Loop Print statement
    print()               #Outer loop Print Statement...this create multiple line for the itteration



# A right angle triangle using nested Loop

for p in range ( 1, 6):
   for q in range(p):
      print("*", end="")
   print()

# a Hollow square nested loop

n = 5

for t in range(n):
   for p in range(n):
      if t == 0 or t == n-1 or p == 0 or p == n-1:
        print("*", end="")
      else:
        print(" ",end="")
print()


# While loop inside a for loop

v = 20

while v > 0:
   for u in range(9):
      print("Do something")
   print()


