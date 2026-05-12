# Functions are used to:

# reuse code
# make projects clean
# reduce repetition
# write professional programs

# Every real software project uses functions.
#Basic syntax of a function:

def great():
    print("Hello Kaushal")
great() # calling function
print("__________FIRST PROGRAM___________________")
# Function with parameters:
def greet(name):
    print("hello " ,name)
greet("kaushal")
greet("royal")
print("__________SECOND PROGRAM___________________")
#Why important to use functions?
#Used everywhere:
#login systems
#APIS
#Calclators
#banking systems
#3 program  imp concept ("FUNCTION WITH RETURN")
def add(a,b):
    return a+b
result=add(10,20)
print(result)
print("__________THIRD PROGRAM___________________")
#DIFFERENCE BETWEEN PRINT AND RETURN:
# PRINT():--> shows output, temporary,less professional
# RETURN():--> Sends value back, reusable,very important for big projects
#4 Even Or Odd program using function 
def check_even_odd(num):
    if num%2==0:
        return "even"
    else:
        return "odd"
    
print(check_even_odd(10))
print(check_even_odd(15))
print("__________FOURTH PROGRAM___________________")
#Mathematical logic
# n mod 2=0
# if rem is 0-->Even
#5 Find Largest Number Using Function
def find_largest_num(a,b):
    if a>b:
        return a
    else:
       return b

print(find_largest_num(15,20))
print("__________FIFTH PROGRAM___________________")
#6 calculation uing function
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

print(add(10, 5)," addition")
print(subtract(10, 5)," subtraction")
print(multiply(10, 5)," multiplication")
print("__________SIXTH PROGRAM___________________")
#7self-->create a function using to check weather a number is pos,neg or zero
def check_num(num1):
    if num1>0:
        print("positive")
    elif num1<0:
        print("Negative")
    else:
        print("zero")
print(check_num(10))
print(check_num(-2))
print(check_num(0))
print("__________SEVENTH PROGRAM___________________")