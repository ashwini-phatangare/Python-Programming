# we can assigns variables in this way
age = 30
AGE = 50
Age = 75
print(age)
print(AGE)
print(Age)

# Type of Variable
# 14 july 2026

#program 1 : print Numbers from 1 to N Using Recursion
# Print numbers from 1 to N using recursion

# def print_numbers(n):
#     if  n == 0:
#         return
#     print_numbers(n-1)
#     print(n)

# num = int(input("Enter a number:")) 
# print_numbers(num)   

# Program 2: Find factorial using recursion
# Factorial using recursion

# def factorial(n):
#     if n == 0 or n == 1:
#         return 1
#     return n * factorial(n-1)

# num = int(input("enter a number:"))
# print("Factorial = ",factorial(num))


#Program 3 : find the Fibonacci series using recursion
# Fibonacci Series using recursion

def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

terms = int(input("enter number of terms:"))
#print(fibonacci(9))
for i in range(terms):
 print(fibonacci(i),end = "")
