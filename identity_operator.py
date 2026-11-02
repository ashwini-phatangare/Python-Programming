#IDENTITY OPERATOR : are the operators used to check memory location of the both variables
a = [ 1,2,3]
b = a
c = [1,2,3]
print(a is b) #True,because b references the same object as a
print(a is c)# false, because c is different object with the same content
print(a == c) # True ,because a and c have the same content
print(a is not b)
print( a is not c)