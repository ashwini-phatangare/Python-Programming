# # #11 july 2026

# # # tuple data type
# # # tuple properties
# # t = (1,2,3,4,5)
# # print(type(t))

# # # tuple properties
# # # immutable - cannot be changed after creation
# # # ordered - maintains the order of element
# # print(t[0]) # 1 
# # # heterogenous- can contain elements of different type
# # t2 = (1,"hello",3.14,True)
# # print(t2)

# # # allow duplicates - can contain duplicates elements
# # t3 = (1,2,2,3,4)
# # print(t3)

# # # count() - returns the number of occurrences of an element in the tuple
# # print(t3.count(2)) #2

# # # index() - returns the index of the first occurrence of an elemnt in the tuple
# # print(t3.index(2)) # 1

# tuple_1 = (1,2,3,4,5,6)
# print(tuple_1)
# # add 7 in above tuple
# # type casting
# l = list(tuple_1)
# l.append(7)
# #print(l)
# t1 = tuple(l)
# print(t1)

#========================================
#Tuple Programs (5) 
# 1. Create a tuple and display its elements.  
# 2. Count occurrences of an element.  
# 3. Find the index of an element.  
# 4. Find the maximum and minimum values in a tuple.  
# 5. Convert a tuple into a list.  
 
t = (1,2,3,3,4,5)
# print(tuple(t))
# print(t.count(3))
# print(t.index(4))
# print(max(t))
# print(min(t))
l =list(t)
print(l)
t1 = tuple(t)
print(t1)