# # # # Section A - append()

# # # # question 1 :Create the following list.
# # fruits =  ["Apple","Banana","Mango"]
# # # Perform the following operations
# # #Add "orange"
# # # Add "Grapes"
# # # Add "Pineapple"
# # fruits =  ["Apple","Banana","Mango"]
# # fruits.append("Orange")
# # fruits.append("Grapes")
# # fruits.append("Pineapple")
# # print(fruits)

# # # # Question 2
# # # # create the following list

# # # #perform the following operations
# # # #Add 95
# # # #Add 100
# # # #Add 85
# # # #print the final list
# # marks = [65,72,88,91]
# # marks.append(95)
# # marks.append(100)
# # marks.append(85)
# # print(marks)

# # # Question 3
# # # Create the following list
# # countries = ["India","japan","canada"]
# # countries.append("Australia")
# # countries.append("Germany")
# # countries.append("Brazil")
# # print(countries)
# #------------------------------------------------------------------------------------------------------------------

# # Section B : insert()

# # Question 4
# # create the following list
# cities = ["Pune","Mumbai","Delhi"]
# # perform the following operations
# # insert "Nagpur " at index 1
# # insert "Nashik " at index 0
# # insert "Kolhapur " at index 3
# cities = ["Pune","Mumbai","Delhi"]
# cities.insert(1,"Nagpur")
# cities.insert(0,"Nashik")
# cities.insert(3,"Kolhapur")
# print(cities)

# # Question 5
# # create the following list
# #yellow at index 2
# #black at index 4
# # white at index 1
# colors = ["Red","Green","Blue"]
# colors.insert(2,"Yellow")
# colors.insert(4,"Black")
# colors.insert(1,"White")
# print(colors)

# # Question 6 
# # Create the following list
# # SQl at index 1
# # javascript at index 4
# languages = ["python","java","c++"]
# languages.insert(1,"SQL")
# languages.insert(4,"javascript")
# print(languages)

# #-------------------------------------------------------------------------------------------------

# # Section C
# # Question No : 7
# # create two lists
# # Merge both lists using extend()
# even = [2,4,6,8]
# odd = [1,3,5,7]
# even.extend(odd)
# print(even)

# #Question : 8
# # Create
# students = ["rahul","Amit"]
# new_students =["Sneha","Riya","Pooja"]
# students.extend(new_students) 
# print(students)

# # Question : 9
# # Create
# electronics = ["Laptop","Monitor","Speaker"]
# accessories = ["Mouse" ,"Monitor" ," Speaker"] 
# electronics.extend(accessories)
# print(electronics)             

# #-----------------------------------------------------------------------------------------------------

# # Section D - remove()

# # Question 10
# #create
# animals = ["Dog","Cat","Tiger","Cow","Cat"]
# animals.remove("Cat")
# animals.remove("Cow")
# print(animals)

# # Question 11:
# # create
# numbers = [15,25,35,45,55]
# numbers.remove(35)
# numbers.remove(55)
# print(numbers)


# # Question 12
# # create
# subjects = ["Math","English","Science","History"]
# subjects.remove("English")
# subjects.remove("History")
# print(subjects)

# #---------------------------------------------------------------------------------------------------------------

# # Section E : pop()

# # Question 13
# # create
# # pop last element
# # pop element at index 2
# students = ["Amit","Rahul","Sneha","Pooja","Riya"]
# students.pop(4)
# students.pop(2)
# print(students)

# # Question 14
# # Create
# # Remove the value at index 3
# prices = [250,500,750,1000,1250]
# prices.pop(3)
# print(prices)

# # Question 15
# # Create
# # remove 
# # last book
# # first book
# books = ["Python","SQL","Excel","Power BI","Tableau"]
# books.pop(4)
# books.pop(0)
# print(books)

# #----------------------------------------------------------------------------

# # Section F - sort()
# # Question 16
# # create
# # sort the list
# ages = [45,12,67,23,89,34]
# ages.sort()
# print(ages)

# # Question 17 
# #create
# # arrange the names alphabetically
# names = ["Karan","Ankit","Priya","Bhavana","Rohit"]
# names.sort()
# print(names)

# # Question 18
# # create
# prices = [450,250,850,120,980,620]
# prices.sort()
# print(prices)

# #-------------------------------------------------------------------------------------------------------

# # Section G: reverse()
 
