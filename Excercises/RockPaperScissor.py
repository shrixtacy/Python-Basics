import random

Options = ("rock","paper","scissors")
running = True

while running:

    Player = None
    Computer = random.choice(Options)

    while Player not in Options:
        Player = input("Enter your choice (Rock, Paper, Scissor): ").lower()

    if Player == Computer:
        print("Its a Tie !")
    elif Player == "rock" and Computer == "paper":
        print("Computer Wins! Paper wraps Rock")
    elif Player == "scissors" and Computer == "rock":
        print("Computer Wins! Rock Breaks the Scissor")
    elif Player == "paper" and Computer == "scissors":
        print("Computer Wins! Scissor cuts the Paper")
    else:
        print("You Win! Woohoooo")

    if not input("Want to play again ? (Y/N): ").lower() == "y":
        running = False
print("Thanks for Playing !")