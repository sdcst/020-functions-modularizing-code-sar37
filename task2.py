"""
Task 2:
Create a program to play a number guessing game
There should be a function:
title()
displays instructions and how to play

game()
plays the games
"""
def title():
    print("guessing game")
    print("instructions on how to play: guess a number between 1-5, guess until you get the correct number.")
    
def game():
    n =""
   
    while n != 2:
        n = input("guess a number from 1-5")
        n = float(n)
        if n != 2:
            print("try again")
        
        else:
            print(" Nice, you got it right!")

title()
game()