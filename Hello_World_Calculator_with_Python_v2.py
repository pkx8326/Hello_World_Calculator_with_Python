#!/usr/bin/env python
# coding: utf-8

# In[5]:


#This is the v 2.0 of the simple calculator program
#This program demonstrates the use of functions with outputs

def plus(a,b):
    result = a+b
    return result

def minus(a,b):
    result = a-b
    return result

def multiply(a,b):
    result = a*b
    return result

def divide(a,b):
    result = round(a/b,1)
    return result

operators = ["+","-","*","/"]

logo = """
 _____________________
|  _________________  |
| |   Hello World!  | |  .----------------.  .----------------.  .----------------.  .----------------. 
| |_________________| | | .--------------. || .--------------. || .--------------. || .--------------. |
|  ___ ___ ___   ___  | | |     ______   | || |      __      | || |   _____      | || |     ______   | |
| | 7 | 8 | 9 | | + | | | |   .' ___  |  | || |     /  \     | || |  |_   _|     | || |   .' ___  |  | |
| |___|___|___| |___| | | |  / .'   \_|  | || |    / /\ \    | || |    | |       | || |  / .'   \_|  | |
| | 4 | 5 | 6 | | - | | | |  | |         | || |   / ____ \   | || |    | |   _   | || |  | |         | |
| |___|___|___| |___| | | |  \ `.___.'\  | || | _/ /    \ \_ | || |   _| |__/ |  | || |  \ `.___.'\  | |
| | 1 | 2 | 3 | | x | | | |   `._____.'  | || ||____|  |____|| || |  |________|  | || |   `._____.'  | |
| |___|___|___| |___| | | |              | || |              | || |              | || |              | |
| | . | 0 | = | | / | | | '--------------' || '--------------' || '--------------' || '--------------' |
| |___|___|___| |___| |  '----------------'  '----------------'  '----------------'  '----------------' 
|_____________________|
"""

print(logo)
print("Welcome to the simple calculator with Python!")

calagain = ("")
result = 0

while calagain not in ("Q", "q"):
    
    if calagain == "Y" or calagain == "y":
        first_num = result
    else:
        while True:
            try:
                first_num = float(input("What's the first number?: "))
                break
            except ValueError:
                print("Please input only numbers.")
                
    
    for items in operators:
        print(items)
    oper = []
    while oper not in operators:
        oper = input("Choose an operator: ")

    while True:
        try:
            second_num = float(input("What's the second number?: "))
            break
        except ValueError:
            print("Please input only numbers.")

    if oper == "+":
        result = round(plus(first_num,second_num),1)
        print(f"The result is {result}.")
    elif oper == "-":
        result = round(minus(first_num,second_num),1)
        print(f"The result is {result}.")
    elif oper == "*":
        result = round(multiply(first_num,second_num),1)
        print(f"The result is {result}.")
    else:
        result = round(divide(first_num,second_num),1)
        print(f"The result is {result}.")


    calagain = ("")
    while calagain not in ("Y", "y", "N", "n", "Q", "q"):
        calagain = input(f"Continue the calculation with {result} Y/N?, or input Q to quit :")

