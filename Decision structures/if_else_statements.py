"""

The "if-else" statement allows us to execute one block of code if the condition is true,
and another block if the condition is false.

Syntax: 

if condition:
    print("Condition is True")
else:
    print("Condition is False")

"""

x = int(input("Enter a number"))

if x%2 == 0:
    print("The number is even")
else :
    print("The number is odd")


## Inline If statements:

"""
Syntax:

result = "True" if condition else "False"


"""


result = "The number is even" if x%2==0 else "the number is odd"
print(result)