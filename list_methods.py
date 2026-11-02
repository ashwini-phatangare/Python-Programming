# 7 july 2026

#list is a collection of elements enclosed in square bracket and stored in one variable having properties
# mutable(you can add or remove elements)

# ordered (it maintain and follow the order of element)

# heterogenous(you can store diff types of values in single list)

# allow duplicates

# list properties and methods
# l = [1,2,3,4,5]
# print(l)
# print(type(l))

# #list properties
# # mutable - can be changed after creation
# l[0] = 10
# print(l)

# # ordered - maintains the order of elements
# print(l[0])  #10

# # heterogenous - can contain elements of different types
# l2 = [1,"hello",3.14,True]
# print(l2)

# # allow duplicates - can contain duplicates elements
# l3 = [1,2,2,3,4]
# print(l3)

# list methods
l = [1,2,3,4,5]
# append() - adds an element at a specific index
l.append(6)
print(l)


#insert() - adds an element at a specific index
l.insert(0,0)
print(l)


## extend()- adds elements from another list to the end of the list
l.extend([7,8,9])
print(l)

# remove() - removes the first occurence of an element from the list
l.remove(2)
print(l)

# pop() - removes and returns the element of specific index(default is the last element)
l.pop(3)
print(l)

#sort()- sorts the elements of the list in ascending order
l.sort()
print(l)

# reverse() - reverse the order of the elements in the list
l.reverse()
print(l)

# clear()- removes all the elements from the list
l.clear()
print(l)

#====================================================
#List Programs (5) 
# 1. Find the largest element in a list.  
# 2. Find the smallest element in a list.  
# 3. Calculate the sum of all list elements.  
# 4. Remove duplicate elements from a list.  
# 5. Sort the list in ascending order. 
l = [20,30,40,40,50]
print(max(l))
print(min(l))
print(sum(l))
l.remove(40)
print(l)
l.sort()
print(l)




