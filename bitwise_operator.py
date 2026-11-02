# BITWISE OPERATOR
#Easy Trick for Exams
#<<	Left Shift	Multiply by 2ⁿ
# eg.5 × 2¹ = 10
# eg.5 × 2² = 20
#eg.5 × 2³ = 40
#>>	Right Shift	Divide by 2ⁿ (floor for positive numbers)
# eg .20 ÷ 2¹ = 10
# eg.20 ÷ 2² = 5
# eg .20 ÷ 2³ = 2.5 → 2 (floor)

a = 5
b = 4
print( a & b) # BITWISE AND
print( a | b) # BITWISE OR
print( a ^ b)# bitwise XOR
print(a >> 2) # bitwise rightshift 
print(a <<  2)# biwise leftshift 
