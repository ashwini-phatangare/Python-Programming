# 10 july 2026
# String indexing and slicing.


# string indexing - extracting element from a specific position.
# positive indexing - left to right - start from 0
# negative indexing - right to left - start from -1

s = "python"
print(s[0])
print(s[-1])
print(s[5])

# string slicing
s1 = "Python  programming"
print(s1[0:7])
print(s1[:7])
print(s1[7:18])
print(s1[7:])
print(s1[::2])
print(s1[::-1])    

# concatenate : used to join two strings
t1 = "python"
t2 = "program"
t3 = t1 + t2
print(t3)



s = "abc123"
print(s.isalnum()) # alphabet + numeric
print(s.isalpha()) # alphabet
print(s.isdigit()) # digit

