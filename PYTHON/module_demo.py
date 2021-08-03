#To use the functions in another file in python

import arithmetic_functions
x = int(input("Enter the first number: "))
y = int(input("Enetr the second number: "))
# ADD
z = arithmetic_functions.add(x,y)
print("The sum of x and y is : %d"%(z))
# DIFFERENCE
z = arithmetic_functions.sub(x,y)
print("The differnce of x and y is : %d"%(z))
# MULTIPLY
z = arithmetic_functions.mul(x,y)
print("The product of x and y is : %d"%(z))
# DIVISION
z = arithmetic_functions.div(x,y)
print("The division of x and y is : %f"%(z))
# EXPONENTIAL
z = arithmetic_functions.exp(x,y)
print("The power of x to y is : %d"%(z))
# AVERAGE
z = arithmetic_functions.avg(x,y)
print("The average of x and y is : %f"%(z))
# REMAINDER
z = arithmetic_functions.rem(x,y)
print("The remainder for x and y is : %d"%(z))
