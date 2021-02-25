#!python3

"""
Create a function called distance()
Input is 2 tuples, that each contain an (x,y) coordinate.
Return value is the distance between the (x,y) coordinates.
Note that the coordinates should be signed (positive or negative) floats
(2 points)
"""
import math

def distance(x,y):
    return math.hypot(y[0]-x[0],y[1]-x[1])

x=distance((2,4), (6,3))
print(x)