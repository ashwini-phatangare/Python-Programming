# 13 july 2026

# Functions

# what is a function?
# A function is a block of reusable code that performs a specific task.
#or
# a function is a block of code used to perform specific task/operation.

# Advantage of functions
#1.Code Resusability
#2. reduce code duplication
# 3.easy to read
# 4.easy to debug
# 5.improves program structure

# Syntax
# def function_name(parameter)


#========================================
# 1.DEFINING A FUNCTION
#====================================================

def greet(name):
 print(f"{name} Welcome to Python Functions!")
greet("Sita")
greet("Rahul")
print("-"*60)

# There are two types of function
#1.Built - in functions

#2. user-defined functions

# Built-in functions - Functions which already defined by python interpreter

numbers = [10,20,30,40]
print("length:",len(numbers))
print("Maximum:",max(numbers))
print("Minimum:",min(numbers))
print("Sum:",sum(numbers))
print("Type:",type(numbers))
#=========================================================
#  TYPES OF USER DEFINED FUNCTion

# 1.Non Parameterized function
#2.Parameterized Function
#====================================================

#------------------------------------------------
# 1.Non - Parameterized Function
#-------------------------------------------------

def add():
  a = 10
  b = 20
  c = a + b
  print(c)
add()
print("-"*60)

#------------------------------------------
# 2.Parameterized function
#-----------------------------------------
def Add(a,b):
  print(a+b)
Add(100,200)  
Add(120,230)
print("-"*60)

#=============================================
#PARAMETER VS ARGUMENTS
#==================================================

# Argument
# Actual value passed while calling the function.
# Or
# arguments are the values passed at the time of function calling.
# """

# Parameter
# Variable written inside the function definition.
# or
# parameters are the variables which assignment at the time of function creation.

#========================================================

# types of Arguments
#========================================================
