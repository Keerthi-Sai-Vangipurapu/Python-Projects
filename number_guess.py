import random

lowest_num=1
highest_num=1000

answer= random.randint(lowest_num, highest_num)
guesses=0

is_running= True

while is_running:
    guess=input("enter your guess: ")
    
    if guess.isdigit():
        guess=int(guess)
        guesses+=1

        if guess>highest_num or guess<lowest_num:
            print(f"The number is out of range.")
            print(f"Please select a number between {lowest_num} and {highest_num}.")

        elif guess<answer:
            print(f"Too low! Try again!")
        elif guess>answer:
            print(f"Too high! Try again!")
        else:
            print(f"CORRECT! The answer was {answer}.")
            print(f"Number of guesses: {guesses}")
            is_running=False

    else:
        print("Invalid Guess")
        print(f"Please select a number between {lowest_num} and {highest_num}")


    

