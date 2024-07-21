# -*- coding: utf-8 -*-
"""
Created on Sat Jul  6 21:57:15 2024

@author: suyash morye
"""

import random

print ("~~~Welcome to RPS~~")

user_score = 0


comp_score = 0

ties = 0

name = input("Enter your name here: ")


print ("""

1. Paper vs Rock --> Paper

2. Rock vs Scissors --> Rock

3. Scissors vs Paper --> Scissors""")

print ("""Choices are:

1. Rock

2. Paper

3. Scissors""")


choice = int(input("enter your choice from 1-3: "))

print ()
while choice > 3 or choice < 1:  
    choice= int(input("enter valid input"))

if choice == 1: 
    user_choice = "Rock"

elif choice == 2: 
    user_choice = "Paper"

else: 
    user_choice = "Scissors"

print ("The user's choice is", user_choice)


computer = random.randint(1,3)

if computer == 1: 
    comp_choice = "Rock"

elif computer ==2: 
    comp_choice = "Paper"

else: 
    comp_choice = "Scissor"

print("The Computer choice is",comp_choice)


if ((user_choice == "Paper" and comp_choice == "Rock") or (user_choice=="Rock" and comp_choice== Paper)): 
    print("Paper wins")
    result = "Paper"

elif ((user_choice == "Scissor" and comp_choice == "Rock") or (user_choice=="Rock" and comp_choice== Scissor)): 
    print("Rock wins")
    result = "Rock"

else: 
    print("Scissor wins")
    result = "Scissor"


if result == "Tie": 
    ties +=1

elif result == user_choice:  
    print("User wins")
    user_score += 1

else:  
    print("Computer wins")
    comp_score += 1

print ("Scores are")

print (name, "'s score is", user_score)

print ("computer's score is", comp_score)

print ("ties are ", ties)


repeat = input("do you want to play again ?")

if repeat=="No" or repeat == "No":
    break
      

print("Game is over")
print("Thanks for playing ....!!!!!")
