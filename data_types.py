#data Types:

#Type:
# 1.Numerical data type :int,float,complex
# 2.Set 
# 3.Dictionary 
# 4.Boolean 
#5.Sequence data type:  3 types:1.list 2.tuple 3.string

#Numerical data types
# integer data type: integer values
a = 10
print(type(a))
print(a)
# float data type: decimal number/values
b = 2.5
print(type(b))
print(b)
# complex data type:real + imaginary part
c = 2 +3j
print(type(c))
print(c)

#Boolean data type
p = True
print(type(p))
print(p)
q = False
print(type(q))
print(q)

# Set data type
# DEFINATION : Set = set is a collection of elements stored in one variable
# having properties unordered,unique,mutable,heterogenous
s = {1,2,3,4,5,6}
print(type(s))
print(s)

s.add(7)
print(s)
s.add("apple")
print(s)

# Dictionary data type
#DEFINATION: dictionary = dictionary is a collection of key value pairs stored in a one variable.
# having properties unordered , mutable,heterogenous,keys are unique ,values are duplicate.

student = {
    "ID" : 1,
    "Name" : "Ashwini",
    "Age" : 22,
    "city" :"Hydrabad",
}
print(type(student))
print(student)


 # 1.list
 # DEFINATION : list is a sequence data type which stores multiple values in square bracket.
 # having properties mutable,ordered,allow duplicates, heterogenous.

fruits = ["Apple","banana","cherry","Apple"]
print(type(fruits))
print(fruits)


# 2.Tuple
# DEFINATION : tuple is a collection of element stored in one variable
# having properties immutable , ordered ,allow duplicates,heterogenous

tuple1 = (1,2,3,4,5,6,7)
print(tuple1)
print(type(tuple1))


#3.string
# DEFINATION : string is a collection of characters enclosed in " " or ''
# having properties immutable,ordered,homogenous,allow duplicates.
 
name = "abc123"
print(name)
print(type(name))