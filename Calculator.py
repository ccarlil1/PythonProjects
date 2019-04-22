# -*- coding: utf-8 -*-
"""
Created on Thu Apr 18 18:49:44 2019

@author: Casey
Title: Simple Calculator

"""

def pickFunction(operation, num1, num2):
    if operation == "A" or operation == "a":
        return addition(num1, num2)
    
    elif operation == "S" or operation == "s":
        return subtraction(num1, num2)
    
    elif operation == "M" or operation == "m":
        return multiplication(num1, num2)
    
    elif operation == "D" or operation == "d":
        return division(num1, num2)
      
    else: return "Error"
    

def addition(num1, num2):
    answer = num1 + num2
    return answer

def subtraction(num1, num2):
    answer = num1 - num2
    return answer

def multiplication(num1, num2):
    answer = num1 * num2
    return answer

def division(num1, num2):
    try:
        answer = num1 / num2
    except ZeroDivisionError:
        print("Cannot divide by 0")
    else:
        return answer


while True:
    print("A - Add  S - Subtract  M - Multiply  D - Divide  Q - Quit")
    userChoice = input()
    
    if userChoice == "Q" or userChoice == "q" or userChoice == "quit":
        break
    
    print("First Number: ")
    number1 = float(input())
    print("Second Number: ")
    number2 = float(input())
    
    print("Answer: " + str(pickFunction(userChoice, number1, number2)))

