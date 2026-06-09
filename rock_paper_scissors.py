import random

options=["rock", "paper", "scissors"]
person_score=0
computer_score=0

chance=3
while chance:
    computer=random.choice(options)
    person=input("Choose( rock, paper, scissors): ").lower()

    if person == computer:
        print("Draw!")  

    if computer=="rock":
        if person=="scissors":
            computer_score+=1
        elif person=="paper":
            person_score+=1
    


    if computer=="paper":
        if person=="rock":
            computer_score+=1
        elif person=="scissors":
            person_score+=1
    


    if computer=="scissors":
        if person=="paper":
            computer_score+=1
        elif person=="rock":
            person_score+=1
    

    
    print(f"Person: {person} and score: {person_score}.")
    print(f"Computer: {computer} and score {computer_score}.")

    chance-=1


if computer_score > person_score:
    print("Computer Won!")
elif person_score > computer_score:
    print("Person Won!")
else:
    print("Match Draw!")