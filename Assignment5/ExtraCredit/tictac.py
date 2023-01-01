#!/usr/bin/env python3
# Name: Shweta Jones(shsujone)
# Date: June 7, 2020
#Main game code

from board import Board
from player import Player, AI, SmartAI 

print("Welcome to TIC-TAC-TOE Game!")
while True:
    board = Board() #runs Board class, initializes values
    player1 = AI("Bob", "X", board) #provides player 1 information
    player2 = SmartAI("Alice", "O", board)
    turn = True
    board.show() #prints board which is empty
    while True:
        if turn:
            player1.choose() #gets input and updates board based on user input for player 1
            turn = False
        else:
            player2.choose() #gets input and updates board based on user input for player 2
            turn = True
        if board.isdone(): #when the board is 
            break
        board.show() #print the board
    if board.get_winner() == player1.get_sign(): #when the winner is the sign of player 1, winner displayed
        board.show()
        print(f"{player1.get_name()} is a winner!")
    elif board.get_winner() == player2.get_sign(): #when the winner is the sign of player 2, winner is displayed
        board.show()
        print(f"{player2.get_name()} is a winner!")
    else: #when there is no winner, it is a tie
        board.show()
        print("It is a tie!")
    ans = input("Would you like to play again? [Y/N] ").upper() #asks user for answer, makes into upper
    if (ans != "Y"): #when anything other than y is entered, game is done
        print("Goodbye!")
        break #leaves code



