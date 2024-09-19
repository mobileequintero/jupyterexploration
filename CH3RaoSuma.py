# Name: Enrique Alejandro Quintero Garcia
# Date: 09/07/2024
# Program: Chapter 3
# Description and Extra Information: 
# This application is a one minicalculator
# The frist step is type your name
# the second step is put two numbers 
# the third is choose the operator Symbol

# CONSTANTS
GREET = "Hello"
TITLE = "Welcome to Mini Calculator Program!"
LINE = '------------------------------------'
DIV_ZERO_ERROR= "DIVISION BY ZERO ERROR!"
INVALID_OP_ERROR = "is a INVALID OPERATOR!"
ASSIGMENT_OP = "="

# prompt/input user's name
name = input("Enter your name:")

# display greeting, title and line
print(LINE)
print(GREET,name,TITLE)
print(LINE)

# prompt/input for first integer number
firstInt = int(input("Enrter first integer: "))

# prompt/input for second integer number
SecondInt = int(input("Enrter second integer: "))

# prompt/input for first integer number
opSym = input("Enrter Operator Symbol: ")
print ("Operator Symbol: ",opSym)
print(LINE)

if opSym == "**":
    print(firstInt,opSym,SecondInt,ASSIGMENT_OP,firstInt ** SecondInt)
elif opSym == "+":
    print(firstInt,opSym,SecondInt,ASSIGMENT_OP,firstInt + SecondInt)
elif opSym == "-":
    print(firstInt,opSym,SecondInt,ASSIGMENT_OP,firstInt - SecondInt)
elif opSym == "*":
    print(firstInt,opSym,SecondInt,ASSIGMENT_OP,firstInt * SecondInt)        
elif opSym == "/" or opSym == "//" or opSym == "%":
    print("Valor del operador:",opSym)
    if SecondInt == 0:
        print(DIV_ZERO_ERROR)
    else:
        if opSym == "/":
            print(firstInt,opSym,SecondInt,ASSIGMENT_OP,firstInt / SecondInt)        
        elif opSym == "//":
            print(firstInt,opSym,SecondInt,ASSIGMENT_OP,firstInt // SecondInt)
        elif opSym == "%":
            print(firstInt,opSym,SecondInt,ASSIGMENT_OP,firstInt // SecondInt)
else:
    print(INVALID_OP_ERROR)
# Use elifs and check for    