#  # Question : 19
# #Create
# days = ["Monday","Tuesday","thursday","Friday","Saturday","Sunday"]
# days.reverse()
# print(days)

# # Question 20
# # create
# roll_no = [101,102,103,104,105]
# roll_no.reverse()
# print(roll_no)

# # Question 21:
# # Create
# months = ["jan","feb","mar","apr","may","jun"]
# months.reverse()
# print(months)

# #-------------------------------------------------------------------------------------------------

# # Section H : clear()

# # Question 22
# # create
# subjects = ["mats","science","english","history"]
# subjects.clear()
# print(subjects)

# # Question 23 
# # create 
# cart = [ "laptop","Mouse","Keyboard","Monitor"]
# cart.clear()
# print(cart)

# # Question 24
# # create 
# fruits = ["Apple","Banana","Orange","Mango"]
# fruits.clear()
# print(fruits)

#----------------------------------------------------------------------------

# Section I :  Mixed Practice

# Question : 25
# create 
#append jasmine
#insert sunflower at index 2
# Extend with Tulip and marigold
# Remove lily
# sort the list
# Reverse the list
# flowers = ["Rose","Lily","Lotus"]
# flowers.append("jasmine")
# flowers.insert(2,"Sunflower")
# flowers.extend(["Tulip","marigold"])
# flowers.remove("Lily")
# flowers.sort()
# flowers.reverse()
# print(flowers)

# Question 27
# create
# scores = [45,89,65,78,92,56]
# perform 
# Append 100
# Remove 65
# Sort
# Reverse
# scores = [45,89,65,78,92,56]
# scores.append(100)
# scores.remove(65)
# scores.sort()
# scores.reverse()
# print(scores)

# Question 28
# create
# employees = ["Raj","Simran","Amit","Neha"]
# perform
# insert karan at index 2
# pop last employee
# Extend with priya and sahil
# Remove Raj
# employees = ["Raj","Simran","Amit","Neha"]
# employees.insert(2,"karan")
# employees.pop(3)
# employees.extend(["priya","sahil"])
# employees.remove("Raj")
# print(employees)


# Question :29
# create an empty list
# take 5 fruits from the user input() and append

# fruits = []
# for i in range(5):
#  fruit = input(f"enter a fruits{i + 1}:")
#  fruits.append(fruit)
# print("Final list :",fruits)

# Question :30
# take 10 numbers from the user
# perform 
# Sort
# Reverse
# numbers = []
# for i in range(10):
#     num = int(input(" enter a number:"))
#     numbers.append(num)
# print("final list of numbers:",numbers)
# numbers.sort()
# print("sorted list:",numbers)
# numbers.reverse()
# print("final list(desc):",numbers)


# Question 31
# create a shopping cart
# take 5 products from the user
# Remove one product entered by the user
# Add one new product
# display the updated cart
# cart = []
# # take products
# for i in range(5):
#     product = input(f"enter product {i + 1} ")
#     cart.append(product)
#     print("shopping cart:",cart)

#     # remove product
# remove_product = input("enter a product to remove")
# if remove_product in cart:
#     cart.remove(remove_product)
#     print("product remove successfully")
# else:
#     print("product not found")
#     # add a new product
# new_product= input("enter a new product")
# cart.append(new_product) 
# print("updated shopping cart:",cart)       




# Question no 32:
# create two lists of employee
# merge both lists using extend
# sort the merge list alphabetically
# Reverse the sorted list
# emp1 = ["Amit","Ram","Sham"]
# emp2 = ["Gita","Sita","Anjali"]
# emp1.extend(emp2)
# emp1.sort()
# emp1.reverse()
# print(emp1)

# OR 

# Create two empty lists
emp1 = []
emp2 = []

# Take input for first list
print("Enter 3 employee names for List 1:")
for i in range(3):
    name = input("Enter employee name: ")
    emp1.append(name)

# Take input for second list
print("\nEnter 3 employee names for List 2:")
for i in range(3):
    name = input("Enter employee name: ")
    emp2.append(name)

# Display both lists
print("\nList 1:", emp1)
print("List 2:", emp2)

# Merge both lists
emp1.extend(emp2)
print("\nMerged List:", emp1)

# Sort alphabetically
emp1.sort()
print("Sorted List:", emp1)

# Reverse the sorted list
emp1.reverse()
print("Reverse Sorted List:", emp1)

