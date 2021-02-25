#!python3

def largest(myList):
    myList.sort()
    return (myList[0],myList[-1])

print( largest([3,5,6,62,2,3,4,42]) )
x,y = largest([3,5,6,62,2,3,4,42])
print(x)
print(y)
x = 3
print(x)
