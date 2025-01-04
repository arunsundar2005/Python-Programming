# The "if-elif-else" statement allows for multiple conditions to be checked sequentially. 
# If the first condition is false, it checks the next "elif" condition, and so on. 
# If none are true, the "else" block is executed.


"""
Syntax: 

if condition1:
    print("Condition 1 is True")
elif condition2:
    print("Condition 2 is True")
else:
    print("All conditions are False")


"""


x = int(input("Enter a number"))

if x.is_integer:
    print("The number is zero")
elif x % 2==0:
    print("The number is even")
else :
    print("The number is odd")

