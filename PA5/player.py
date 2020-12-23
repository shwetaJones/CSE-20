#!/usr/bin/env python3
# Name: Shweta Jones(shsujone)
# Date: June 7, 2020
#player.py: acts as player, asks user for input and chages board based on values
class Player:
    #the player method allows for user to make changes to the player, and also makes changes within the board
    def __init__(self, name, sign):
        # initalizes name and sign of player
        # input: the name and sign of the user is given
        # output: the initilized values are saved, nothing is returned
        self.name = name
        self.sign = sign
    
    def get_sign(self):
        # return an instance sign
        # input: no input is given 
        # output: the updated sign is returned
        return self.sign
    
    def get_name(self):
        # return an instance name
        # input: no inout is given 
        # output: the updated name is returned
        return self.name
    
    def choose(self, board):
        # prompt the user to choose a cell
        # if the user enters a valid string and the cell on the board is empty, update the board
        # otherwise print a message that the input is wrong and rewrite the prompt
        # use the methods board.get_size(), board.isempty(index), and board.set(index, sign)
        # you need to convert A1, B1, …, C3 cells into index values from 1 to 9
        # you can do the conversion here in the player.py or in the board.py
        # this implemenation is up to you
        # input: the board is given by main
        # output: the user is asked to enter a spot, and if valid the board is updated and returned
        valid = True
        while valid:
            userInput = input(self.name + ", " + self.sign + ": Enter a cell [A-C][1-3]:") #prompts the user to enter a spot
            boardDict = {"a1":0, "b1":1, "c1":2, "a2":3, "b2":4, "c2":5, "a3":6, "b3":7, "c3":8, "A1":0, "B1":1, "C1":2, "A2":3, "B2":4, "C2":5, "A3":6, "B3":7, "C3":8} #Creates a dict that includes both upper and lower case, mainly bc the assignment didn't specify which the user will enter 
            if userInput in boardDict: #checks if entry is valid
                index = boardDict[userInput] #sets index to dictionary value
                if board.isempty(index) == True: #checks if the spot is empty 
                    board = board.set(index, self.sign) #sets the empty spot with the sign
                    return board #returns to main
                    valid = False #allows to leave while loop
                else: #runs when the spot is not empty
                    print ("You did not choose correctly")
                    valid = True #runs through loop again
            else: #runs when entry is not valid
                print ("You did not choose correctly")
                valid = True #runs through loop again
