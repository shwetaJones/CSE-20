#!/usr/bin/env python3
# Name: Shweta Jones(shsujone)
# Date: June 7, 2020
#board.py: changes values within the board based on player changes, also displays the board
class Board:
    def __init__(self):
        # initializes the board with certain values
        # input: no values are given to this method
        # output:initialized values
        self.sign = " " #sets sign to empty first
        self.size = 3 #sets the size of board
        self.board = list(self.sign * self.size**2) #created board
        self.winner = "" #sets winner to nothing
        
    def get_size(self):
        # return the board size (an instance size)
        # input: no input is given
        # output: the size of the board is returned
        return self.size
    
    def get_winner(self):
        # return the winner (a sign O or X) (an instance winner)
        # input: no input is given
        # output: the updated winner is given
        return self.winner
        
    def set(self, index, sign):
        # mark the cell specified by the index with the sign (X or O)
        # input: the index of the board and the sign of the player is given
        # output: the updated board ir returned to player
        self.board[index] = sign #sets the board position to the sign given by player
        return self.board
    
    def isempty(self, index):
        # return True if the cell specified by the index is empty (not marked with X or O)
        # input: the index of the user input is given
        # output: a boolean is returned based on if the spot is empty of not
        empty = True
        if self.board[index] == " ": #sets to true to player is spot is empty
            empty = True
        else: #sets to false if spot if not empty
            empty = False
        return empty 
    
    def isdone(self):
        # check all game terminating conditions, if one of them is present, assign the var done to True
        # depending on conditions assign the instance var winner to O or X
        # return done
        # input: no input is given to this method
        # output: checks to see if the game has ended, if so True is returned otherwise, False is returned
        done = False
        whiteCount = 0
        for element in self.board: #iterates through board and counts whitespaces
            if element == " ":
                whiteCount +=1
        if self.board[0] == self.board[1] == self.board[2] != " ": #top row
            if self.board[0] == "X": #sets winner to X, otherwise O
                self.winner = "X"
            else:
                self.winner = "O"
            done = True
        elif self.board[3] == self.board[4] == self.board[5] != " ": #middle row
            if self.board[3] == "X": #sets winner to X, otherwise O
                self.winner = "X"
            else:
                self.winner = "O"
            done = True
        elif self.board[6] == self.board[7] == self.board[8] != " ": #bottom row
            if self.board[6] == "X": #sets winner to X, otherwise O
                self.winner = "X"
            else:
                self.winner = "O"
            done = True
        elif self.board[0] == self.board[3] == self.board[6] != " ": #first column
            if self.board[0] == "X": #sets winner to X, otherwise O
                self.winner = "X"
            else:
                self.winner = "O"
            done = True
        elif self.board[1] == self.board[4] == self.board[7] != " ": #second column
            if self.board[1] == "X": #sets winner to X, otherwise O
                self.winner = "X"
            else:
                self.winner = "O"
            done = True
        elif self.board[2] == self.board[5] == self.board[8] != " ": #third column
            if self.board[2] == "X": #sets winner to X, otherwise O
                self.winner = "X"
            else:
                self.winner = "O"
            done = True
        elif self.board[0] == self.board[4] == self.board[8] != " ": #left diagonal
            if self.board[0] == "X": #sets winner to X, otherwise O
                self.winner = "X"
            else:
                self.winner = "O"
            done = True
        elif self.board[2] == self.board[4] == self.board[6] != " ": #right diagonal
            if self.board[2] == "X": #sets winner to X, otherwise O
                self.winner = "X"
            else:
                self.winner = "O"
            done = True
        elif whiteCount == 0: #if the all spaces within the board is filled, then done is set to True
            done = True     
        else: #if all above fails, then False is returned
            done = False
        return done
        
    def show(self):
        # draw the board
        # input: no input is given for this 
        # output: the updated board is returned
        print ("   A   B   C")
        print (" +---+---+---+")
        print ("1| " + self.board[0] + " | " + self.board[1] + " | " + self.board[2] + " | ")
        print (" +---+---+---+")
        print ("2| " + self.board[3] + " | " + self.board[4] + " | " + self.board[5] + " |")
        print (" +---+---+---+")
        print ("3| " + self.board[6] + " | " + self.board[7] + " | " + self.board[8] + " |")
        print (" +---+---+---+")
        print()

