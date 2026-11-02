# 14 july 2026

# Lambda function - is a small anonymous function in which argument and 
# expression defined in one line.

# Syntax:
# lambda arguments : expression
# """

# square = lambda x : x ** 2
# print(square)

# addition = lambda a,b : a + b
# print(addition(10,20))
# print("-" * 50)

# # even_odd
# even_odd = lambda num : True if num % 2 == 0 else False
# print(even_odd(2))


#=================================================================================
#  MAP FUNCTION - used to iterate all element and returns new collection of sequence.
# =================================================================================
#"""
# map(function,iterable) 
# Applies a function to every moment
#"""

# numbers = [1,2,3,4,5]
# result = list(map(lambda x:x**2,numbers))
# print(result)
# print("-"*50)

# =======================================================================
# FILTER FUNCTION
#==========================================================================

# """
# filter(function,iterable)

# Returns elements that satisfy the condition
# """

# numbers = [10,15,20,25,30,10,15]
# even = list(filter(lambda x : x % 2 == 0,numbers))
# print(even)
# print("-"*50)

# =================================================
# REDUCE FUNCTION
#============================================================
# reduce(function,iterable)
# need to import from functools.
# """
from functools import reduce
numbers = [1,2,3,4,5]
result = reduce(lambda x,y:x+y,numbers)
print(result)
print("-"*50)
#================================================================
# Example 1
# def cube(n):
#     return n ** 3
# print(cube(3))

# Example 2
# marks = [45,60,75,90]
# result = list(map(lambda x: x+ 5,marks))
# print(result)

# # Example 3
# marks = [45,60,75,90]
# passed = list(filter(lambda x : x >= 50,marks))
# print(passed)


# # Example 4
# from functools import reduce 
# marks = [50,60,70,80]
# total_marks = reduce