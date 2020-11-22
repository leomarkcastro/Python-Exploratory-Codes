
import keyword                  #I used this in sample_keylist function
from sys import stdin, stdout   #I used this on faster_io
from time import sleep          #I used this on fun_print

# Contains conditional operator
def conditional_operator(value):
    a = 1 if value > 10 else 0
    return a

'''
conditional_operator(5)
'''

# Outputs all the core keywords of python
def sample_keylist():
    print(keyword.kwlist)

# Checks if a variable is a keyword of python
def checkIfFunction(text):
    return keyword.iskeyword(text)

'''
text = "dog"
print ("{} is {}keyword".format(text ,"not a " if checkIfFunction(text)==False else 'a '))
'''

# Shows on how to print on python without it being in a newline
def print_without_newline():
    print("This is a print with a newline")
    print("This will be a print", end = " ")
    print("without a newline involved")

'''
print_without_newline()
'''

# Basic calculator. Input the operator code, then input the first then the second value. No switch function :(
def calculator():
    print("Please select an option: \n" \
    "1) Add \n"\
    "2) Subtract \n"\
    "3) Multiply \n"\
    "4) Divide \n")

    operator = int(input("Please select an operation(1,2,3,4): "))

    x = int(input("Enter first value: "))
    y = int(input("Enter second value: "))

    if(operator == 1):
        print("{} + {} = {}".format(x,y,x+y))
    elif(operator == 2):
        print("{} - {} = {}".format(x,y,x-y))
    elif(operator == 3):
        print("{} * {} = {}".format(x,y,x*y))
    elif(operator == 4):
        print("{} / {} = {}".format(x,y,x/y))
    else:
        print("There are some error in your input")

# This shows the print with format function. Useful for texts with variables involved
def exploring_inputs():
    # This function will show two methods of input system in python

    a = input("Enter anything: ")
    print("{} is a {} type variable".format(a, type(a)))

    a = input()
    print("{} is a {} type variable".format(a, type(a)))

# A straightforward calculator that solicits the direct math equation from the user
def advanced_calculator():

    print("Up to three lines of value will work")
    x,y,z = input("Input the mathematical operation: ").split()

    if(y == '+'):
        print("{} {} {} = {}".format(x,y,z,int(x)+int(z)))
    elif(y == '-'):
        print("{} {} {} = {}".format(x,y,z,int(x)-int(z)))
    elif(y == '*'):
        print("{} {} {} = {}".format(x,y,z,int(x)*int(z)))
    elif(y == '/'):
        print("{} {} {} = {}".format(x,y,z,int(x)/int(z)))

# Input output methods of Python (Faster method does not properly work
def faster_io():
    print("The goal is to collect an input and spew it as fast as possible")

    def before():
        n = input()

        arr = [int(x) for x in input().split()]

        summation = 0

        for x in arr:
            summation += x

        print(summation)

    def after(): #This allegedly spew input and output functions faster
        n = stdin.readline()

        arr = [int(x) for x in stdin.readline().split()]

        summation = 0

        for x in arr:
            summation += x

        stdout.write(summation)

    before()

#How to input a print with padding
def advanced_print():
    print("This is a text, without padding")
    print("This is a text with left padding".ljust(60, '-'))
    print('This is a text with right padding'.rjust(60, '-'))
    print("This is a text with center padding".center(60, "="))

#Prints a waving text by rjust function padding. So fun
def fun_print():
    pad = 40
    while True:
        while pad > 4:
            print("Text".rjust(pad, '-'))
            pad -= 1
            sleep(0.10)
        while pad < 40:
            print("Text".rjust(pad, '-'))
            pad += 1
            sleep(0.10)

print(__name__)