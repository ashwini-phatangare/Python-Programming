# 10 july 2026
# string properties and methods
s = "Hello,World!"
print(s)
print(type(s))
print(s[0])

## string properties
# immutable - cannot be changed after creation
# ordered - maintains the order of character
# homogenous - same type of data
# allow duplicates - can contain duplicate characters

# string methods
# upper() - converts all characters in the string to uppercase
s_upper = s.upper()
print(s_upper)

# lower() - converts all characters in the string to lowercase
s_lower = s.lower()
print(s_lower)
print(s.capitalize()) # sentence case .word ch first letter capital krto.mhnje hello world ha word ahe tr tyala Hello world as print krto.
print(s.title()) # jr 2 word astil aaplya kde tr tyance first letter capital krto
# hello word ha word ahe tr tyala Hello World as print krnar

# strip() - removes leading and trailing whitespace from the string
# donhi side che blankspace remove hotat
s_strip = "  Hello , World!   ".strip()
print(s_strip)
print(len(s_strip))


# lstrip()- removes leading whitespace from the string
#  only left side cha blankspace remove hoto
s_lstrip = "  Hello,World!   ".lstrip()
print(s_lstrip)
print(len(s_lstrip))



# rstrip() - removes trailing whitespace from the string
# only right side cha blankspace remove hoto
s_rstrip = " hello ,world!  ".rstrip()
print(s_rstrip)
print(len(s_rstrip))

# replace() -replace all occurrences of a substring with another substring
s_replace = s.replace("Hello","Hi")
print(s_replace)

# split() - splits the string into a list of substrings based on specified delimiter
s1 = "Hello I am python developer"
s_split = s1.split(" ")
print(s_split)

# join() - joins a list of strings into a single string using a specified delimiter
s_join = "".join(s_split)
print(s_join)

# find() - returns the index of the first occurence of the substring in the string,
# or -1 if not found 
text = "Hello python"
s_find = text.find("python")
print(s_find)

#index() - returns the index of the first occurrence of a substring in the string,
# or raise a ValueError if not found
s_index = text.index("java")
print(s_index)



#=================================================================
#String Programs (5) 
# 1. Count the number of vowels in a string.  
# 2. Reverse a string.  
# 3. Check whether a string is a palindrome.  
# 4. Count uppercase and lowercase letters.  
# 5. Replace all spaces with underscore


