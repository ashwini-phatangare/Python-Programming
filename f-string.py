# f-string(preferred)
# introduced in python 3.7
# variables are placed inside {}


name = "BOB"
age = 25
salary = 45000.5
print(f"Name:{name},Age:{age}")
print(f"Salary:{salary:,.2f}")#comma +2 decimal places 
x,y = 10,3
print(f"Sum:{x + y}")