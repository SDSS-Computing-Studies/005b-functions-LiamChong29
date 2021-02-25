#!python3
""" 
Create a function called hypotenuse()
Input is 2 float numbers and a boolean
If the boolean is True, then find the hypotenuse
If the boolean is False, then the larger number is the hypotenuse
Return the missing side
(2 points)
"""
import math

def hypotenuse(a,b,c):
    if c == True:
        return math.hypot(a,b)
    elif c == False:
        return math.sqrt(a**2 - b**2)

x = hypotenuse(3,4,True)
print(x)

y = hypotenuse(13,5,False)
print(y)