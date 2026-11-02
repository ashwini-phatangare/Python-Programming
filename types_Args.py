# 13 july 2026

def info(name,dept,country="India"):
    print(f"Hello,my name is{name} I'm from {dept} department and my office location")
#==============================================================================================

#TYPES OF ARGUMENTS

#1.Positional arguments → values are assigned to parameters based on their position/order.
#2.Keyword arguments → values are assigned using the parameter name.
#3.A default argument : is a parameter that has a predefined value. 
# The default value is used if no argument is passed.”
#4.arbitary argument

#======================================================================================================
# 1.positional argument
info("Sita","HR") # positional argument (order maintain)
# info("hr","Sita")

#2.default argument
info("Pratik","IT","USA")

# 3.Keyword argument
info(dept="HR",name = "Sita")

# 4.arbitary argument
info(dept = "Hr",name = "Sita")

# 4A .VARIABLE LENGTH ARGUMENT (*args)

# method overloading - same parameter but different arguments
# method overriding - same parameter and same arguments

def total(*numbers):
    print("Numbers :", numbers)
    print("Sum",sum(numbers))

total(10,20)
total(10,20,30,40)

# 4B : keyword length arbitary argument (**kwargs)
def details(**data):
    print(data)
details(name = "divya",age = 23,city = "pune")
details(name="divya",age = 23,city = "pune",course = "DA",fees  = 56000)    
