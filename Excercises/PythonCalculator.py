#Make a Python calculator

Operator = input("Choose an operator (+ , - , * , /) : ")

a = float(input("Enter a number: "))
b = float(input("Enter another number: "))

if Operator == "+":
    sum = a + b
    print(f"The sum of both number is {round (sum, 2)} ")
elif Operator == "-":
    sub = a - b
    print(f"The sub of both number is {round(sub,2)}")
elif Operator == "*":
    multi = a * b
    print(f"The multiplication of both number is {round(multi, 2)}")
elif Operator == "/":
    div = a / b
    print(f"The division of both number is {round(div,2)}")
else:
    print("Buddy choose a Valid OPERATOR...GODDAMMIT")