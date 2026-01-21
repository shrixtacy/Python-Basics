Questions = ("What is National Animal of India ?",
             "What is the National Anthem of India ?",
             "When did India get its Independance ?")
Options = (("A. Tiger", "B. Elephant", "C. Cow"),
           ("A. Jana Gana Mana", "B. Shiv Strotram", "C. Vande Mataram"),
           ("A. 1945", "B. 1948", "C. 1947"))

Answers = ("A", "A", "C")

Guesses = []
score = 0
question_num = 0


for question in Questions:
    print("--------------------")
    print(question)
    for option in Options[question_num]:
        print(option)
    
    guess = input("Enter Your Guesses (A , B, C): ").upper()
    Guesses.append(guess)
    if guess == Answers[question_num]:
        score += 1
        print("Correct !")
    else:
        print("Wrong Guess")
        print(f"The Right Answer is {Answers[question_num]}")

    question_num +=1

print()
print("--------EVALUATION METRICS--------")

print("Guesses: ", end = " ")
for guess in Guesses:
    print(guess, end = " ")
print()

print("Answers: ", end = " ")
for correct_answers in Answers:
    print(correct_answers, end = " ")
print()


print("------Total Score & Percentage------")

print(f"The total numeric Score is {score} out of 3")
score_percent = int(score/len(Questions)*100)
print(f"The score percentage is {score_percent}")


    