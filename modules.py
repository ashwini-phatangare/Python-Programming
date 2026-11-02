# 2 August 2026

# Modules

# Definition :
#------------------------------------------------
# A module is a python file(.py) that contains reusable code 
# such as functions ,classes,variables,and constants

# Advantages :

# 1.Code reusability
# 2.Easy Maintainance
# 3.better Code organizations
# 4. Reduce Code Duplication


# Types Of Modules
#--------------------------------------------------------------

# 1. Built - in Modules
#   -  math
#   -   random 
#    -   os 
#    -   datetime
#     -   calendar
#      -  statistics
#      -   time
#       -  strings
#       -    sys
# 
#  2. User Defined Modules
# 
# Created by programmer

# ---------------------------------------------------------
# Ways to import modules:
# ----------------------------------------------


# 1.import module
# import math


# 2. import module as alias
# import math as m

# 3.from module import function
# from abc import ABC,abstractmethod

# 4 .from module import *
# from math import *

#===========================================================================

print("\n===================")
print("1.IMPORT MODULE")
print("==============================================")

import math
print("Square root of 64 = " ,math.sqrt(64))
print("Factorial of 5 = ",math.factorial(5))
print("power = " ,math.pow(2,5))

#=============================================================

# 2.IMPORT MODULE AS ALIAS

#=============================================================
print("\n===================")
print("1.IMPORT AS ALIAS")
print("==============================================")

import math as m
print("PI =" ,m.pi)
print("Ceil =",m.ceil(4.2))
print("Floor = ",m.floor(4.9))

#========================================================

# FROM IMPORT

#===========================================================

print("\n===================")
print("1.FROM IMPORT")
print("==============================================")

from math import *

print("sin(90) =", sin(radians(90)))
print("cos(0) =", cos(radians(0)))

#============================================

# RANDOM MODULE

#==============================================
print("\n===================")
print("RANDOM MODULE")
print("==============================================")

import random
print("Random Integer = ",random.randint(1,100))
colors = ["Red","Blue","Green","Black"]
print("Random Color =",random.choice(colors))
random.shuffle(colors)
print("After Shuffle = ",colors)


#=====================================================

# DATETIME MODULE

#=========================================================
print("\n===================")
print("2.DATETIME MODULE")
print("==============================================")

import datetime as dt
today = dt.datetime.now()
print("Current Date & Time =",today)
print("Year =",today.year)
print("Month = ",today.month)
print("Day =",today.day)

#==========================================

# CALENDAR MODULE

#========================================
print("\n===================")
print("CALENDAR MODULE")
print("==============================================")

import calendar
print(calendar.month(2026,8))

#=========================================================
# STATISTICS MODULE

#=====================================================
print("\n===================")
print("STATISTIC MODULE")
print("==============================================")

import statistics

marks = [70,80,90,85,95]

print("Mean = ",statistics.mean(marks))
print("Median= ",statistics.median(marks))
print("Mode= ",statistics.mode(marks))

#+===================================================

print("\n===================")
print("STRING MODULE")
print("==============================================")

import string
print("Uppercase =",string.ascii_uppercase)
print("lowercase =" ,string.ascii_lowercase)
print("Digits =" ,string.digits)

#==========================================================================

# TIME MODULE
#=====================================================
print("\n===================")
print(" TIME  MODULE")
print("==============================================")

import time
print("Current Time =",time.strftime("%H:%M:%S"))


#====================================================================

# OS MODULE

#===========================================================

print("\n===================")
print(" OS  MODULE")
print("==============================================")

import os
print("Current Directory")
print(os.getcwd)
print("\nFiles in current folder")

