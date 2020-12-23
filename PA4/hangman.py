#Objective: practicing with lists, dictionaries, files, exceptions, loops, elif statements, functions and string methods: strip(), join(), isalpha(), upper(), etc.
    
from random import choice, random
#dictionary_file = "dictionary.txt"

def intro():
    print("Welcome to Hangman Game!") #prints into
    HangMan() #runs hangMan method

def HangMan():
    a,b = get_game_options() #saves the returned values as seperated values: https://note.nkmk.me/en/python-function-return-multiple-values/
    size = int(a) #saves first value as the size of the word
    lives = int(b) #saves second value as the number of lives
    
    dashLine = " _"*size #creates a line of dashes based on the size of the word
    OLine = "O"*lives #creates a line of O's to track the number of lives used
    word = wordChoice(size) #sends the size to the wordChoice method to produce a random word to be used in the game
    
    print(dashLine + " lives: " + str(lives) + " " + OLine) #prints the expected format with keeps track of lives and letters
    
    chosenLetters = [] #creates empty list to keept track of letters chosen by the user
    letterIndex = 0 #sets the index of the letter 0
    totalOccur = 0
    
    while lives > 0 and totalOccur < size: #runs while the number of lives is greater than 0
        entry = str(input("Please choose a new letter > ")) # Current entry
        entryPos = [pos for pos, char in enumerate(word) if char == entry] #finds all the index positions of the entry and stores into a list
        totalOccur += len(entryPos) #the length of the list is added to the total number of currect guesses
        chosenLetters.append(entry) #List of all of the entries, appends each entry
        elementString = "" #makes empty string
        if entry in word: #checks if the guess is within the word
                if totalOccur < size: #if the total word has not been printed out yet this runs 
                    print ("You guessed right!")
                    print ("Letters chosen: " + ','.join(chosenLetters)) #seperated the list into a string sperated by commas: https://stackoverflow.com/questions/44778/how-would-you-make-a-comma-separated-string-from-a-list-of-strings
                else: #if the total word is guessed
                    print ("You guessed right!")
                    print ("Congratulations!!! You won! The word was " + str(word.upper()) + "!")
                    answer = input("Would you like to play again [Y/N]?") #asks user if they want to play again
                    answer = answer.upper() #makes entry uppercase so that Y or y is accepted
                    if answer == "Y":
                        HangMan() #this method runs again
                    else: #if the anwer is N or n
                        print ("Goodbye!")
                        break; #allows to end the program
        else: #if the guess is in correct
                lives -= 1 #decreases the number of lives by one
                OLine = OLine.replace("O", "x", 1) #replaces the O with an x for every time a life is lost
                if lives > 0: #if the number of lives is still greater than 0, then function continues and prints following statements
                    print ("You guessed wrong, you lost one life.")
                    print ("Letters chosen: " + ','.join(chosenLetters)) #seperated the list into a string sperated by commas
                else:
                    print ("You guessed wrong, you lost one life.")
                    print ("You lost! The word was " + str(word.upper()) + "!")
                    answer = input("Would you like to play again [Y/N]?") #asks user if they want to play again
                    answer = answer.upper() #makes entry uppercase so that Y or y is accepted
                    if answer == "Y":
                        HangMan() #this method runs again
                    else:
                        print ("Goodbye!")
                        break; #allows to end the program
        for element in word: #runs through each character in word         
            if element in chosenLetters: #if that element is equal to a work in the list chosen letters
                elementString += " " + element #then the _ is replaced with the element
            else:
                elementString += " _" #else the dash is placed
        print (elementString + " lives: " + str(lives) + " " + OLine) #the expected format is printed with the updates from above

def wordChoice(size):
    myList = []
    file = open("dictionary.txt", "r") #opens and reads through text file and saves into another file so it can be edited: https://kite.com/python/answers/how-to-convert-each-line-in-a-text-file-into-a-list-in-python
    for line in file: #runs through each line in the file
        line = line.strip() #remove the "\n" next to each word
        myList.append(line) #the line is then placed into myList
    length1 = [] #creates empty lists that will contain words with its corresponding lengths
    length2 = []
    length3 = []
    length4 = []
    length5 = []
    length6 = []
    length7 = []
    length8 = []
    length9 = []
    length10 = []
    length11 = []
    length12 = []
    for i in myList: #iterates thorugh each word in the list and adds to its correpsonding list based on length
        if len(i) == 1:
            length1.append(i)
        elif len(i) == 2:
            length2.append(i)
        elif len(i) == 3:
            length3.append(i)
        elif len(i) == 4:
            length4.append(i)
        elif len(i) == 5:
            length5.append(i)
        elif len(i) == 6:
            length6.append(i)
        elif len(i) == 7:
            length7.append(i)
        elif len(i) == 8:
            length8.append(i)
        elif len(i) == 9:
            length9.append(i)
        elif len(i) == 10:
            length10.append(i)
        elif len(i) == 11:
            length11.append(i)
        elif len(i) == 12:
            length12.append(i)
    if size == 1: #produces a random word based on the size inputted by the user or by default by the program 
        word = choice(length1)
    elif size == 2:
        word = choice(length2)
    elif size == 3:
        word = choice(length3)
    elif size == 4:
        word = choice(length4)
    elif size == 5:
        word = choice(length5)
    elif size == 6:
        word = choice(length6)
    elif size == 7:
        word = choice(length7)
    elif size == 8:
        word = choice(length8)
    elif size == 9:
        word = choice(length9)
    elif size == 10:
        word = choice(length10)
    elif size == 11:
        word = choice(length11)
    elif size == 12:
        word = choice(length12)
    return word #returns the words to the hangMan method

def get_game_options():
    try: #gets size from user
        size = int(input("Please choose a size of a word to be guessed [3 – 12, default 5] :")) #asks user to input size of word
        if size>12 or size<3: #if the size is not within the boundaries
            size = 5 #default is set to 5
            print("A dictionary word of any size will be chosen.")
        else: #if the entry is within the boundaries
            print("The word size is equal to " + str(size) +".") #prints the expected format containing size specified by the user
    except ValueError: #is the case that a word or "enter" is entered, default is assigned along with expected output
        size = 5
        print("A dictionary word of any size will be chosen.")

    try: #gets lives from user
        lives = int(input("Please choose a number of lives [1 – 10, default 5]:")) #asks user to input number of lives
        if lives>10 or lives<1: #if the size is not within the boundaries
            lives = 5 #default is set to 5
            print("You have 5 lives.")
        else: #if the entry is within the boundaries
            print("You have " + str(lives) + " lives.") #prints the expected format containing size specified by the user
    except ValueError: #is the case that a word or "enter" is entered, default is assigned along with expected output
        lives = 5
        print("You have 5 lives.")
    
    return size, lives #returns the number of lives and size or word to hangMan method 

intro() #runs intro method

