# assignment: programming assignment 3
# author: Shweta Jones
# date: 05/03/2020
# file: calculator.py is a program that (put the description of the program)
# input: The input for this program is the operation the user wants to use as well as the numbers the user wants
# output: The out would consist of the results answer from the operation and values from the user

gameOn = False

def calculate():
    global gameOn #makes the gameOn variable to global so that it can be accessed and changed in different methods
    print ("Welcome to Calculator Program!")
    gameOn = True #sets variable to true to run the gameOn while loop
    while gameOn:
        print ("Please choose one of the following operations:")
        print ("Addition – A")
        print ("Subtraction – S")
        print ("Multiplication – M")
        print ("Division – D")
        operation = input ("> ") #makes the input equal to the operation wanted by the user
        if operation in ('A', 'S', 'M', 'D'): #checks if the operation is a valid char  
            firstValid = False #sets firstValid to false
            while firstValid is not True: #while loop determines if first number is valid
                x = input ("Please enter the first number: ") #asks user for first number 
                if isfloat(x) == True: #if value is valid, then the following programs run
                    secondValid = False #sets secondValid to false
                    while secondValid is not True:#while loop determines if second number is valid
                        y = input ("Please enter the second number: ") #asks user for second number 
                        if isfloat(y) == True: #if value is valid, then the following programs run
                            print ("The first number is " + str(x))
                            print ("The second number is "+ str(y))
                            if operation == 'A': #if the A is entered then it runs the add method
                                answer = add(x,y) #runs add method and gives two values
                                print (str(x) + " + " + str(y) + " = " + str(answer)) #prints out values in string form
                                firstValid = True #allows for the while loop to end
                                secondValid = True #allows for the while loop to end
                            elif operation == 'S': #if the S is entered then it runs the add method
                                answer = subtract(x,y) #runs subtract method and gives two values
                                print (str(x) + " - " + str(y) + " = " + str(answer))
                                firstValid = True 
                                secondValid = True
                            elif operation == 'M': #if the M is entered then it runs the add method
                                answer = multiply(x,y) #runs multiply method and gives two values
                                print (str(x) + " x " + str(y) + " = " + str(answer))
                                firstValid = True
                                secondValid = True
                            elif operation == 'D': #if the D is entered then it runs the add method
                                answer = divide(x,y) #runs divide method and gives two values
                                print (str(x) + " / " + str(y) + " = " + str(answer))
                                firstValid = True
                                secondValid = True
                            again() #runs the again method 
                        else: #if second number is not valid, the following print statement runs
                            print ("You did not choose a second number.")
                else: #if first number is not valid, the following print statement runs
                    print ("You did not choose a first number.")
        else: #if operation is not valid, the following print statement runs
            print ("You did not choose the operation correctly.") 
            again() #runs the again method 

def isfloat (token) : 
    """checks if the entered value is a valid number, if so returns true, else returns false"""
    dot = False
    minus = False
    for char in token :
        if char.isdigit() :                                           # allow many digits in a string
            continue
        elif char == "." :                                             # allow only one dot in a string
                if not dot :
                    dot = True
                else :                                  
                    return False
        elif char == "-" and token[0] == "-":    # allow one minus in front
            if not minus :
                minus = True
            else :
                return False
        else :                                                                    # do not allow any other characters in a string
            return False
    return True
    
def add (num1, num2):
    """The add method adds the two values given by the calculate method"""
    answer = float(num1)+float(num2)
    return answer

def subtract (num1, num2):
    """The subtract method subtracts the two values given by the calculate method"""
    answer = float(num1)-float(num2)
    return answer

def multiply (num1, num2):
    """The multiply method multiplies the two values given by the calculate method"""
    answer = float(num1)*float(num2)
    return answer

def divide (num1, num2):
    """The divide method divides the two values given by the calculate method"""
    answer = float(num1)/float(num2)
    return answer

def again ():
    """This method asks the user if they want to continue using this program or not, if so runs through the calculate method, else leaves the program"""
    global gameOn #allows access to variable gameOn and changes the value for it if necessary
    calcAgain = input ("Do you want to continue? [Y/N] > ") #asks user if they want to continue
    if calcAgain == 'Y': #if yes, prgram goes back to the gameOn while loop
        gameOn = True
    elif calcAgain == 'N': #if no, gameOn is turned to false and the cauclate program is done
        print ("Goodbye!")
        gameOn = False

calculate()  