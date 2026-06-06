print("QUIZ STARTS")

questions=("Which data structure uses FIFO (First In First Out)?",
           "What is the time complexity of binary search?",
           "Which of the following is not a programming language?",
           "What does CPU stand for?",
           "Which keyword is used to define a function in Python?")

options=(("A.Stack ", "B.Queue ", "C.Tree ", "D.Graph "),
         ("A.O(n) ", "B.O(log n) ", "C.O(n log n) ", "D.O(1) "),
         ("A.Python ", "B.Java ", "C.HTML ", "D.C++ "),
         ("A.Central Processing Unit ", "B.Computer Personal Unit ", "C.Central Program Unit ", "D.Control Processing Unit "),
         ("A.func ", "B.def ", "C.function ", "D.define "))

answers=("B","B","C","A","B")

guesses=[]

que_num=0

score=0

for question in questions:
    print("--------------------")
    print(question)
    for option in options[que_num]:
        print(option)
    print("--------------------")
    
    guess=input("enter your answer: ").upper()
    guesses.append(guess)
    if guess == answers[que_num]:
        score+=1
        print("Correct Answer!")
    else:
        print("Wrong Answer!")
        print(f"{answers[que_num]} is Correct Answer.")
    que_num+=1



print("---------------------")
print("       RESULTS       ")
print("---------------------")
print("Your Guesses: ")
for guess in guesses:
    
    print(guess, end=" ")
print("\n Answers: ")

for answer in answers:
    print(answer, end=" ")

print("\n     SCORE      ")
print(f"{score} correct out of 5.")
score=int(score/len(questions)*100 )
print(score,"%")
