#Python Quiz Game

Questions = ("What is the full name of Thor ?",
             "When did Avengers Endgame take place ?",
             "what is the full name of Peter Parker's Aunt ?",
             "What radiation did Bruce go through to become Hulk ?",
             "Serum name that was injected in Steve Rogers is ?")

Options = (("A. Thor Odinson", "B. Odinson Thor", "C. Mijolnir Wielder Thor"),
           ("A. 2021", "B. 2023", "C. 2025"),
           ("A. Aunt May","B. May Parker", "C. Mary Parker" ),
           ("A. Gamma Rays", "B. Super Soldier Serum", "C. Admantinum Serum"),
           ("A. Gamma Serum", "B. Super Soldier Serum", "C. Black serum"))

Answers = ("A", "C", "B", "A", "B")

guesses = []
score = 0
Question_Num = 0


for question in Questions:
    print("-------------------")
    print(question)
    for option in Options[Question_Num]:
        print(option)

    guess = input("Enter (A, B, C, D): ").upper()
    guesses.append(guess)
    if guess == Answers[Question_Num]:
        score +=1
        print("CORRECT !")
    else:
        print("INCORRECT !")
        print(f"{Answers[Question_Num]} is the Correct Answer")

    Question_Num += 1


print()
print("------EVALUATION METRICS-------")

print("Guesses: ", end =" ")
for guess in guesses:
    print(guess, end = " ")
print()

print("Answers: ", end =" ")
for answer in Answers:
    print(answer, end = " ")
print()

print()
print("--------YOUR TOTAL SCORE----------")
score = int(score/len(Questions)* 100)
print(f"You scores {score} out of 5")


