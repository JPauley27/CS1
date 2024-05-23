'''
Author: Jack Pauley
Description: I designed a code that plays rock paper scissors against the user. It asks the user which one they want. I also coded a score counter so after everygae it adds a point to the winners score then asks them if they want to play again if they say yes the code will run again if they say no then it tells them the score and it ends. 
Date: 11/17/23
Bugs: None
Challenges: Point Counter
'''
import random
import time
import sys
import os
#brings in the random, os, time and system libraries in order to use different functions from those libraries

userpoints = 0# this displays the users points before the game has started. It is the point counter
computerpoints = 0# this is the computer points before the game has started.
rps = ["rock","paper","scissors"]# This is the list the computer chooses from.
destroy= ["d","e","s","t","r","o","y"]#this is the list of letters
question= str.lower(input("do you want to play?"))# this asks the user if they want to play rock paper scissors
if question== ("yes"): # if they respond yes the code continues
    while True: #loops until code are broken
        print("the user has", userpoints)#this shows the users points to the user
        print ("the computer has", computerpoints)#this shows the users points to the user
        print("Rock, Paper, Scissors say shoot...") #this is printing rock paper says shoot
        user_rps = str.lower(input("enter decision: "))#  this asks the user to enter their decision on whether they want to put rock paper or scissors
        bot_rps = random.choice(rps)# This tells the computer to pick a random choice from the rps list

        if user_rps == "destroy the code": # if the user inputs destroy the code a will trigger a sequence of events
            print("3") # prints the word 3
            time.sleep (1) # the code wont do anything for a second
            print("2") #prints the word 2
            time.sleep (1)# the code wont do anything for a second
            print("1") #prints the word 1
            time.sleep (1)# the code wont do anything for a second
            print("KABOOM!!") #prints the word Kaboom
            break # breaks the loop

        if user_rps not in rps: # if the user input is not in the rps list
            print("Invalid") # prints the word invalid
        else:# if the user prints anything else than yes or no
            if user_rps == bot_rps: # if they both put the same response they tie
                print("tie.")# the code prints tie
            elif user_rps == "rock" and bot_rps == "paper":  # if the user puts rock and the bot puts paper the bot wins
                print("bot wins")# prints the bot wins
                computerpoints +=1 # add one point to the bots score
            elif user_rps == "rock" and bot_rps == "scissors": # if the user puts rock and the bot puts scissors the user wins
                print("the user wins!!")# prints the words  the user wins
                userpoints += 1# adds a point to the users score
            elif user_rps == "paper" and bot_rps == "scissors":# if the user puts paper and the bot puts scissors  the bot wins
                print("the bot wins")# prints the words the bot wins
                computerpoints +=1# add one point to the computers score
            elif user_rps == "paper" and bot_rps == "rock": # if the user puts paper and the bot puts rock the user wins
                print("the user wins!!")# prints the words the user wins
                userpoints += 1 # adds one point to the users score
            elif user_rps == "scissors"and bot_rps == "rock":# if the user puts scissors and the bot puts rock  the bot wins
                print(" the bot wins") # prints the words the bot wins
                computerpoints +=1#adds a point to the bots score
            elif user_rps == "scissors" and bot_rps == "paper":# if the user puts scissors and the bot puts paper the user wins
                print("the user wins!!")# prints the words the user wins
                userpoints += 1 # adds a point to the users score
            
            print(f"user - {userpoints}, computer - {computerpoints}") #this prints the users points and the computers points
            if len(destroy)>= 1: #if the lenght of destroy is greater than one 
                index = random.randint(0,len(destroy)-1)# this takes a ranodm index from the the destroy list 
                print(destroy[index])# prints one letter from the destroy index
                destroy.pop(index)# it removes a item form the destroy list using index
            else:# if the user prints anything other than yes or no
                secret= input(" What was the secret word?")
                if secret== "destroy":
                    print("3") # prints the word 3
                    time.sleep (1) # has a one second delay
                    print("2")#prints the word 2
                    time.sleep (1)# has a one second delay
                    print("1")#print the word 1
                    time.sleep (1)# has a one second delay
                    print("KABOOM!!")#prints the word Kaboom
                    os.remove(r"C:\Users\jpauley27\Desktop\CS1\RPS.py")# os. remove removes the code from my computer
                    sys.exit()# this stops the code without asking the users input
            
            while True:
                playagain = str.lower(input("do you want to play again? ")) #this asks the user if they want to play rock paper scissors again

                if playagain == ("yes"):# if the user responds yes to the question it runs again 
                    break # stops the code
                elif playagain == ("no"): # if they respond no it starts the destruction countdown
                    print("3") # prints the word 3
                    time.sleep (1) # has a one second delay
                    print("2")#prints the word 2
                    time.sleep (1)# has a one second delay
                    print("1")#print the word 1
                    time.sleep (1)# has a one second delay
                    print("KABOOM!!")#prints the word Kaboom
                    sys.exit()# this shuts down all the code without the user having any say
                else:# if the user prints anything other than yes or no
                    print("thats not a valid statment!!!")#prints the words thats not a valid statement
else: #if the user prints any else than yes or no
    print("Goodbye!")#prints the word goodbye

