# -*- coding: utf-8 -*-
"""
Created on Mon Aug 31 12:37:23 2020

@author: Thong
"""
#Rock, papers, scissors game


#NEXT STEP CREATE A CLASS for RPS
#CREATE A LIBRARY OF GAMES

#Import the library
import random as r

#creating a class
def RPS():

#Assign variables to guess and answer
    guess = str(input("Let's play RPS, type one of the options in: rock, paper, scissor:"))
    answer = r.choice(["rock", "paper", "scissor"])

#Draw outcome
    if guess == answer:
        print ("You draw, try again \nThe computer chose:", answer)
#Win outcome for (Rock vs )
    elif (guess == "rock" and answer == "scissor") or (guess == "paper" and answer == "rock") or (guess == "scissor" and answer == "paper"):   
        print ("You win \nThe computer chose:", answer)       
    
#Lose outcome
    elif (guess == "rock" and answer == "paper") or (guess == "paper" and answer == "scissor") or (guess == "scissor" and answer == "rock"): 
        print ("You lose \nThe computer chose", answer) 
    
#Wrong input
    else:
        print ("Input 'rock', 'paper', 'scissor'")
        return RPS()
        
while True:
    game = input("Do you want to play RPS?")
    if game == 'yes':
        RPS()
    elif game == 'no':
        break
    else: 
        print("Try 'yes' or 'no'")
        

        
        