"""
Python Development Techdegree
Project 1 - The Number Guessing Game
--------------------------------
"""
import random

attempt_count = 1

high_score = 0

def start_game():
    
    print("Welcome to Nathans number guessing game!")

    answer = random.randrange(1,11)
    attempt_count = 1
    
    global high_score

    if high_score > 0:
        print("The current high score is {}".format(high_score))

    while True:
        try:
            guess = int(input("pick a number from 1-10\n"))
        
            if  guess < 1:
                print("That number is not between 1 and 10.\n")
                continue
            
            elif guess > 10:
                print("That number is not between 1 and 10.\n")
                continue
       
        except ValueError:
            print("Please enter a number.")
            continue
           
        if guess < answer:
            print("Sorry, it's higher. Try again\n")
            attempt_count += 1
            continue
            
        elif guess > answer:
            print("Sorry, it's lower. Try again\n")
            attempt_count += 1
            continue
            
        elif guess == answer:
            if attempt_count < high_score or high_score == 0:
                high_score = attempt_count
            break
            
    print("Congratulations, you got it right, and it only took {} attempts".format(attempt_count))
    print("Would you like to try again?")
    
    while True:
        restart = input("(Y)es/(N)o)\n")
        
        if restart.lower() == "y":
            start_game()
                

        elif restart.lower() == "n":
            print("Thank you for playing my game!")
            exit(0)    
                
start_game()