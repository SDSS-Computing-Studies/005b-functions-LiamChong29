#!python3

"""
A function is created by defining using the def command.
The commands will not be executed unless the function is
"called"
"""

# def : tells us that a function is being defined
#     : it is followed by the function name and input parameters
#     : the name must meet the same criteria as naming variables
# all the commands within the function are indented to indicate
# the function block of commands
# the input parameter is required, and is a variable that can be
# used inside the function
# the return value is sent back to the main block of code
# notice the use of comments to indicate what the input parameters are
# as well as what the output is

def double(number):
    # input:
    #   a float number
    # output:
    #   a float number
    # purpose: to generate the value of the input number when doubled

    answer = number * 2
    return answer


# note: The function must be "called", which means using the name
# to execute the code.  The function can be used "inline" or assigned
# to a variable.

print("==This is an inline use of a function")
print("The number 4, when doubled is " + str(double(4)) )
print("\n\n")


print("==This is how the value of the function can be assigned")
x = double(4)
print("The number 4, when doubled is " + str(x) )
print("\n\n")

print("==Functions can receive inputs that are variable:")
num = float(input("Enter a number:"))
print("The number " + str(num) + " when doubled is " + str(double(num)))
print("or")
answer = double(num)
print("The answer is "  + str(answer))
