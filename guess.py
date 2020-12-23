# assignment: programming assignment 2
# author: Shweta Jones
# date: 04/20/2020
# file: guess.py is an interactive game that asks the user to guess a number from 1 to 10
# input: only integers from 1 to 10
# output: interactive messages

from random import random
print ("Play a game: Guess My Number.")
gameOn = True
while gameOn:
    
    number = int (random() * 10 + 1) #allows for a # between 1 and 10 get generates
    attempts = 0 #sets the attempts to 0
    print("You have three attempts to guess my number.")
    
    for attempts in range (0,3): #this function runs when attempts are less than 3    
        guess = input ("Please enter a number from 1 to 10:")
        guess = int(guess) #makes the input an int rather than a string
        
        if guess < number: #runs when the user guess is less than the random #
            print("You guessed wrong, Your number is smaller than mine.")
            print("Guess again. Please enter a number")
            attempts = attempts + 1 #adds to the attempt count
            
        elif guess > number: #runs when the user guess is more than the random #
            print("You guessed wrong, Your number is bigger than mine.")
            print("Guess again. Please enter a number")
            attempts = attempts + 1 #adds to the attempt count
            
        elif guess == number: #runs when the user guess is equal to the random #
            print ("You guessed right. Congratulations you won!")
            gameOn = False #allows it to go to the if/else function
            break; #allows it to leave the for loop
        
    if attempts == 3: #runs when attempts are over 3
        print ("Sorry, you lost. My number is " + str (number) + ".")
        gameOn = False #allows it to go to the if/else function
               
    if gameOn == False: 
        answer = input ("Would you like to play again [Y/N]?")
        
        if answer == 'Y':
            gameOn = True #allows the program to start from the top
            
        elif answer == 'y':
            gameOn = True #allows the program to start from the top
            
        elif answer == 'N':
            print ("Goodbye!")
            
        elif answer == 'n':
            print ("Goodbye!")
