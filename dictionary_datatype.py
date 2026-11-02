# # 11 july 2026
# # dictionary datatypes

# # what is dictionary ?
# # a dictionary is a collection of key value pairs

# # Properties:
# # 1.Mutable(can modify values)

# # Ordered(python 3.7+)

# # keys are unique

# # values can be duplicate

# # # Heterogenous (different data types allowed) 

# # keys must be immutable(string,int,float,tuple)


# # syntax :
# # dictionary ={key value:pairs}

# # 1. Creating Dictionary
# # print("\n==========Creating Dictionary=======")
# # always key value pair separated by commas
# Student = {
#     "name" : "Arjun",
#     "age" : 25,
#      "course" :"Data analytics"
# }
# print(Student)

# # # 2. Creating Dictionary using dict()

# # print("\n====== dict() constructor=======")
# student2 = dict(name="ashwini",age = 23,city="Hydrabad")
# print(student2)

# # 3.Accessing Values
# #print("\n======= get()=========")
# print(Student.get("course"))
# print(Student.get("city"))
# print(Student.get("email","Not Found"))

# # 4 .  Adding new elements

# print("\n===adding element======")
# Student["city"] = "Mumbai"
# print(Student)
# Student["name"] = "Purva"
# print(Student)

# # updating value
# # print("\n======updating value====")
# Student["age"] = 26
# print(Student)


# # 6.update() method
# # print("\n==== update()======")
# Student.update ({
#   "email" :"purva@gmail.com",
  # })
# print(Student)

# # 7.keys() 
# print(Student.keys())

# # 8.values()
# print(Student.values())

# # 9. items()
# print(Student.items())

# # 10.loop through dictionary
# #print("\n======Loop Through Keys========")

# for key in Student:
#     print(key)

#  #print("\n ======== Loop Through Values =======")
# for value in Student.values():
#     print(value)   

#  # print("\n======== Loop Through Items========")
# for key,value in Student.items():
#     print(key,"-",value)   

# # 11.pop()
# #print("\n===pop()====")
# removed = Student.pop("phone")
# print("Removed Value:",removed)
# print(Student)

# # 12 .popitem()
# # print("\n======popitem()======")
# last_item = Student.popitem()
# print("Removed:",last_item)
# print(Student)

# #13 .setdefault()
# print("\n====setdefault()====")
# Student.setdefault("country","India")
# print(Student)

# #14.copy()
# print("\n====copy()=====")
# new_Student = Student.copy()
# print(new_Student)

# 15. #Clear()
# print("\n=======clear()=====")

# temp = {
#     "A": 10,
#     "B" : 20
# }
# temp.clear()
# print(temp)

# set1 = {1,2,3,4,5,6}
# set1.clear()
# print(set1)

# # 12 july 2026

# # 16.print("\n=======fromkeys()=======")
# keys = ["python","SQL","Power BI"]
# course = dict.fromkeys(keys,0)
# print(course)


# # 17.len()
# print("\n=====len()======")
# print(len(Student))

# # 18.in Operator
# # print("\n======= in Operator=======")
# print("name" in Student)
# print("salary" in Student)

# # 19.del keyword
# # print("\n======del========")
# employee = {
#     "id" :101,
#     "name" : "Rohan",
#     "salary":45000
#     }
# print(employee)
# del employee["salary"]
# print(employee)

# # delete complete dictionary
# del employee
# print(employee)


#Example==========================================================
#1. Create a dictionary of student details.  
# 2. Display all keys and values.  
# 3. Add a new key-value pair.  
# 4. Update an existing value.  
# 5. Delete a key from the dictionary.  

# Student = {
#     "ID" : 1,
#     "Name" : "Ashwini",
#     "Age" : 22,
#     "Class" : "TY"
# }
# print(Student.keys())
# print(Student.values())
# Student["city"] = "Hydrabad"
# print(Student)
# Student.update({"age":23})
# print(Student)
# del Student["Class"]
# print(Student)
#==========================================================================


#Create a dictionary of employee details with ID, Name, Salary, and Department.
# Display all keys.
# Display all values.
# Add a new key-value pair: City.
# Update the employee's Salary.
# Delete the Department key.
# Print the final dictionary.

employee = {
    "ID" : 101,
    "Name" : "Sandip",
    "Salary" : 80000,
    "Department" : "Chemistry"
}
print(employee.keys())
print(employee.values())
employee["city"] = "Hydrabad"
print(employee)
employee.update({"Salary" : 100000})
print(employee)
del employee["Department"]
print(employee)
