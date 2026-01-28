#Making a number guesseing game between 1 - 9

import random

Low = 1
High = 9 
Answer = random.randint(Low,High)
Guesses = 0 
is_running = True

print("----GUESS THE NUMBER----")
print()
print(f"Enter any number between the range of {Low} to {High}")

while is_running:

    guess = input("Enter Your Guess: ")

    if guess.isdigit():
        guess = int(guess)
        Guesses += 1

        if guess < Low and guess > High:
            print("Out of Range")
            print(f"Enter any number between the range of {Low} to {High}")
        elif guess > Answer:
            print("Too High! Try again")
        elif guess < Answer:
            print("Too Low! Try Again")
        else:
            print(f"You are correct...The answer was {Answer}")
            print(f"The number of Guesses: {Guesses}")

    else:
        print("The Guess is Invalid")
        print(f"Please Enter any number between the range of {Low} to {High}")