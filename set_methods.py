# 8 july 2026
# # set data type properties and methods
# s = {1,2,3,4,5}
# print(s)
# print(type(s))

# # set properties:

# # 1.mutable : can be changed after creation
# s.add(6)
# print(s)

# # unordered - does not maintain the order of elements
# # heterogenous - can contain elements of different types
# s2 = {1,"hello",3.14,True}
# print(s)

# # unique elements - can not contain duplicate elements.
# s3 ={1,2,2,3,4}
# print(s3) #(1,2,3,4)

# # set methods
# s.remove(3)
# print(s)
# s.discard(10) # does not raise an error if the element is not found
# print(s)
# s.pop() # removes and return an arbitrary element from the set
# print(s)
# s.update({7,8,9})
# print(s)
# s.clear()
# print(s)

a = {1,2,3}
b = {3,4,5}
print("union:",a|b)
print("intersection:",a&b)
print("A-B",a.difference(b))
print("B-A:",b.difference(a))
print("symmetric_difference:",a.symmetric_difference(b))

c = {10,20,30,40,50}
d = {10,30}
 # superset
 # subset
 # isdisjoint()

# print("is there no common element?",c.isdisjoint(d))
# print("is c is superset>:",c.issuperset(d))
# print("is d is subset of c?",d.issubset(c))


# Set Programs (5) 
# 1. Create two sets and perform union.  
# 2. Find the intersection of two sets.  
# 3. Find the difference of two sets.  
# 4. Add and remove elements from a set.  
# 5. Check whether an element exists in a set. 

# a = {1,2,3,4,5}
# b = {4,5}
# print("union",a|b)
# print("Intersection",a&b)
# print("Difference",a-b)
# a.add(6)
# print(a)
# a.remove(2)
# print(a)
# if 4 in a:
#     print("element exist in set")
# else:
#      print("element does not exist")

